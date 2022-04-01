from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import keys
##https://www.seleniumeasy.com/ website for run test automation

driver = webdriver.Chrome('/Users/asimsaeed/Downloads/chromedriver')

driver.get('https://websitedownloader.io/')
driver.implicitly_wait(3)
elementBTn = driver.find_element_by_id('startDownloadButton-0')
elementBTn.click()
 
# WebDriverWait(driver , 30).until(
#     EC.text_to_be_present_in_element(
#         (By.ID , 'startDownloadUrlInput-0-helper-text', 'This field is required')
#     )
# )

elementWarn  =  driver.find_element_by_id('startDownloadUrlInput-0-helper-text') ##Validation error message
print(f'WARN ELEMENT===>>>>>{elementWarn.text}')

if (elementWarn.text  == 'This field is required'):
    elementInputField  =  driver.find_element_by_id('startDownloadUrlInput-0')
    elementInputField.send_keys('www.google.com')
    elementBTn.click() #Click button
    closeBTN =  driver.find_element_by_id('closeSettingsButton')
    closeBTN.click()
    downloadBTN  =  driver.find_element_by_id('downloadZipButton')
    downloadBTN.click()
    loginBtn  =  driver.find_element_by_id('subscriptionDialogLoginButton')
    loginBtn.click()


