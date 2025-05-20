from customer.user_manager import User_manager
from customer.customer_manager import Customer_manager

def main():
    user_manager = User_manager()

    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Ver usuarios")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            user_manager.create_user()

        elif opcion == "2":
            logged_user = user_manager.login()
            if logged_user:
                while True:
                    print("\n*** MENÚ CLIENTE ***")
                    print("1. Crear cliente")
                    print("2. Ver clientes")
                    print("3. Ver datos")
                    print("4. Volver al menú principal")
                    opcion_cliente = input("Elige una opción: ")

                    if opcion_cliente == "1":
                        Customer_manager.create_customer(logged_user)
                    elif opcion_cliente == "2":
                        Customer_manager.list_customers()
                    elif opcion_cliente == "3":
                        customer = Customer_manager.find_by_user(logged_user)
                        if customer:
                            customer.show_contact_info()
                        else:
                            print("No se encontró cliente asociado al usuario logueado.")
                    elif opcion_cliente == "4":
                        break
                    else:
                        print("Opción inválida.")
            else:
                print("No se pudo iniciar sesión.")

        elif opcion == "3":
            user_manager.show_users()

        elif opcion == "4":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()