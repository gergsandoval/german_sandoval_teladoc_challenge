from services.selenium_service import SeleniumService
from pages.list_user_page import ListUserPage
from services.table_service import TableService

class ListUserService(SeleniumService):

    def click_add_user(self):
        self.click_on(ListUserPage.add_user_button)
    
    def get_actual_user(self, user_name):
        table_service = TableService(self.context)
        user_data = table_service.get_user_data()
        actual_user = next(filter(lambda user : user.user_name == user_name, user_data), "Not Found")
        return actual_user

