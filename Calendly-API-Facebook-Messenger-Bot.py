import requests
import time
import json
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Configuration Constants
CALENDLY_API_URL = "https://api.calendly.com/scheduled_events"
ORG_UUID = "YOUR-ORG-UUID"
FACEBOOK_GROUP_CHAT_URL = "https://www.facebook.com/messages/t/Your-messenger-group-id"
EMAIL = "your-email"
PASSWORD = "your-password"
EDGE_DRIVER_PATH = "your-msedge-driver-path\\msedgedriver.exe"
EDGE_BINARY_LOCATION = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# Initialize Edge WebDriver
service = Service(executable_path=EDGE_DRIVER_PATH)
edge_options = webdriver.EdgeOptions()
edge_options.binary_location = EDGE_BINARY_LOCATION
edge_options.use_chromium = True
edge_options.add_argument("disable-infobars")
driver = webdriver.Edge(service=service, options=edge_options)

# Login to Facebook
driver.get("https://www.facebook.com")
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "pass")
email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)
time.sleep(6)

# Define time intervals for Calendly event fetching
current_time = datetime.now()
start_time = current_time
end_time = current_time.replace(hour=21, minute=59, second=0, microsecond=0)
interval = timedelta(hours=4)

# Loop to fetch Calendly events
while start_time <= end_time:
    formatted_start_time = start_time.strftime("%Y-%m-%dT%H:%M")

    # Fetch Calendly events
    response = requests.get(
        CALENDLY_API_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR-AUTH-TOKEN",
        },
        params={
            "organization": f"https://api.calendly.com/organizations/{ORG_UUID}",
            "min_start_time": formatted_start_time,
            "max_start_time": end_time.strftime("%Y-%m-%dT%H:%M"),
        },
    )
    data = json.loads(response.text)

    uris_and_start_times = [
        (event["uri"], event["start_time"]) for event in data["collection"]
    ]

    for uri, start_time_str in uris_and_start_times:
        event_start_time = datetime.fromisoformat(start_time_str)
        adjusted_start_time = event_start_time + timedelta(hours=1)
        invitees_url = f"{uri}/invitees"
        invitees_response = requests.get(invitees_url, headers=headers)
        invitees_data = json.loads(invitees_response.text)

        # Print and send Facebook messages
        for invitee in invitees_data["collection"]:
            invitee_name = invitee.get("name", "No Name Provided")
            invitee_email = invitee.get("email", "No Email Provided")
            print(f"Event URI: {uri}")
            print(f"Interview Time: {adjusted_start_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Invitee Name: {invitee_name}")
            print(f"Invitee Email: {invitee_email}")
            time.sleep(10)

            element = driver.find_element(By.XPATH, '//p[@class="xat24cr xdj266r"]')
            element.send_keys(
                "Interview Time: ",
                adjusted_start_time.strftime("%m-%d %H:%M"),
                Keys.SHIFT + Keys.ENTER,Keys.SHIFT,
                "Invitee Email: ",
                invitee_email,
                Keys.SHIFT + Keys.ENTER,Keys.SHIFT,
                "Invitee Name: ",
                invitee_name,
            )
            element.send_keys(Keys.ENTER)

    start_time += interval

    # Wait for 4 hours before the next request
    time.sleep(4 * 60 * 60)

# Quit the driver after the last iteration
driver.quit()
