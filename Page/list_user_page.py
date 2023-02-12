from selenium.webdriver.common.by import By

class ListUserPage:
    add_user_button = (By.CSS_SELECTOR, "button[type='add']")
    table_locator = (By.TAG_NAME, 'table')
    delete_locator_begin = '//td[normalize-space()='
    delete_locator_end = ']/../td[position() = last()]/button'
    confirm_deletion = (By.XPATH, "//button[normalize-space()='OK']")

    @staticmethod
    def create_delete_locator(user_name):
        xpath = f"{ListUserPage.delete_locator_begin}{user_name}{ListUserPage.delete_locator_end}"
        return (By.XPATH, xpath)