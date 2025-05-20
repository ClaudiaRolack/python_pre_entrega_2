class User_manager:

    def __init__(self):
        self.users = {}
    
    def create_user(self):
        user = input("Escribe el nombre de tu usuario: ")
        password = input("Escribe tu contraseña: ")

        if user in self.users:
            print("Este usuario ya existe.")
        else:
            self.users[user] = password
            print(f"Usuario {user} creado exitosamente.")

    def login(self):
        user = input("Usuario: ")
        password = input("Contraseña: ")

        if user in self.users and self.users[user] == password:
            print(f"¡Bienvenido {user}!")
            return user
        else:
            print("Usuario o contraseña incorrectos.")
            return None
        
    def show_users(self):
        if not self.users:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados: ")
            for user, password in self.users.items():
                print(f"Usuario: {user} - Contraseña: {password}")