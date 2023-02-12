from selenium.webdriver.common.by import By

class AddUserPage:
    first_name = (By.NAME, "FirstName")
    last_name = (By.NAME, "LastName")
    user_name = (By.NAME, "UserName")
    password = (By.NAME, "Password")
    customer_aaa = (By.XPATH, "//label[normalize-space()='Company AAA']")
    customer_bbb = (By.XPATH, "//label[normalize-space()='Company BBB']")
    role = (By.NAME, "RoleId")
    email = (By.NAME, "Email")
    cell_phone = (By.NAME, "Mobilephone")
    close = (By.XPATH, "//button[normalize-space()='Close']")
    save = (By.XPATH, "//button[normalize-space()='Save']")
