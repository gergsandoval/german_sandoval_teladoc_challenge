from Service.selenium_service import SeleniumService
from Page.list_user_page import ListUserPage
from Entity.list_user import ListUser

class ListUserService(SeleniumService):

    def click_add_user(self):
        self.click_on(ListUserPage.add_user_button)

    def get_user_data(self):
        user_data = []
        rows = self.get_rows(ListUserPage.table_locator)
        for row in rows:
            first_name = self.get_text_inside_row(row, index = 0)
            last_name = self.get_text_inside_row(row, index = 1)
            user_name = self.get_text_inside_row(row, index = 2)
            customer = self.get_text_inside_row(row, index = 4)
            role = self.get_text_inside_row(row, index = 5)
            email = self.get_text_inside_row(row, index = 6)
            cell_phone = self.get_text_inside_row(row, index = 7)
            locked = self.is_checked(row, index = 8)
            user = ListUser(first_name, last_name, user_name, customer, role, email, cell_phone, locked)
            user_data.append(user)
        return user_data
    
    def get_actual_user(self, user_name):
        user_data = self.get_user_data()
        actual_user = next(filter(lambda user : user.user_name == user_name, user_data), "Not Found")
        return actual_user

    def delete_user(self, user_name):
        delete_locator = ListUserPage.create_delete_locator(user_name)
        self.click_on(delete_locator)
        self.confirm_deletion()

    def confirm_deletion(self):
        self.click_on(ListUserPage.confirm_deletion)