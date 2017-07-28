import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def lambda_handler(event, context):
  driver = webdriver.Chrome()
  driver.implicitly_wait(30)
  wait = WebDriverWait(driver, 20)
  driver.maximize_window()

  driver.get('https://www.smbc-card.com/mem/index.jsp')

  wait.until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, '#contWrap > div.ktop_infoAreaWrap > div > ul.ktop_infoBox.line.valignTop > li > div.loginInfoBox > form > ul > li:nth-child(1) > input[type="text"]'))
      )
  driver.find_element_by_css_selector('#contWrap > div.ktop_infoAreaWrap > div > ul.ktop_infoBox.line.valignTop > li > div.loginInfoBox > form > ul > li:nth-child(1) > input[type="text"]').send_keys(os.environ['VPASS_USER_ID'])
  driver.find_element_by_css_selector('#contWrap > div.ktop_infoAreaWrap > div > ul.ktop_infoBox.line.valignTop > li > div.loginInfoBox > form > ul > li:nth-child(2) > input[type="password"]').send_keys(os.environ['VPASS_PASSWORD'])
  driver.find_element_by_css_selector('#contWrap > div.ktop_infoAreaWrap > div > ul.ktop_infoBox.line.valignTop > li > div.loginInfoBox > form > p > input').click()
  wait.until(
          EC.visibility_of_element_located((By.CSS_SELECTOR, ".sideMenu01 > li:nth-child(2) > a:nth-child(1)"))
      )
  driver.get('https://www.smbc-card.com/memx/authori/shokai/index.html')
  wait.until(
          EC.presence_of_element_located((By.CSS_SELECTOR, "#vp-view-VC8403-001_RS0001_cvv2"))
      )

  driver.find_element_by_css_selector('#vp-view-VC8403-001_RS0001_month').send_keys(os.environ['VPASS_CARD_EXPIRE_MONTH'])
  driver.find_element_by_css_selector('#vp-view-VC8403-001_RS0001_year').send_keys(os.environ['VPASS_CARD_EXPIRE_YEAR'])
  driver.find_element_by_css_selector('#vp-view-VC8403-001_RS0001_cvv2').send_keys(os.environ['VPASS_SECURITY_CODE'])
  driver.find_element_by_css_selector('#vp-view-VC8403-001_RS0001_GMVC8403001C300001-btn01').submit()

  wait.until(
          EC.presence_of_element_located((By.CSS_SELECTOR, '#vp_alcor_view_Label_173'))
      )

  value = driver.find_element_by_css_selector('#vp_alcor_view_Label_173').text

  logout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#sideVpassLogoutBtn')))
  time.sleep(1) # Maybe we need it to wait for changing opacity to 0.
  logout_button.click()
  driver.quit()

  return value