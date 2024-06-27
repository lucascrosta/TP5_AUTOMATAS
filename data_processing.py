import re
from utils import change_date_format

def load_users(data_red, reg_user):
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
    lila = [] # almacena todas las filas del archivo CSV que corresponden al usuario seleccionado
    for row in data_red:
        if row[3] == selected_user:
            row[6] = change_date_format(row[6])
            row[8] = change_date_format(row[8])  
            lila.append(row)
    return lila

def filter_user_data(lila, dates):
    pipa = [] #almacena las filas filtradas que corresponden al usuario seleccionado y al rango de fechas especificado.
    for dat in dates:
        for row in lila:
            if row[6] == dat:
                modified_row = [row[3], row[6], row[7], row[8], row[9], row[13]]
                pipa.append(modified_row)
    return pipa