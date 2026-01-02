import os
import sys

def check_updates():
    try:
        respuesta = requests.get(API_URL)
        if respuesta.status_code == 200:
                release_data = respuesta.json()
                latest_tag_name = release_data['tag_name']

        if str(VERSION) != latest_tag_name:
            print(Fore.GREEN + f"[!] Nueva version disponible: {latest_tag_name}")
            print(Fore.YELLOW + f"[!] Estas usando la version: {VERSION}")
            print(Fore.CYAN + f"Descargala en: https://github.com/{USERNAME}/{REPO_NAME}/releases/latest\n")
            print("[!] Presione cualquier tecla para continuar en esta version.")
            msvcrt.getch()
            return False 
        else:
            return False 
            
    except Exception:
        return False
def check_net():
    try:
        requests.get("https://google.com", timeout=3)
        return True
    except:
        return False 
def limpiar_temporales():
    os.system('cls')
    rutas_temp = [
        os.environ.get('TEMP'),
        os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')
    ] 
    print(Fore.YELLOW + "[*] Iniciando limpieza de archivos temporales...")
    archivos_borrados = 0
    errores = 0

    for ruta in rutas_temp:
        if not os.path.exists(ruta):
            continue
        for nombre in os.listdir(ruta):
            ruta_completa = os.path.join(ruta, nombre)
            try:
                if os.path.isfile(ruta_completa) or os.path.islink(ruta_completa):
                    os.unlink(ruta_completa)
                elif os.path.isdir(ruta_completa):
                    shutil.rmtree(ruta_completa)
                archivos_borrados += 1
            except Exception:
                errores += 1
                continue

    print(Fore.GREEN + f"[+] Limpieza completada. Borrados: {archivos_borrados} | En uso: {errores}")
    return True
def aplicar_alto_rendimiento():
    os.system('cls')
    guid_alto_rendimiento = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
    try:
        
        resultado = subprocess.run(
            ["powercfg", "/setactive", guid_alto_rendimiento],
            capture_output=True,
            text=True,
            check=True
        )
        os.system('cls')
        print(Fore.GREEN + "[+] Plan de Alto Rendimiento activado con éxito.")
        return True
    except subprocess.CalledProcessError:
        os.system('cls')
        print(Fore.RED + "[!] Error: No se pudo activar el plan. Ejecuta el programa con permisos de administrador.")
        return False
def activarModoOscuro():
    os.system('cls')
    commands = [
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'ColorPrevalence', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'EnableTransparency', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'SystemUsesLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f']
    ]
    
    try:
        for cmd in commands:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(Fore.GREEN + "[+] Modo oscuro activado con éxito.")   
        return True
        
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error al modificar el registro: {e}")
        return False   
def desactivarModoOscuro():
    os.system('cls')
    commands = [
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'ColorPrevalence', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'EnableTransparency', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '1', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'SystemUsesLightTheme', '/t', 'REG_DWORD', '/d', '1', '/f']
    ]
    
    try:
        for cmd in commands:
            subprocess.run(cmd, check=True, capture_output=True, text=True) 
        print(Fore.YELLOW + "[-] Modo oscuro desactivado.")        
        return True
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error al modificar el registro: {e}")
        return False
