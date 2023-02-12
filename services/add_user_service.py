from pages.add_user_page import AddUserPage
from pages.list_user_page import ListUserPage
from services.selenium_service import SeleniumService

class AddUserService(SeleniumService):
    
    def add_first_name(self, first_name):
        self.type_on(AddUserPage.first_name_input, first_name)

    def add_last_name(self, last_name):
        self.type_on(AddUserPage.last_name_input, last_name)

    def add_user_name(self, user_name):
        self.type_on(AddUserPage.user_name_input, user_name)

    def add_password(self, password):
        self.type_on(AddUserPage.password_input, password)  

    def select_customer(self, customer):
        if customer == "Company AAA":
            self.click_on(AddUserPage.customer_aaa_radio)
        elif customer == "Company BBB":
            self.click_on(AddUserPage.customer_bbb_radio)
        else:
            raise Exception(f"The customer {customer} isn't available")    
    
    def add_role(self, role):
        self.select_by_visible_text(AddUserPage.role_select, role)

    def add_email(self, email):
        self.type_on(AddUserPage.email_input, email)

    def add_cell_phone(self, cell_phone):
        self.type_on(AddUserPage.cell_phone_input, cell_phone)

    def click_save(self):
        self.click_on(AddUserPage.save_button)

    def add_user(self, first_name, last_name, user_name, password, customer, role, email, cell_phone):
        self.add_first_name(first_name)
        self.add_last_name(last_name)
        self.add_user_name(user_name)
        self.add_password(password)
        self.select_customer(customer)
        self.add_role(role)
        self.add_email(email)
        self.add_cell_phone(cell_phone)
        self.click_save()