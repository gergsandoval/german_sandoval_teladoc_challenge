class ListUser:
    
    def __init__(self, first_name, last_name, user_name, customer, role, email, cell_phone, locked):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.customer = customer
        self.role = role
        self.email = email
        self.cell_phone = cell_phone
        self.locked = locked

    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__
    