from Page.add_user_page import AddUserPage
from Page.list_user_page import ListUserPage
from Service.selenium_service import SeleniumService

class AddUserService(SeleniumService):
    
    def add_first_name(self, first_name):
        self.type_on(AddUserPage.first_name, first_name)

    def add_last_name(self, last_name):
        self.type_on(AddUserPage.last_name, last_name)

    def add_user_name(self, user_name):
        self.type_on(AddUserPage.user_name, user_name)

    def add_password(self, password):
        self.type_on(AddUserPage.password, password)  

    def add_customer(self, customer):
        if customer == "Company AAA":
            self.click_on(AddUserPage.customer_aaa)
        elif customer == "Company BBB":
            self.click_on(AddUserPage.customer_bbb)
        else:
            raise Exception("The customer selected isn't available")    
    
    def add_role(self, role):
        self.select_by_visible_text(AddUserPage.role, role)

    def add_email(self, email):
        self.type_on(AddUserPage.email, email)

    def add_cellphone(self, cellphone):
        self.type_on(AddUserPage.cell_phone, cellphone)

    def click_save(self):
        self.click_on(AddUserPage.save)

    def add_user(self, first_name, last_name, user_name, password, customer, role, email, cellphone):
        self.add_first_name(first_name)
        self.add_last_name(last_name)
        self.add_user_name(user_name)
        self.add_password(password)
        self.add_customer(customer)
        self.add_role(role)
        self.add_email(email)
        self.add_cellphone(cellphone)
        self.click_save()