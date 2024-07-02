# TP5_AUTOMATAS

## Descripción
Con el desarrollo de este proyecto se busca crear una aplicación que permita realizar un seguimiento de las sesiones de los usuarios en el rango de fechas deseado. El mismo se basa en la creación de un archivo de datos CSV que contenga los datos de las sesiones de los usuarios. Con esta información, se puede realizar análisis detallado y generar informes para evaluar la frecuencia de uso, duración de las sesiones, identificación de patrones de comportamiento, entre otros.
La información que se obtiene es el usuario, la fecha de inicio y fin de la sesión, la hora de inicio y fin y la MAC AP del usuario.

Funcionalidad Principal:

    Carga de Datos y Selección de Usuario:
        Carga los nombres únicos de usuarios desde un archivo CSV, excluyendo ciertos usuarios específicos y validando el formato con una expresión regular.
        Permite al usuario seleccionar un usuario específico de la lista cargada.

    Selección de Fechas:
        Solicita al usuario ingresar un rango de fechas (inicio y fin) en formato "dd-mm-aaaa".
        Valida que las fechas ingresadas sean válidas y que la fecha de inicio no sea posterior a la fecha de fin.

    Filtrado y Visualización de Datos:
        Filtra los datos del usuario seleccionado según el rango de fechas especificado.
        Muestra en consola los datos filtrados, incluyendo detalles como la fecha y hora de inicio y fin de las conexiones.

    Opciones Adicionales:
        Permite al usuario exportar los datos filtrados a un archivo Excel.
        Proporciona opciones para buscar otro usuario, otro rango de fechas o salir del programa.

Utilidades y Funciones Clave:

    Manejo de Fechas: Utiliza funciones para convertir formatos de fecha, validar entradas y generar listas de fechas dentro de un rango.

    Interfaz de Usuario Mejorada: Emplea la librería colorama para proporcionar colores en la consola, mejorando la legibilidad de las opciones y mensajes.

    Manejo de Excepciones Personalizadas: Define excepciones personalizadas para manejar errores específicos relacionados con el formato de fecha y datos faltantes.


Integrantes: Artola, Choque, Crosta, Guerra Díaz, Quinteros y Torres 