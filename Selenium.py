from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os


def LoadCookies():
  chrome_options = Options()
  chrome_options.headless = True
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--incognito')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)

  driver.get(os.getenv("url"))

  elem = driver.find_element(By.ID, "UserName")
  elem.send_keys(os.getenv("username"))
  elem = driver.find_element(By.ID, "Password")
  elem.send_keys(os.getenv("password"))
  elem.send_keys(Keys.RETURN)

  rvft = driver.find_element(
    By.NAME, "__RequestVerificationToken").get_property("value")

  time.sleep(1)

  cookies = driver.get_cookies()
  driver.close()

  return [rvft, cookies]


def ParseCookies(data):
  rvt = ""
  aspnetAppC = ""
  aspnetSID = ""
  vitsecC = ""
  hjSU = ""
  hJFS = ""
  hJS = ""
  hJASIP = ""
  Connected = ""
  AWSALB = ""

  for cookie in data[1]:
    if cookie['name'] == '__RequestVerificationToken':
      rvt = cookie['value']
    elif cookie['name'] == '.AspNet.ApplicationCookie':
      aspnetAppC = cookie['value']
    elif cookie['name'] == 'ASP.NET_SessionId':
      aspnetSID = cookie['value']
    elif cookie['name'] == 'VitSecCookie':
      vitsecC = cookie['value']
    elif cookie['name'] == '_hjSessionUser_2054357':
      hjSU = cookie['value']
    elif cookie['name'] == '_hjFirstSeen':
      hJFS = cookie['value']
    elif cookie['name'] == '_hjSession_2054357':
      hJS = cookie['value']
    elif cookie['name'] == '_hjAbsoluteSessionInProgress':
      hJASIP = cookie['value']
    elif cookie['name'] == 'Connected':
      Connected = cookie['value']
    elif cookie['name'] == 'AWSALB':
      AWSALB = cookie['value']

  cookieString = f"__RequestVerificationToken={rvt}; .AspNet.ApplicationCookie={aspnetAppC}; ASP.NET_SessionId={aspnetSID}; VitSecCookie={vitsecC}; _hjSessionUser_2054357={hjSU}; _hjFirstSeen={hJFS}; _hjSession_2054357={hJS}; _hjAbsoluteSessionInProgress={hJASIP}; Connected={Connected}; AWSALB={AWSALB}; AWSALBCORS={AWSALB}"

  return [data[0], cookieString]


print(ParseCookies(LoadCookies()))