def opcionesDeRendimiento():
    os.system('cls')
    comandos = [
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects', '/v', 'VisualFXSetting', '/t', 'REG_DWORD', '/d', '3', '/f'],
        ['reg', 'add', 'HKCU\Control Panel\Desktop', '/v', 'UserPreferencesMask', '/t', 'REG_BINARY', '/d', '9012018010000000', '/f'],
        ['reg', 'add', 'HKCU\Control Panel\Desktop\WindowMetrics', '/v', 'MinAnimate', '/t', 'REG_SZ', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', '/v', 'TaskbarAnimations', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\DWM', '/v', 'EnableAeroPeek', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\DWM', '/v', 'AlwaysHibernateThumbnails', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', '/v', 'DisablePreviewDesktop', '/t', 'REG_DWORD', '/d', '1', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', '/v', 'ThumbnailLivePreview', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', '/v', 'IconsOnly', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', '/v', 'ListviewShadow', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced', '/v', 'ListviewAlphaSelect', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Control Panel\Desktop', '/v', 'DragFullWindows', '/t', 'REG_SZ', '/d', '1', '/f'],
        ['reg', 'add', 'HKCU\Control Panel\Desktop', '/v', 'FontSmoothing', '/t', 'REG_SZ', '/d', '2', '/f']
    ]

    try:
        for cmd in comandos:
            subprocess.run(cmd, check=True, capture_output=True)

        subprocess.run(['RUNDLL32.EXE', 'user32.dll', 'UpdatePerUserSystemParameters'], check=True)

        print(Fore.YELLOW + "[*] Reiniciando Explorer para aplicar cambios...")
        subprocess.run(['taskkill', '/f', '/im', 'explorer.exe'], check=True, capture_output=True)
        time.sleep(2)
        subprocess.Popen(['start', 'explorer.exe'], shell=True)
        
        return True
    except Exception as e:
        print(f"Error al aplicar rendimiento: {e}")
        os.system("start explorer.exe")
        return False

def windows_tweaks():
    global OPCIONES_DE_RENDIMIENTO, MODO_OSCURO, PLAN_ENERGIA, LIMPIEZA
    while True:
        os.system('cls')

        print(Fore.CYAN + "[+] Windows 10/11 Tweaks\n")
        if OPCIONES_DE_RENDIMIENTO:
            print(Fore.GREEN + "[1] Opciones de rendimiento visual")
        else:
            print("[1] Opciones de rendimiento visual")
        if MODO_OSCURO:
            print(Fore.GREEN + "[2] Desactivar Modo Oscuro")
        else:
            print("[2] Modo Oscuro")    
        if PLAN_ENERGIA:
            print(Fore.GREEN + "[3] Aplicar Plan de Energia (Maximo Rendimiento)")
        else:
            print("[3] Aplicar Plan de Energia (Maximo Rendimiento)")
        if LIMPIEZA:
            print(Fore.GREEN + "[4] Borrar archivos temporales")
        else:
            print("[4] Borrar archivos temporales")
        
        print("[5] Volver\n")
        x = input()
        if not x.isdigit():
                os.system('cls')
                continue           
        opcion = int(x)
        if opcion == 1:
            bat = opcionesDeRendimiento()
            if bat:
                OPCIONES_DE_RENDIMIENTO = True
                time.sleep(1)
                os.system('cls')
            else:
                print("Ocurrio un error inesperado, intente nuevamente.")
                time.sleep(3)
                os.system('cls') 
        elif opcion == 2:
            if MODO_OSCURO:
                bat = desactivarModoOscuro()
                if bat:
                    MODO_OSCURO = False
                    time.sleep(1)
                    os.system('cls')
                else:
                    print("Ocurrio un error inesperado, intente nuevamente.")
                    time.sleep(3)
                    os.system('cls')
            else:
                bat = activarModoOscuro()
                if bat:
                    MODO_OSCURO = True
                    time.sleep(1)
                    os.system('cls')
                else:
                    print("Ocurrio un error inesperado, intente nuevamente.")
                    time.sleep(3)
                    os.system('cls')
        elif opcion == 3:
            if aplicar_alto_rendimiento():
                PLAN_ENERGIA = True
                time.sleep(1)
                os.system('cls')
            else:
                print("Ocurrio un error inesperado, intente nuevamente.")
                time.sleep(1)
                os.system('cls')
        elif opcion == 4:
            if limpiar_temporales():
                LIMPIEZA = True
                print(Fore.LIGHTYELLOW_EX + "\n[!] Presione cualquier tecla para volver al menú...")
                msvcrt.getch()
                os.system('cls')
            else:
                print("Ocurrio un error inesperado, intente nuevamente.")
                time.sleep(1)
                os.system('cls')
        elif opcion == 5:
            return

def menu():
    global OPCIONES_DE_RENDIMIENTO, MODO_OSCURO, PLAN_ENERGIA, LIMPIEZA
    if check_net():   
        if check_updates():
            msvcrt.getch() # only for Debug :D
        else:
            while True:
                os.system('cls')
                print(Fore.LIGHTCYAN_EX + "[+] pyOptimizer - by pyshiclua")
                print(Fore.GREEN + f"[+] release {VERSION}\n")
                if OPCIONES_DE_RENDIMIENTO and MODO_OSCURO and PLAN_ENERGIA and LIMPIEZA:
                    print(Back.GREEN + Fore.BLACK + "[1] Windows 10/11 Tweaks")
                else:
                    print("[1] Windows 10/11 Tweaks")

                print("[2] Salir\n")
                x = input()
                if not x.isdigit():
                    os.system('cls')
                    continue           
                opcion = int(x)

                if opcion == 1:
                    windows_tweaks()           
                elif opcion == 2:
                    sys.exit()
                else:       
                    os.system('cls')
    else:
        print(Fore.RED + "Necesitas conexion a internet para ejecutar este programa, verifique su conexion.")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    USERNAME = 'pyshic-lua'
    REPO_NAME = 'optimizerrepo'
    VERSION = '1.1'
    API_URL = f'https://api.github.com/repos/{USERNAME}/{REPO_NAME}/releases/latest'
    OPCIONES_DE_RENDIMIENTO = False
    MODO_OSCURO = False
    PLAN_ENERGIA = False
    LIMPIEZA = False

    try:
        import subprocess
        import requests
        import time
        import shutil
        import msvcrt
        from colorama import init, Fore, Back
        init(autoreset=True)    
        
        menu()
        
    except Exception as e:
        import traceback
        print("\n" + "="*60)
        print("Se detecto un error.")
        print(traceback.format_exc())
        print("="*60)
        input("\nPresiona ENTER para cerrar y ver el error..")       

