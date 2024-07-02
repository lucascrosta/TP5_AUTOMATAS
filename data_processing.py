import re
from utils import change_date_format
from utils import ExceptionDate, MissingEndDate

def load_users(data_red, reg_user):
    """
    Carga y filtra una lista de usuarios únicos desde los datos proporcionados.

    Args:
        data_red (list): Lista de listas donde cada sublista representa una fila de datos.
        reg_user (str): Expresión regular para validar usuarios.

    Returns:
        tuple: 
            list: Lista de nombres de usuarios únicos en minúsculas.
            dict: Diccionario que mapea índices a nombres de usuarios.
    """
    users = []
    user_index_mapping = {}
    index = 1
    for row in data_red:
        if row[3] != 'Usuario' and row[3].lower() not in users and row[3] != 'invitado-deca' and not re.match(reg_user, row[3]):
            user_name = row[3].lower()
            users.append(user_name)
            user_index_mapping[index] = user_name
            index += 1
    return users, user_index_mapping


def get_user_data(data_red, selected_user):
    """
    Obtiene los datos del usuario seleccionado del archivo CSV.

    Args:
        data_red (list): Lista de listas donde cada sublista representa una fila de datos.
        selected_user (str): Nombre del usuario seleccionado.

    Returns:
        list: Lista de filas que corresponden al usuario seleccionado con fechas formateadas.
    
    Raises:
        ExceptionDate: Si el formato de la fecha no es válido.
        MissingEndDate: Si la fecha es una cadena vacía.
    """
    lila = [] 
    for row in data_red:
        if row[3] == selected_user:
            try:
                row[6] = change_date_format(row[6])
                row[8] = change_date_format(row[8])
            except ExceptionDate as e:
                print(e)
                return lila, False
            except MissingEndDate as e:
                print(e)
                return lila, False
            lila.append(row)
    return lila, True


def filter_user_data(lila, dates):
    """
    Filtra los datos del usuario seleccionado según el rango de fechas especificado.

    Args:
        lila (list): Lista de filas que corresponden al usuario seleccionado.
        dates (list): Lista de fechas en el formato 'dd-mm-aaaa' para filtrar.

    Returns:
        list: Lista de filas filtradas que corresponden al usuario seleccionado y al rango de fechas especificado.
    """
    pipa = []  
    for dat in dates:
        for row in lila:
            if row[6] == dat:
                modified_row = [row[3], row[6], row[7], row[8], row[9], row[13]]
                pipa.append(modified_row)
    return pipa
