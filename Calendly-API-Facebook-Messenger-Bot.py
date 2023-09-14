import requests
import time
from datetime import datetime, timedelta
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By




url = 'https://api.calendly.com/scheduled_events'
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR-AUTH-TOKEN"
}


group_chat_url = 'https://www.facebook.com/messages/t/Your-meessenger-group-id'

email = 'your-email'
password = 'your-password'
edge_driver_path = 'your-msedge-driver-path\\msedgedriver.exe'
service = Service(executable_path = edge_driver_path)


edge_options = webdriver.EdgeOptions()
edge_options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" 
edge_options.use_chromium = True 
edge_options.add_argument("disable-infobars")

 # Create the Edge WebDriver instance
driver = webdriver.Edge(service = service, options=edge_options)


driver.get('https://www.facebook.com')
email_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')
email_input.send_keys(email)
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

# Wait login 
time.sleep(6)

driver.get(group_chat_url)
      

# start time to the current date and time
current_time = datetime.now()
start_time = current_time.replace(hour=12, minute=30, second=0, microsecond=0)

# max start time to 23:30 (11:30 PM) 
end_time = current_time.replace(hour=23, minute=30, second=0, microsecond=0)

interval = timedelta(hours=4)

while start_time <= end_time:
    formatted_start_time = start_time.strftime('%Y-%m-%dT%H:%M')

    response = requests.get(url, headers=headers, params={
        'organization': 'https://api.calendly.com/organizations/YOUR-ORG-UUID',
        'min_start_time': formatted_start_time,
        'max_start_time': end_time.strftime('%Y-%m-%dT%H:%M')
    })

    data = json.loads(response.text)

    uris_and_start_times = [(event['uri'], event['start_time']) for event in data['collection']]

    for uri, start_time_str in uris_and_start_times:
        event_start_time = datetime.fromisoformat(start_time_str)

        adjusted_start_time = event_start_time + timedelta(hours=1)

        print(f"Event URI: {uri}")
        print(f"Interview Time: {adjusted_start_time.strftime('%Y-%m-%d %H:%M:%S')}")

        invitees_url = f"{uri}/invitees"

        invitees_response = requests.get(invitees_url, headers=headers)

        invitees_data = json.loads(invitees_response.text)

        for invitee in invitees_data['collection']:
            invitee_name = invitee.get('name', 'No Name Provided')
            invitee_email = invitee.get('email', 'No Email Provided')
            print(f"Invitee Name: {invitee_name}")
            print(f"Invitee Email: {invitee_email}")

           
            time.sleep(10)

            element = driver.find_element(By.XPATH, '//p[@class="xat24cr xdj266r"]')
            element.send_keys("Interview Time: ", adjusted_start_time.strftime('%m-%d %H:%M'),
                  Keys.SHIFT + Keys.ENTER, Keys.SHIFT ,
                  "Invitee Email: ", invitee_email,
                  Keys.SHIFT + Keys.ENTER, Keys.SHIFT ,
                  "Invitee Name: ", invitee_name)

            element.send_keys(Keys.ENTER)
            



    start_time += interval
    time.sleep(10)
    driver.quit()

    # Wait for 4 hours before the next request
    time.sleep(4*60*60) 

    driver = webdriver.Edge(service=service, options=edge_options)
    driver.get('https://www.facebook.com')
    email_input = driver.find_element(By.ID, 'email')
    password_input = driver.find_element(By.ID, 'pass')
    email_input.send_keys(email)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    # Wait login 
    time.sleep(6)
    driver.get(group_chat_url)

# The driver will be quit after the last iterationo 
driver.quit()