import re
from datetime import datetime, timedelta
from colorama import Fore

class ExceptionDate(Exception):
    """Excepción personalizada para manejar errores de formato de fecha."""
    pass

def menu():
    """
    Muestra el menú de bienvenida y la lista de usuarios en la consola con color cian.
    """
    color = Fore.CYAN
    print("")
    print(color + "----------------BIENVENIDOS----------------")
    print("")
    print(color + "----LISTA DE USUARIOS----")


def change_date_format(date_str):
    """
    Cambia el formato de una fecha de 'YYYY-MM-DD' a 'DD-MM-YYYY'.

    Args:
        date_str (str): Fecha en formato 'YYYY-MM-DD'.

    Returns:
        str: Fecha en formato 'DD-MM-YYYY'.

    Raises:
        ExceptionDate: Si el formato de la fecha no es válido.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        raise ExceptionDate(Fore.RED + f"Formato no válido para la fecha: {date_str}. Ingrese nuevamente.")


def str_to_date(date_in, date_out):
    """
    Convierte cadenas de fechas en objetos de fecha.

    Args:
        date_in (str): Fecha de inicio en formato 'DD-MM-YYYY'.
        date_out (str): Fecha de fin en formato 'DD-MM-YYYY'.

    Returns:
        tuple: Dos objetos de fecha correspondientes a las fechas de inicio y fin.

    Raises:
        ExceptionDate: Si el formato de las fechas no es válido.
    """
    try:
        date_in_obj = datetime.strptime(date_in, "%d-%m-%Y").date()
        date_out_obj = datetime.strptime(date_out, "%d-%m-%Y").date()
        return date_in_obj, date_out_obj
    except ValueError:
        raise ExceptionDate(Fore.RED + "Formato no válido de fechas. Ingrese nuevamente.")


def validate_date(date_in, date_out):
    """
    Valida el formato de las fechas y verifica que la fecha de inicio no sea posterior a la fecha de fin.

    Args:
        date_in (str): Fecha de inicio en formato 'DD-MM-YYYY'.
        date_out (str): Fecha de fin en formato 'DD-MM-YYYY'.

    Raises:
        ExceptionDate: Si alguna de las fechas no tiene un formato válido o si la fecha de inicio es posterior a la fecha de fin.
    """
    reg_date = r'^\d{2}-(0[1-9]|1[0-2])-\d{4}$'
    
    if not re.match(reg_date, date_in):
        raise ExceptionDate(Fore.RED + "Formato no válido de fecha de inicio. Ingrese nuevamente.")
    if not re.match(reg_date, date_out):
        raise ExceptionDate(Fore.RED + "Formato no válido de fecha de fin. Ingrese nuevamente.")
    
    date_in_obj, date_out_obj = str_to_date(date_in, date_out)
    
    if date_in_obj > date_out_obj:
        raise ExceptionDate(Fore.RED + "La fecha de inicio no puede ser posterior a la fecha de fin. Ingrese nuevamente.")


def dates_range(date_in, date_out):
    """
    Genera un rango de fechas entre las fechas de inicio y fin especificadas.

    Args:
        date_in (str): Fecha de inicio en formato 'DD-MM-YYYY'.
        date_out (str): Fecha de fin en formato 'DD-MM-YYYY'.

    Returns:
        list: Lista de fechas en el rango especificado, en formato 'DD-MM-YYYY'.
    """
    date_in_obj, date_out_obj = str_to_date(date_in, date_out)
    delta = timedelta(days=1)  # Para que se genere un rango de fechas de 1 día
    dates = []
    while date_in_obj <= date_out_obj:
        dates.append(date_in_obj.strftime("%d-%m-%Y"))
        date_in_obj += delta
    return dates
