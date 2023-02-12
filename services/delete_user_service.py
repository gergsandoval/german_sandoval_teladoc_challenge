from services.selenium_service import SeleniumService
from pages.delete_user_page import DeleteUserPage

class DeleteUserService(SeleniumService):

    def delete_user(self, user_name):
        delete_locator = DeleteUserPage.create_delete_locator(user_name)
        self.click_on(delete_locator)
        self.confirm_deletion()

    def confirm_deletion(self):
        self.click_on(DeleteUserPage.confirm_deletion_button)