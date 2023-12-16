from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string
import requests

def ask_question(question, lower):
    print(question)
    response = input()
    if lower:
        return response.lower()
    else:
        return response

used_usernames = []
used_passwords = []
Register_url = "https://discord.com/register"
months = ['december', 'januar', 'februar', 'marts', 'April', 'May', 'juni', 'juli', 'august', 'september', 'oktober', 'november']

inv = ask_question("Please input the invite you would like to use if you already have every account invited then leave this blank:", False)
channel_id = ask_question("Please enter the channel ID you would like to spam:", False)
Message = ask_question("Please input the message you would like the Selfbot to spam:", True)

def generate_username(length=6):
    # generate a random username
    username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    
    # check if the username has been used before
    while username in used_usernames:
        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    
    # add the new username to the list of used usernames
    used_usernames.append(username)
    
    return username

def generate_password(length=32):
    # define the pool of characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # generate a password
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    for _ in range(length - 4):  # subtract 4 because we already have 4 characters
        password.append(random.choice(characters))
    random.shuffle(password)
    password = ''.join(password)

    # check if the password has been used before
    while password in used_passwords:
        password = generate_password(length)

    # add the new password to the list of used passwords
    used_passwords.append(password)

    return password



def account_generator():
    date = random.randint(1970, 2002)
    print(date)
    selection_month = random.choice(months)
    print(selection_month)
    selection_day = random.randint(1,28)
    print(selection_day)
    

    email = ask_question("Please input the email you would like to use this email must have support for eg: Example+1@example.com I would recommend Gmail", False)
    # create a new Chrome browser instance
    browser = webdriver.Chrome()
    # navigate to the webpage
    browser.get('https://discord.com/register')

    # create a WebDriverWait instance
    wait = WebDriverWait(browser, 10)  # wait up to 10 seconds

    # locate the elements
    email_field = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
    username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    Display_name = wait.until(EC.presence_of_element_located((By.NAME, 'global_name')))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    register_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/div[7]/button')))
    terms_of_service_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/div[8]/label/input')))
    enter_month = browser.find_element(By.ID, "react-select-3-input")
    enter_day = browser.find_element(By.ID, "react-select-2-input")
    enter_year = browser.find_element(By.ID, "react-select-4-input")

    email_field.send_keys(email)
    username = generate_username()
    print(username)
    username_field.send_keys(username)
    Display_name.send_keys(username)
    pwd = generate_password()
    print(pwd)
    password_field.send_keys(pwd)
    enter_day.send_keys(selection_day, Keys.ENTER)
    enter_month.send_keys(selection_month, Keys.ENTER)
    enter_year.send_keys(date, Keys.ENTER)
    terms_of_service_checkbox.click()
    register_button.click()
    while True:
        if browser.current_url != "https://discord.com/register":
            time.sleep(10)
            token = browser.execute_script('return window.localStorage.token')
            print(token)
            return token
account_generator()
tokens = [""]

dc_tokens = ', '.join(tokens)
dc_tokens = '"' + dc_tokens + '"'
dc_tokens = dc_tokens.replace('"', '')
dc_tokens = dc_tokens.replace('.', '')

def api_msg():
    for token in tokens:
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }

        payload = {
            "content": Message,
            "tts": True,
        }

        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)

        if response.status_code == 200:
            print(f"Message sent using token {token}")
        else:
            print(f"Failed to send message using token {token}. Response: {response.text}")

while True:
    api_msg()
    time.sleep(0.55)
