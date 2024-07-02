import csv
from dotenv import load_dotenv
import os
import re
from datetime import datetime, timedelta
from colorama import Fore
from openpyxl import Workbook

from utils import *
from data_processing import *

def main():
    """
    Función principal del programa. 
    Carga los datos de los usuarios desde un archivo CSV, permite al usuario seleccionar un usuario y un rango de fechas,
    y filtra y muestra los datos correspondientes. También permite exportar los datos filtrados a un archivo Excel.
    """

    load_dotenv()

    reg_user = r'^[1-9]|^\d+(,\d+)?E[+-]?\d+$'
    users = []
    user_index_mapping = {}
    box_width = 36

    file_path = os.getenv('csv_file_route')

    while True:
        with open(file_path, newline='') as data:
            data_red = csv.reader(data, delimiter=',')  # Contiene los datos de la tabla de usuarios

            color_w = Fore.WHITE
            index = 1
            users.clear()
            user_index_mapping.clear()

            menu()

            for row in data_red:
                if row[3] != 'Usuario' and row[3].lower() not in users and row[3] != 'invitado-deca' and not re.match(reg_user, row[3]):
                    user_name = row[3].lower()
                    users.append(user_name)
                    user_index_mapping[index] = user_name
                    print(color_w + f"{index}. {row[3]}")
                    index += 1

            print(color_w + f"\n+{'-' * (box_width - 2)}+")

            color = Fore.CYAN
            color_good = Fore.GREEN
            color_bad = Fore.RED

            while True:
                user_index = int(input(color + "Seleccione un usuario con el número de índice: "))
                if user_index in user_index_mapping:
                    selected_user = user_index_mapping[user_index]
                    print(color_good + f"Usuario seleccionado: {selected_user}")
                    break
                else:
                    print(color_bad + "Índice seleccionado no válido. Intente nuevamente.")

        date_in = input(color + "Por favor ingrese la fecha de inicio del rango (dd-mm-aaaa): ")
        date_out = input(color + "Por favor ingrese la fecha del fin del rango (dd-mm-aaaa): ")
        print(color_w + f"+{'-' * (box_width - 2)}+")

        while True:
            try:
                validate_date(date_in, date_out)
                break
            except ExceptionDate as e:
                print(e)
                date_in = input(color + "Por favor ingrese la fecha de inicio del rango (dd-mm-aaaa): ")
                date_out = input(color + "Por favor ingrese la fecha del fin del rango (dd-mm-aaaa): ")

        dates = dates_range(date_in, date_out)

        with open(file_path, newline='') as data:
            data_red = csv.reader(data, delimiter=',')  # Contiene los datos de la tabla de usuarios
            lila, state = get_user_data(data_red, selected_user)

        if not state:
            input("Presione [ENTER] para continuar...")
            continue  # Volver al menú si no hay fecha de fin

        pipa = filter_user_data(lila, dates)

        color = Fore.YELLOW
        color_title = Fore.LIGHTMAGENTA_EX


        if len(pipa) == 0:
            print(Fore.WHITE + "El usuario no tuvo sesiones activas en las instalaciones en el rango seleccionado")
        else:
            print(color + "\n==================================== DATOS ====================================")
            print(Fore.RESET)
            print(color_title + f"{'Usuario':<20}{'Fecha Conexión Inicio':<25}{'Hora Inicio':<15}{'Fecha Conexión Fin':<25}{'Hora Fin':<15}{'MAC AP':<15}")
            print(Fore.RESET)
            for row in pipa:
                print(f"{row[0]:<20}{row[1]:<25}{row[2]:<15}{row[3]:<25}{row[4]:<15}{row[5]:<15}")

        while True:
            print(Fore.YELLOW +"\n¿Qué le gustaría hacer a continuación?")
            print(Fore.YELLOW +"1. Guardar los datos en un archivo Excel")
            print(Fore.YELLOW +"2. Buscar otro usuario")
            print(Fore.YELLOW +"3. Buscar otro rango de fechas")
            print(Fore.YELLOW +"4. Salir")
            choice = input("Seleccione una opción: ")

            if choice == '1':
                wb = Workbook()
                ws = wb.active
                ws.append(['Usuario', 'Fecha Conexión Inicio', 'Hora Inicio', 'Fecha Conexión Fin', 'Hora Fin', 'MAC AP'])

                for row in pipa:
                    ws.append(row)

                excel_file_path = 'filtered_data.xlsx'
                wb.save(excel_file_path)
                print(Fore.GREEN + f"\nDatos filtrados exportados exitosamente a '{excel_file_path}'")
            elif choice == '2':
                break  # Rompe el bucle interno y vuelve al inicio del bucle principal para seleccionar otro usuario
            elif choice == '3':
                while True:
                    date_in = input(Fore.CYAN + "Por favor ingrese la fecha de inicio del rango (dd-mm-aaaa): ")
                    date_out = input(Fore.CYAN + "Por favor ingrese la fecha del fin del rango (dd-mm-aaaa): ")
                    print(color_w + f"+{'-' * (box_width - 2)}+")
                    try:
                        validate_date(date_in, date_out)
                        break
                    except ExceptionDate as e:
                        print(e)
                
                dates = dates_range(date_in, date_out)
                with open(file_path, newline='') as data:
                    data_red = csv.reader(data, delimiter=',')
                    lila = get_user_data(data_red, selected_user)

                pipa = filter_user_data(lila, dates)
                color = Fore.YELLOW
                color_title = Fore.LIGHTMAGENTA_EX

                if len(pipa) == 0:
                    print("El usuario no tuvo sesiones activas en las instalaciones en el rango seleccionado")
                else:
                    print(color + "\n==================================== DATOS ====================================")
                    print(Fore.RESET)
                    print(color_title + f"{'Usuario':<20}{'Fecha Conexión Inicio':<25}{'Hora Inicio':<15}{'Fecha Conexión Fin':<25}{'Hora Fin':<15}{'MAC AP':<15}")
                    print(Fore.RESET)
                    for row in pipa:
                        print(f"{row[0]:<20}{row[1]:<25}{row[2]:<15}{row[3]:<25}{row[4]:<15}{row[5]:<15}")
            elif choice == '4':
                print(Fore.WHITE + "Saliendo...")
                return 
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
