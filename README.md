# WiFi Deauthentication Detection System

## Overview

The WiFi Deauthentication Detection System is a Django-based web application designed to monitor and manage WiFi devices, detect deauthentication events, and provide a user-friendly interface for configuring settings and accessing device information.

![Screenshot](/path/to/screenshot.png)

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
   
4. Configure the database settings in `settings`.
5. select Device tab and enable monitor mode,
6. select deauth detector tab and select the device and set the macaddress.io api key(optional).
7. select dashboard and start the sensor.
8. if attack is  detected it visualise on the dashboard(refresh is required).


## Usage

1. Log in to the web application using your credentials.
2. Navigate through the GUI to access different features:
   - Enable/disable monitor mode
   - View connected devices and monitor mode status
   - Configure database settings
   - Access MAC address lookup API
3. Monitor deauthentication events in real-time and view logs in the database.

## Sensor Script

The sensor script (`deauth2.py`) is responsible for scanning deauthentication events. It can be triggered from the UI using subprocesses.


## Contributing

Contributions are welcome! Please follow the guidelines in `CONTRIBUTING.md` before submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- Developed by [Your Name](https://github.com/yourusername)

## Acknowledgements

- Special thanks to [Name] for inspiration and guidance.

---

Replace placeholders such as `/path/to/screenshot.png`, `yourusername`, `Name`, etc., with relevant information specific to your project. Make sure to include any additional sections or details that you think are important for users and contributors to know.

Once you've filled in all the necessary information, save the file as `README.md` in the root directory of your project. This README will serve as a comprehensive guide for anyone interested in using or contributing to your WiFi deauthentication detection system.
