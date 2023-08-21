import sys
import time
import scapy.all as scapy
import json
import os

from pymongo import MongoClient
from maclookup import ApiClient
from maclookup import exceptions

f = open('setup.json', "r")
data = json.loads(f.read())
f.close()
api = data['wifi']['deauther_detector']['api']
adapter = data['wifi']['deauther_detector']['adapter_name_before']
database = data['wifi']['database']

# Mac lookup client - free for 1000 requests
mac_client = ApiClient(api)

# MongoDB connection
client = MongoClient(database)
db = client['deauth_attacks']
attacks = db['attacks']

# Router mac
HARDCODED_ROUTER_MAC = "20:4e:7f:0e:df:46"

# Monitor mode wifi card
monitor_device = "wlan0"

class DeauthenticationDetector:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.data = {}
        self.Sniffing_Start()

    def extract_packets(self, pkt):
        if pkt.haslayer(scapy.Dot11Deauth) and pkt.addr2 is not None and pkt.addr3 is not None:
            addr1 = pkt.addr1
            addr2 = pkt.addr2
            signal_strength = pkt.dBm_AntSignal  # Signal strength in dBm
            flag = str(pkt.ChannelFlags)
            self.save_packet(addr1, addr2, signal_strength, flag, pkt.len, pkt.reason)

    def Sniffing_Start(self):
        scapy.sniff(prn=self.extract_packets, *self.args, **self.kwargs)

    def save_packet(self, addr1, addr2, signal_strength, channel_flags, packet_length, pktType):
        if addr1 == HARDCODED_ROUTER_MAC:
            router = addr1
            victim = addr2
        else:
            router = addr2
            victim = addr1

        router_info = self.lookup_mac(router)
        victim_info = self.lookup_mac(victim)
        attacks.insert_one({
            'router': router,
            'victim': victim,
            'routerInfo': router_info,
            'victimInfo': victim_info,
            'timestamp': int(time.time()),
            'signalStrength': signal_strength,
            'channelFlags': channel_flags,
            'packetLength': packet_length,
            'type': pktType
        })

        if str([router, victim]) in self.data.keys():
            self.data[str([router, victim])] = self.data[str([router, victim])] + 1
        else:
            self.data[str([router, victim])] = 1

    def lookup_mac(self, mac_address):
        blank = {
            'oui': "UNKNOWN",
            'is_private': "UNKNOWN",
            'company_name': "UNKNOWN",
            'company_address': "UNKNOWN",
            'country_code': "UNKNOWN"
        }

        try:
            mac_info = mac_client.get(mac_address.replace(":", ""))
            return {
                'oui': mac_info.vendor_details.oui,
                'is_private': mac_info.vendor_details.is_private,
                'company_name': mac_info.vendor_details.company_name,
                'company_address': mac_info.vendor_details.company_address,
                'country_code': mac_info.vendor_details.country_code
            }

        except exceptions.EmptyResponseException:
            print('Empty response')
            return blank

        except exceptions.UnparsableResponseException:
            print('Unparsable response')
            return blank

        except exceptions.ServerErrorException:
            print('Internal server error')
            return blank

        except exceptions.UnknownOutputFormatException:
            print('Unknown output')
            return blank

        except exceptions.AuthorizationRequiredException:
            print('Authorization required')
            return blank

        except exceptions.AccessDeniedException:
            print('Access denied')
            return blank

        except exceptions.InvalidMacOrOuiException:
            print('Invalid MAC or OUI')
            return blank

        except exceptions.NotEnoughCreditsException:
            print('Not enough credits')
            return blank

        except Exception:
            print('Unknown error')
            return blank


def main(*args, **kwargs):
    DeauthenticationDetector(*args, **kwargs)
    return

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(f"Started monitoring on {monitor_device}")
        print("Press CTRL+C to exit")
        main(iface=monitor_device)
    else:
        print(f" [ Error ] Please Provide Monitor Mode Interface Name Also \n\n\t:~# sudo {sys.argv[0]} mon0 ")
