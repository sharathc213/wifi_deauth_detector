import collections
from django.http import HttpResponse
from django.shortcuts import render
from bson.json_util import dumps
import json
from django.http import JsonResponse
from django.template.loader import get_template
from django.template import Context, Template,loader
import os
from pymongo import MongoClient
import pymongo
import time
import subprocess
import datetime

import netifaces



import pcapy
import sys
import os
import datetime
import deauth2
import psutil
import signal


def Detector(request):
   return render(request,'Detector.html')

def getdetector(request):
   
   f = open ('setup.json', "r")
   data = json.loads(f.read())
   f.close()
   content={'adapter':data['wifi']['deauther_detector']['adapter_name_before']}

   
   api=data['wifi']['deauther_detector']['sensor_pid']
   adapter=data['wifi']['deauther_detector']['adapter_name_before']
   database=data['wifi']['database']



# MongoDB Setup
   client = MongoClient(database)
   db = client['deauth_attacks']
   attacksCollection = db['attacks']
   # lastAttackCollection = db['lastAttack']

        
       
   content["data"]= dumps(attacksCollection.find())
   content["data2"]  =json.loads(dumps(attacksCollection.find()))  
   content["data3"]=[0,0,0,0,0,0,0,0,0,0,0,0]
   for d in content["data2"]:
      p=d['timestamp']
      n=datetime.date.fromtimestamp(int(p))
      # print(n.month-1)
      content["data3"][n.month-1] = content["data3"][n.month-1]+1
      # print(content["data3"][n.month]+1)
      # content["data3"][n.month-1]=content["data3"][n.month]+1
      t = datetime.datetime.fromtimestamp(int(p))
      d['date']=datetime.datetime.fromtimestamp(int(p))

   template = loader.get_template('detector_data.html')
   # print(content["data3"])
  
   return HttpResponse(template.render(content, request))
   # return render(request,'m.html',content)


def getinterface(request):
   if request.method == 'POST':
      alldevice=netifaces.interfaces()
      return JsonResponse({"data":alldevice})
def settings(request):
   return render(request,'settings.html')

def getsettings(request):
   flag=False
   template = loader.get_template('settings_data.html')
   f = open ('setup.json', "r")
   data = json.loads(f.read())
   f.close()
   alldevice=netifaces.interfaces()
   wifi_device=[]
   wifi_device_after=[]
   wifi_device_with_mon=[]
   adapter_name_after=data['wifi']['deauther_detector']['adapter_name_before']
   for c in alldevice:
      result=subprocess.run(["iwconfig", c],capture_output=True,text=True)
      if result.stdout:
         is_mon_1=subprocess.run(["iwconfig", c],capture_output=True,text=True)
         if is_mon_1.stdout.find("Monitor") != -1:
            flag=True
         os.system("ifconfig " + c + " down")
         os.system("iwconfig " + c + " mode monitor")
         os.system("ifconfig " + c + " up")
         is_mon=subprocess.run(["iwconfig", c],capture_output=True,text=True)
         print(is_mon)
         if is_mon.stdout.find("Monitor") != -1:
            if not flag:
               os.system("ifconfig " + c + " down")
               os.system("iwconfig " + c + " mode managed")
               os.system("ifconfig " + c + " up")
               wifi_device.append({"name":c,"support":True,"status":False})
            else:
               wifi_device.append({"name":c,"support":True,"status":True})
            flag=False
         else:
            wifi_device.append({"name":c,"support":False,"status":False})
   
   for c in alldevice:
      result=subprocess.run(["iwconfig", c],capture_output=True,text=True)
      if result.stdout:
         is_mon=subprocess.run(["iwconfig", c],capture_output=True,text=True)
         if is_mon.stdout.find("Monitor") != -1:
            wifi_device_with_mon.append({"name":c,"support":True,"status":True})
         else:
            wifi_device_with_mon.append({"name":c,"support":False,"status":False})
  

   

   content={'database':data['wifi']['database'],'alldevice':wifi_device,'wifi_device_with_mon':wifi_device_with_mon,'api':data['wifi']['deauther_detector']['api']}
   print(str(template))
  
   return HttpResponse(template.render(content, request))


   
   
def saveDatabase(request):
   if request.method == 'POST':
      database_link=request.POST.get('database_link')
      f = open ('setup.json', "r")
      data = json.loads(f.read())
      f.close()

      data['wifi']['database']=database_link
      f = open ('setup.json', "w")
      json.dump(data,f)
      f.close()
      return JsonResponse({"database_link":database_link,"error":False,"msg":"success"})


def resetDatabase(request):
   if request.method == 'POST':
      f = open ('setup.json', "r")
      data = json.loads(f.read())
      f.close()

      database_link=data['wifi']['database']
     
      
      try:
         client = MongoClient(database_link)
         client.server_info()
         client.drop_database('deauth_attacks')
         return JsonResponse({"database_link":database_link,"error":False,"msg":"Sucess"})
      except pymongo.errors.ServerSelectionTimeoutError:
         return JsonResponse({"database_link":database_link,"error":True,"msg":"Database Not Connected"})
      
      

