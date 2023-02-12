from selenium.webdriver.common.by import By

class ListUserPage:
    add_user_button = (By.CSS_SELECTOR, "button[type='add']")
    table_locator = (By.TAG_NAME, 'table')
