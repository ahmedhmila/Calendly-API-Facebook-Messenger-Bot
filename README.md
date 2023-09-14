# Calendly-API-Facebook-Messenger-Bot
Automate sending messages to a Facebook Messenger group chat based on scheduled events from Calendly. Keep your team or friends informed about upcoming events without manual intervention.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Introduction

The Calendly-API-Facebook-Messenger-Bot is a Python script that leverages the Calendly API to fetch scheduled events and send automated messages to a specified Facebook Messenger group chat. It's designed to streamline communication by providing event details, including interview times, invitee names, and emails, directly to your team or group chat.

## Features

- **Integration with Calendly:** Fetches scheduled events and their details from the Calendly API.
- **Automated Messaging:** Sends messages with event information to a Facebook Messenger group chat.
- **Customizable Interval:** Define how often the script runs to send updates to the group chat.
- **User-Friendly:** Uses Selenium to log in to Facebook and send messages, making it easy to set up and use.

## Installation

### Prerequisites

- Python 3.x
- `requests` library
- `selenium` library
- Webdriver for your browser (e.g., Microsoft Edge)

### Steps

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/facebook-messenger-auto-bot.git
   ```

2. Install the required Python libraries using pip:
   ```
   pip install requests selenium
   ```

3. Download and install the WebDriver for your browser (e.g., Microsoft Edge). Make sure to set the path correctly in the script (variable `edge_driver_path`).

## Usage

1. Run the script:
   ```
   python auto_bot.py
   ```

2. Log in to your Facebook account when prompted by the script.

3. Provide the group chat URL where you want to send messages.

4. The script will periodically fetch event details from Calendly and send messages to the group chat.

## Contributing

Feel free to fork the project and submit pull requests for enhancements, bug fixes, or new features. Your contributions are welcome and can help make this project even more powerful!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- Project Creator: Ahmed Hmila
- Project Link: [https://github.com/ahmedhmila/Calendly-API-Facebook-Messenger-Bot](https://github.com/ahmedhmila/Calendly-API-Facebook-Messenger-Bot)

- 📧 **Email:** [ahmedhmiladev@gmail.com](mailto:ahmedhmiladev@gmail.com)
- 💼 **LinkedIn:** [Let's connect on LinkedIn!](https://www.linkedin.com/in/ahmed-hmila/)
---
