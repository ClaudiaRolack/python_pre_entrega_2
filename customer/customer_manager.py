class Customer_manager:
    customers = []  

    def __init__(self, name, email, address, phone_number, user):
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.user = user
        Customer_manager.customers.append(self)

    def __str__(self):
        return f"Cliente: {self.name} - Email: {self.email}"

    def show_contact_info(self):
        print(f"{self.name} - Tel: {self.phone_number} | Dirección: {self.address}")

    @classmethod
    def create_customer(cls, user):
        name = input("Nombre: ")
        email = input("Email: ")
        address = input("Dirección: ")
        phone = input("Teléfono: ")

        new_customer = cls(name, email, address, phone, user)
        cls.customers.append(new_customer)
        print(f"Cliente'{name}' creado y asociado al usuario '{user}'")
   


    @classmethod
    def list_customers(cls):
        if not cls.customers:
            print("No hay clientes registrados.")
        else:
            for customer in cls.customers:
                print(customer)

    @classmethod
    def find_by_user(cls, username):
        for customer in cls.customers:
         if customer.user == username:
                return customer
        return None