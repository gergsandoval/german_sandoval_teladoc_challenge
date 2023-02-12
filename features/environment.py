from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def before_all(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()

def after_all(context):
    context.driver.quit()