def enablemon(request):
   if request.method == 'POST':
      interface=request.POST.get('interface')
      os.system("ifconfig " + interface + " down")
      os.system("iwconfig " + interface + " mode monitor")
      os.system("ifconfig " + interface + " up")

      alldevice=netifaces.interfaces()
      wifi_device=[]
      wifi_device_after=[]
      for c in alldevice:
         result=subprocess.run(["iwconfig", c],capture_output=True,text=True)
         if result.stdout:
            is_mon=subprocess.run(["iwconfig", c ],capture_output=True,text=True)
            if is_mon.stdout.find("Monitor") != -1:
               wifi_device.append({"name":c,"support":True,"status":True})
            else:
               wifi_device.append({"name":c,"support":False,"status":False})
      return JsonResponse({"mon_enb_dev":wifi_device})

def diseablemon(request):
   if request.method == 'POST':
      interface=request.POST.get('interface')
      os.system("ifconfig " + interface + " down")
      os.system("iwconfig " + interface + " mode managed")
      os.system("ifconfig " + interface + " up")
      alldevice=netifaces.interfaces()
      wifi_device=[]
      wifi_device_after=[]
      for c in alldevice:
         result=subprocess.run(["iwconfig", c],capture_output=True,text=True)
         if result.stdout:
            is_mon=subprocess.run(["iwconfig", c ],capture_output=True,text=True)
            if is_mon.stdout.find("Monitor") != -1:
               wifi_device.append({"name":c,"support":True,"status":True})
            else:
               wifi_device.append({"name":c,"support":False,"status":False})
      return JsonResponse({"mon_enb_dev":wifi_device})

def saveDetector(request):
   if request.method == 'POST':
      api=request.POST.get('api')
      adapter_withmon=request.POST.get('adapter_withmon')
    
      f = open ('setup.json', "r")
      data = json.loads(f.read())
      f.close()
      
      if api!="" and api!=None:

         data['wifi']['deauther_detector']['api']=api
      if adapter_withmon!="" and adapter_withmon!=None:

         data['wifi']['deauther_detector']['adapter_name_before']=adapter_withmon
      f = open ('setup.json', "w")
      json.dump(data,f)
      f.close()
      return JsonResponse({"api":data['wifi']['deauther_detector']['api'],"err":False,"msg":"Success"})

def start_deauth_detector(request):
   if request.method == 'POST':
      adapter=request.POST.get('adapter')
      f = open ('setup.json', "r")
      data = json.loads(f.read())
      f.close()
      alldevice=netifaces.interfaces()
      wifi_device=[]
      for c in alldevice:
         result=subprocess.run(["iwconfig", c],capture_output=True,text=True)
         if result.stdout:
            wifi_device.append(c)
      for a in wifi_device:
         if a==adapter:
            is_mon=subprocess.run(["iwconfig", adapter],capture_output=True,text=True)
            if is_mon.stdout.find("Monitor") != -1:
               

               p = subprocess.Popen(['python3','deauth2.py'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

               data['wifi']['deauther_detector']['sensor_pid']=p.pid
               f = open ('setup.json', "w")
               json.dump(data,f)
               f.close()
               return JsonResponse({"message":"Detector Started","err":False})
            else:
               return JsonResponse({"message":"Please Enable Monitor Mode","err":True})
         else:
            return JsonResponse({"message":"This Device is not Detected","err":True})
      if len(wifi_device)==0:
         return JsonResponse({"message":"This Device is not Detected","err":True})

      

def stop_deauth_detector(request):
   if request.method == 'POST':
      f = open ('setup.json', "r")
      data = json.loads(f.read())
      f.close()
      pid=data['wifi']['deauther_detector']['sensor_pid']
      if psutil.pid_exists(pid):
         if pid < 0:
            return JsonResponse({"message":"Incorrect PIP","err":True})
            
         if pid == 0:
            
            return JsonResponse({"message":"pid cannot be 0","err":True})
         try:
            os.kill(int(pid), signal.SIGKILL)
            # os.system("kill -s SIGCHLD "+str(pid))
            time.sleep(5)
         except OSError as err:
            if err.errno == errno.ESRCH:
                  return JsonResponse({"message":"No such Process","err":True})
            elif err.errno == errno.EPERM:
                  return JsonResponse({"message":"Permission Denied","err":True})
            else:
                 return JsonResponse({"message":"something error","err":True})
         else:
            return JsonResponse({"message":"Detector Stoped","err":False})

         
      else:
         return JsonResponse({"message":"This PID Does not exist","err":True})



def getsensorbutton(request):
   
   f = open ('setup.json', "r")
   data = json.loads(f.read())
   f.close()
   pid=data['wifi']['deauther_detector']['sensor_pid']
   # time.sleep(5)
   result=subprocess.run(["ps","-aux","|","egrep" ,"'defunct'"],capture_output=True,text=True)
   print(result.stdout)
   content={'adapter':data['wifi']['deauther_detector']['adapter_name_before']}
   if psutil.pid_exists(pid):
      content["sensor"]=True
      print("running")
   else:
      content["sensor"]=False
   
   
   api=data['wifi']['deauther_detector']['sensor_pid']
   adapter=data['wifi']['deauther_detector']['adapter_name_before']
   database=data['wifi']['database']

  

   template = loader.get_template('SensorButton.html')
  
   return HttpResponse(template.render(content, request))
      
