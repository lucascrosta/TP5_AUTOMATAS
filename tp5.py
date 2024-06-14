import csv
from dotenv import load_dotenv
import os
import re
from datetime import datetime, date, timedelta
from colorama import Fore, init

class ExceptionDate(Exception):
    pass

def menu():
    color = Fore.CYAN
    print("")
    print(color + "----------------BIENVENIDOS----------------")
    print("")
    print(color + "----LISTA DE USUARIOS----")

menu()

load_dotenv()

reg_user = r'^[1-9]|^\d+(,\d+)?E[+-]?\d+$'
users = []
index = 1
user_index_mapping = {}
lila = []
box_width = 36

file_path = os.getenv('csv_file_route')

data = open(file_path, newline='')  
data_red = csv.reader(data, delimiter=',')

color_w = Fore.WHITE

for row in data_red:
    # se agrega a una lista y diccionario los usuarios que no sean invitados y que no coincidan con la expresion regular
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

while True: #validacion del indice elegido
    user_index = int(input(color + "Seleccione un usuario con el número de índice: "))
    if user_index in user_index_mapping:
        selected_user = user_index_mapping[user_index]
        print(color_good + f"Usuario seleccionado: {selected_user}")
        break
    else:
        print(color_bad + "Índice seleccionado no válido. Intente nuevamente.")
    

print(color_w + f"+{'-' * (box_width - 2)}+")
date_in = input(color + "Por favor ingrese la fecha de inicio del rango (aaaa-mm-dd): ")
date_out = input(color + "Por favor ingrese la fecha del fin del rango (aaaa-mm-dd): ")
print(color_w + f"+{'-' * (box_width - 2)}+")

def str_to_date(date_in, date_out):

    date_in_obj = datetime.strptime(date_in, "%Y-%m-%d").date()
    date_out_obj = datetime.strptime(date_out, "%Y-%m-%d").date()

    return date_in_obj, date_out_obj

def validate_date(date_in, date_out):

    reg_date = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'

    date_in_obj, date_out_obj = str_to_date(date_in, date_out)

    if re.match(reg_date, date_in) and re.match(reg_date, date_out) and date_in_obj <= date_out_obj:
        pass
    else:
        raise ExceptionDate(color_bad + "Formato no válido de fechas. Ingrese nuevamente.")
    

while True:
    try:
        if validate_date(date_in, date_out):
            break
        break
    except ExceptionDate as e:
        print(e)
        date_in = input(color + "Por favor ingrese la fecha de inicio del rango (aaaa-mm-dd): ")
        date_out = input(color + "Por favor ingrese la fecha del fin del rango (aaaa-mm-dd): ")

dates = []

def dates_range(date_in, date_out):
    date_in_obj, date_out_obj = str_to_date(date_in, date_out)
    delta = timedelta(days=1)
    while date_in_obj <= date_out_obj:
        dates.append(date_in_obj.strftime("%Y-%m-%d"))
        date_in_obj += delta

dates_range(date_in, date_out)

data.seek(0)
pipa = []

for row in data_red:
    if row[3] == selected_user:
        lila.append(row)

for dat in dates:
    for row in lila:
        if row[6] == dat:
            modified_row = [row[3],row[6],row[7],row[8],row[9],row[13]]
            pipa.append(modified_row)


color = Fore.YELLOW
color_title = Fore.LIGHTMAGENTA_EX



# Imprimir los datos formateados en forma de tabla
if len(pipa) == 0:
    print("El usuario no tuvo sesiones activas en las instalaciones en el rango seleccionado")
else:
    print(color + "\n==================================== DATOS ====================================")
    print(Fore.RESET)
    print(color_title + f"{'Usuario':<20}{'Fecha Conexión Inicio':<25}{'Hora Inicio':<15}{'Fecha Conexión Fin':<25}{'Hora Fin':<15}{'MAC AP':<15}")
    print(Fore.RESET)
    for row in pipa:
        print(f"{row[0]:<20}{row[1]:<25}{row[2]:<15}{row[3]:<25}{row[4]:<15}{row[5]:<15}")

print("\n")

data.close() 