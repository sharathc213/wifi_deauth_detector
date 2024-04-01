# WiFi Deauthentication Detection System

## Overview

The WiFi Deauthentication Detection System is a Django-based web application designed to monitor and manage WiFi devices, detect deauthentication events, and provide a user-friendly interface for configuring settings and accessing device information.

![Screenshot1](https://github.com/sharathc213/wifi_deauth_detector/blob/main/Picture1.png)

## Features

- **Monitor Mode Control**: Enable or disable monitor mode for all available WiFi devices.
- **Device List**: View a list of WiFi devices connected to the system and check if monitor mode is enabled.
- **Deauthentication Detection**: Detect and log deauthentication events, saving them to a MongoDB database.
- **Database Configuration**: Configure the database settings through the GUI.
- **MAC Address Lookup API**: Utilize a MAC address lookup API to identify devices.

## Installation

1. Clone the repository:
    ```bash
   git clone https://github.com/yourusername/wifi-deauth-detection.git
   ```

2. Install dependencies:
   ```bash
   cd wifi-deauth-detection
   pip install -r requirements.txt
   cd wifi
   python manage.py runserver
   ```
3. Access the web application at `http://localhost:8000` in your web browser.
   
![Screenshot2](https://github.com/sharathc213/wifi_deauth_detector/blob/main/Picture2.png)

4. Configure the database settings in `settings`.

![Screenshot3](https://github.com/sharathc213/wifi_deauth_detector/blob/main/Picture3.png)

5. select Device tab and enable monitor mode.
   
6. select deauth detector tab and select the device and set the macaddress.io api key(optional).
   
![Screenshot4](https://github.com/sharathc213/wifi_deauth_detector/blob/main/Picture4.png).

7. select dashboard and start the sensor.
   
![Screenshot5](https://github.com/sharathc213/wifi_deauth_detector/blob/main/Picture5.png).

8. if attack is  detected it visualise on the dashboard(refresh is required).

![Screenshot6](https://github.com/sharathc213/wifi_deauth_detector/blob/main/Picture6.png).

## Usage

1. Browse in to the web application.
2. Navigate through the GUI to access different features:
   - Enable/disable monitor mode
   - View connected devices and monitor mode status
   - Configure database settings
   - Access MAC address lookup API
3. Monitor deauthentication events in real-time and view logs in the database.

## Sensor Script

The sensor script (`deauth2.py`) is responsible for scanning deauthentication events. It can be triggered from the UI using subprocesses.

![Screenshotz](https://github.com/sharathc213/wifi_deauth_detector/blob/main/Picture7.png).

## Contributing

Contributions are welcome! Please submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- Developed by [Your Name](https://github.com/sharathc213)

