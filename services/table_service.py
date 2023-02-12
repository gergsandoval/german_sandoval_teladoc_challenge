from entities.list_user import ListUser
from services.selenium_service import SeleniumService
from pages.list_user_page import ListUserPage

class TableService(SeleniumService):

    def get_user_data(self):
        user_data = []
        rows = self.get_table_rows(ListUserPage.table_locator)
        for row in rows:
            first_name = self.get_text_inside_row(row, 0)
            last_name = self.get_text_inside_row(row, 1)
            user_name = self.get_text_inside_row(row, 2)
            customer = self.get_text_inside_row(row, 4)
            role = self.get_text_inside_row(row, 5)
            email = self.get_text_inside_row(row, 6)
            cell_phone = self.get_text_inside_row(row, 7)
            locked = self.is_checked(row, 8)
            user = ListUser(first_name, last_name, user_name, customer, role, email, cell_phone, locked)
            user_data.append(user)
        return user_data