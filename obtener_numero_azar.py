# import date
import datetime
import mechanicalsoup
import threading

dice_URL = 'http://olympus.realpython.org/dice'                                                 # URL del sitio web
timeout = 10                                                                                    # Tiempo de espera entre consultas al sitio web
n_execution = 6                                                                                 # Cantidad total de consultas
i = 0                                                                                           # Contador de consultas
browser = mechanicalsoup.StatefulBrowser()                                                      # Inicialización del navegador web

def print_message():
    global i

    try:
        response = browser.open(dice_URL)                                                       # Abrir sitio web
        if response.status_code==200:                                                           # Verificar la respuesta del servidor
            response = browser.get_current_page().find_all('h2', {'id' : 'result'})             # Buscar el elemento 'h2' con la propiedad id='result'
            out_str = "Me salió un '" + response[0].next + "' el día "                          # Formar string con número del dado obtenido
            response = browser.get_current_page().find_all('p', {'id' : 'time'})                # Buscar el elemento 'p' con la propiedad id='time'
            out_str = out_str + response[0].next                                                # Formar string final
            print(out_str)                                                                      # Mostrar string por el stdout
        else:
            print("Eroor. Código de respuesta:", response.status_code)                          # Imprimir código de respuesta en caso de error
    except:
        print('Error al comunicarse con el servidor')                                           # Avisar que no se pudo hacer conexión con el servidor
    
    i += 1                                                                                      # Contar ejecución actual
    if i>=n_execution:                                                                          # Lógica de término de ejecución del programa
        return
    else:
        threading.Timer(timeout, print_message).start()                                         # Crear un timer para la ejecución de la tarea en un hilo distinto, para no colgar el programa

print_message()                                                                                 # Comienzo de ejecución de la tarea