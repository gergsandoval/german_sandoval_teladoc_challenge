from selenium.webdriver.common.by import By

class DeleteUserPage:

    delete_locator_begin = '//td[normalize-space()='
    delete_locator_end = ']/../td[position() = last()]/button'
    confirm_deletion_button = (By.XPATH, "//button[normalize-space()='OK']")

    @staticmethod
    def create_delete_locator(user_name):
        xpath = f"{DeleteUserPage.delete_locator_begin}{user_name}{DeleteUserPage.delete_locator_end}"
        return (By.XPATH, xpath)