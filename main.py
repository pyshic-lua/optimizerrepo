import os
import subprocess
import requests
import tempfile
import time

def opcionesDeRendimiento():   
    url = "https://raw.githubusercontent.com/pyshic-lua/optimizerrepo/refs/heads/main/tweaks/opciones-de-rendimiento.bat"
    ruta_temporal = os.path.join(tempfile.gettempdir(), "opciones-de-rendimiento.bat")

    try:
        respuesta = requests.get(url)      
        if respuesta.status_code == 200:
            with open(ruta_temporal, "wb") as archivo:
                archivo.write(respuesta.content)        

            subprocess.run([ruta_temporal], shell=True)
            
            if os.path.exists(ruta_temporal):
                os.remove(ruta_temporal)
                return True
        else:
            print(f"Error al conectar con el servidor: {respuesta.status_code}")
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False

def menu():
    while True:

        print("[*] pyOptimizer - release 1.0 - by pyshiclua")
        print("[1] Opciones de Rendimiento")
        print("[2] Salir")
        x = input("> ")
        opcion = int(x)

        if opcion == 1:
         bat = opcionesDeRendimiento()
         if bat:
             time.sleep(1)
             os.system('cls')
         else:
            print("Ocurrio un error inesperado, intente nuevamente.")
            time.sleep(3)
            os.system('cls')
         
        elif opcion == 2:
            break
        else:       
            print("Opcion no valida, ingrese otro numero.")
            time.sleep(1)
            os.system('cls')

if __name__ == "__main__":
    menu()        

