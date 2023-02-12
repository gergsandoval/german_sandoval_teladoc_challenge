from selenium.webdriver.common.by import By

class AddUserPage:
    first_name_input = (By.NAME, "FirstName")
    last_name_input = (By.NAME, "LastName")
    user_name_input = (By.NAME, "UserName")
    password_input = (By.NAME, "Password")
    customer_aaa_radio = (By.XPATH, "//label[normalize-space()='Company AAA']")
    customer_bbb_radio = (By.XPATH, "//label[normalize-space()='Company BBB']")
    role_select = (By.NAME, "RoleId")
    email_input = (By.NAME, "Email")
    cell_phone_input = (By.NAME, "Mobilephone")
    close_button = (By.XPATH, "//button[normalize-space()='Close']")
    save_button = (By.XPATH, "//button[normalize-space()='Save']")
