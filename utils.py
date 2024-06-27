import re
from datetime import datetime, timedelta
from colorama import Fore

class ExceptionDate(Exception):
    pass

def menu():
    color = Fore.CYAN
    print("")
    print(color + "----------------BIENVENIDOS----------------")
    print("")
    print(color + "----LISTA DE USUARIOS----")

def change_date_format(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        raise ExceptionDate(Fore.RED + f"Formato no válido para la fecha: {date_str}. Ingrese nuevamente.")

def str_to_date(date_in, date_out):
    try:
        date_in_obj = datetime.strptime(date_in, "%d-%m-%Y").date()
        date_out_obj = datetime.strptime(date_out, "%d-%m-%Y").date()
        return date_in_obj, date_out_obj
    except ValueError:
        raise ExceptionDate(Fore.RED + "Formato no válido de fechas. Ingrese nuevamente.")

def validate_date(date_in, date_out):
    # Expresión regular para validar fechas en formato 'dd-mm-aaaa'
    reg_date = r'^\d{2}-(0[1-9]|1[0-2])-\d{4}$'
    
    if not re.match(reg_date, date_in):
        raise ExceptionDate(Fore.RED + "Formato no válido de fecha de inicio. Ingrese nuevamente.")
    if not re.match(reg_date, date_out):
        raise ExceptionDate(Fore.RED + "Formato no válido de fecha de fin. Ingrese nuevamente.")
    
    date_in_obj, date_out_obj = str_to_date(date_in, date_out)
    
    if date_in_obj > date_out_obj:
        raise ExceptionDate(Fore.RED + "La fecha de inicio no puede ser posterior a la fecha de fin. Ingrese nuevamente.")

def dates_range(date_in, date_out):
    # Generar un rango de fechas en formato 'dd-mm-aaaa'
    date_in_obj, date_out_obj = str_to_date(date_in, date_out)
    delta = timedelta(days=1)  # Para que se genere un rango de fechas de 1 día
    dates = []
    while date_in_obj <= date_out_obj:
        dates.append(date_in_obj.strftime("%d-%m-%Y"))
        date_in_obj += delta
    return dates
