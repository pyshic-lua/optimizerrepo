import os
import sys
import subprocess
import requests
import time
import shutil
import msvcrt
from colorama import init, Fore, Back
init(autoreset=True)

# Configuraciones Globales
USERNAME = 'pyshicDev'
REPO_NAME = 'pyOptimizer'
VERSION = '1.2'
LATESTTAGNAME = None
API_URL = f'https://api.github.com/repos/{USERNAME}/{REPO_NAME}/releases/latest'

# Estado de los Tweaks
OPCIONES_DE_RENDIMIENTO = False
MODO_OSCURO = False
PLAN_ENERGIA = False
LIMPIEZA = False
TELEMETRIA = False
MODO_JUEGO = False

def get_cols():
    return shutil.get_terminal_size().columns

def print_bloque_centrado(lista_opciones, titulo=None, color_titulo=Fore.CYAN):
    columnas = get_cols()
    
    if titulo:
        print(color_titulo + titulo.center(columnas) + "\n")
    
    def clean_len(s):
        import re
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return len(ansi_escape.sub('', s))

    ancho_maximo = max(clean_len(linea) for linea in lista_opciones)
    margen_izquierdo = (columnas - ancho_maximo) // 2
    padding = " " * margen_izquierdo
    
    for linea in lista_opciones:
        print(padding + linea)

def checkLatestTagName():
    global LATESTTAGNAME
    try:
        respuesta = requests.get(API_URL, timeout=5)
        if respuesta.status_code == 200:
            release_data = respuesta.json()
            LATESTTAGNAME = release_data['tag_name']
            return True      
    except:
        print(Fore.RED + f"[!] Error, revise su conexion a internet")
        return sys.exit(2)

def interfaz():
    os.system('cls')
    columnas = get_cols()
    banner = r"""               ___       _   _           _              
 _ __  _   _  /___\_ __ | |_(_)_ __ ___ (_)_______ _ __ 
| '_ \| | | |//  // '_ \| __| | '_ ` _ \| |_  / _ \ '__|
| |_) | |_| / \_//| |_) | |_| | | | | | | |/ /  __/ |   
| .__/ \__, \___/ | .__/ \__|_|_| |_| |_|_/___\___|_|   
|_|    |___/      |_|                                   
"""
    for linea in banner.split('\n'):
        print(Fore.LIGHTCYAN_EX + linea.center(columnas))
    
    if str(VERSION) > LATESTTAGNAME:
        print(Fore.LIGHTCYAN_EX + f"[Version {VERSION} (unPublished) - Developed by {USERNAME}]".center(columnas) + "\n")
    elif str(VERSION) <= LATESTTAGNAME:
        print(Fore.LIGHTCYAN_EX + f"[Version {VERSION} - Developed by {USERNAME}]".center(columnas) + "\n")
    
    
    

def check_updates():
    if str(VERSION) < LATESTTAGNAME:
        print_bloque_centrado([
            Fore.GREEN + f"[!] Nueva version disponible: {LATESTTAGNAME}",
            Fore.YELLOW + f"[-] Estas usando la version: {VERSION}",
            Fore.CYAN + f"Descargala en: https://github.com/{USERNAME}/{REPO_NAME}/releases/latest\n",
            Fore.WHITE + f"[~] Presione cualquier tecla para continuar en esta version."
        ])
        msvcrt.getch()
    else: return False
 

def check_net():
    try:
        requests.get("https://google.com", timeout=3)
        return True
    except:
        return False

def limpiarTemporales():
    interfaz()
    rutas_temp = [os.environ.get('TEMP'), os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp')]
    
    print_bloque_centrado([Fore.YELLOW + "[*] Iniciando limpieza de archivos temporales..."])
    
    archivos_borrados, errores = 0, 0
    for ruta in rutas_temp:
        if not ruta or not os.path.exists(ruta): continue
        for nombre in os.listdir(ruta):
            ruta_completa = os.path.join(ruta, nombre)
            try:
                if os.path.isfile(ruta_completa) or os.path.islink(ruta_completa): os.unlink(ruta_completa)
                elif os.path.isdir(ruta_completa): shutil.rmtree(ruta_completa)
                archivos_borrados += 1
            except: errores += 1
            
    print_bloque_centrado([
        Fore.GREEN + f"[+] Limpieza completada.",
        Fore.WHITE + f"    Borrados: {archivos_borrados}",
        Fore.WHITE + f"    En uso: {errores}"
    ])
    return True
def desactivarModoJuego():
    interfaz()
    columnas = get_cols()
    
    comandos_gaming = [
        ['reg', 'add', 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\GraphicsDrivers', '/v', 'HwSchMode', '/t', 'REG_DWORD', '/d', '2', '/f'],
        
        ['reg', 'add', 'HKCU\\Software\\Microsoft\\GameBar', '/v', 'AllowAutoGameMode', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\\Software\\Microsoft\\GameBar', '/v', 'AutoGameModeEnabled', '/t', 'REG_DWORD', '/d', '0', '/f'],
        
        ['reg', 'add', 'HKCU\\System\\GameConfigStore', '/v', 'GameDVR_FSEBehaviorMode', '/t', 'REG_DWORD', '/d', '2', '/f']
    ]

    print_bloque_centrado([
        Fore.YELLOW + "[*] Desactivando Modo juego..",
    ])

    for cmd in comandos_gaming:
        try:
            subprocess.run(cmd, capture_output=True, check=False)
        except:
            continue

    print_bloque_centrado([
        Fore.GREEN + "            [+] Modo juego ha sido desactivado.",
        Fore.WHITE + "  Es necesario reiniciar para aplicar algunos cambios de GPU."
    ])
    return True
def aplicar_alto_rendimiento():
    interfaz()
    guid = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
    try:
        subprocess.run(["powercfg", "/setactive", guid], check=True, capture_output=True)
        print_bloque_centrado([Fore.GREEN + "[+] Plan de Alto Rendimiento activado con éxito."])
        return True
    except:
        print_bloque_centrado([Fore.RED + "[!] Error: Ejecuta como administrador."])
        return False

def activarModoOscuro():
    interfaz()
    commands = [
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'SystemUsesLightTheme', '/t', 'REG_DWORD', '/d', '0', '/f']
    ]
    try:
        for cmd in commands: subprocess.run(cmd, check=True, capture_output=True)
        print_bloque_centrado([Fore.GREEN + "[+] Modo oscuro activado."])
        return True
    except: return False

def desactivarModoOscuro():
    interfaz()
    commands = [
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'AppsUseLightTheme', '/t', 'REG_DWORD', '/d', '1', '/f'],
        ['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize', '/v', 'SystemUsesLightTheme', '/t', 'REG_DWORD', '/d', '1', '/f']
    ]
    try:
        for cmd in commands: subprocess.run(cmd, check=True, capture_output=True)
        print_bloque_centrado([Fore.YELLOW + "[-] Modo oscuro desactivado."])
        return True
    except: return False

def opcionesDeRendimiento():
    interfaz()
    comandos = [['reg', 'add', 'HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects', '/v', 'VisualFXSetting', '/t', 'REG_DWORD', '/d', '3', '/f']]
    try:
        for cmd in comandos: 
            subprocess.run(cmd, check=True, capture_output=True)
        
        print_bloque_centrado([Fore.YELLOW + "[*] Reiniciando Explorer..."])
        subprocess.run(['taskkill', '/f', '/im', 'explorer.exe'], capture_output=True)
        time.sleep(1)

        os.system('start explorer.exe')
        
        return True
    except Exception as e: 
        os.system('start explorer.exe')
        return False
    
def tareasTelemetria():

    interfaz()
    tareas = [
        r"\Microsoft\Windows\Customer Experience Improvement Program\Consolidator",
        r"\Microsoft\Windows\Customer Experience Improvement Program\BthSQM",
        r"\Microsoft\Windows\Customer Experience Improvement Program\KernelCeipTask",
        r"\Microsoft\Windows\Customer Experience Improvement Program\UsbCeip",
        r"\Microsoft\Windows\Customer Experience Improvement Program\Uploader",
        r"\Microsoft\Windows\Application Experience\Microsoft Compatibility Appraiser",
        r"\Microsoft\Windows\Application Experience\ProgramDataUpdater",
        r"\Microsoft\Windows\Application Experience\StartupAppTask",
        r"\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector",
        r"\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver",
        r"\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem",
        r"\Microsoft\Windows\Shell\FamilySafetyMonitor",
        r"\Microsoft\Windows\Shell\FamilySafetyRefresh",
        r"\Microsoft\Windows\Shell\FamilySafetyUpload",
        r"\Microsoft\Windows\Autochk\Proxy",
        r"\Microsoft\Windows\Maintenance\WinSAT",
        r"\Microsoft\Windows\Application Experience\AitAgent",
        r"\Microsoft\Windows\Windows Error Reporting\QueueReporting",
        r"\Microsoft\Windows\CloudExperienceHost\CreateObjectTask",
        r"\Microsoft\Windows\DiskFootprint\Diagnostics",
        r"\Microsoft\Windows\FileHistory\File History (maintenance mode)",
        r"\Microsoft\Windows\PI\Sqm-Tasks",
        r"\Microsoft\Windows\NetTrace\GatherNetworkInfo",
        r"\Microsoft\Windows\AppID\SmartScreenSpecific",
        r"\Microsoft\Windows\WindowsUpdate\Automatic App Update",
        r"\Microsoft\Windows\Time Synchronization\ForceSynchronizeTime",
        r"\Microsoft\Windows\Time Synchronization\SynchronizeTime",
        r"\Microsoft\Windows\HelloFace\FODCleanupTask",
        r"\Microsoft\Windows\Feedback\Siuf\DmClient",
        r"\Microsoft\Windows\Feedback\Siuf\DmClientOnScenarioDownload",
        r"\Microsoft\Windows\Application Experience\PcaPatchDbTask",
        r"\Microsoft\Windows\Device Information\Device",
        r"\Microsoft\Windows\Device Information\Device User"
    ]

    print_bloque_centrado([Fore.YELLOW + f"[*] Desactivando {len(tareas)} tareas de telemetría.."])
    
    desactivadas = 0
    for tarea in tareas:
        try:
            subprocess.run(["schtasks", "/end", "/tn", tarea], capture_output=True, text=True)
            result = subprocess.run(["schtasks", "/change", "/tn", tarea, "/disable"], capture_output=True, text=True)
            
            if result.returncode == 0:
                desactivadas += 1
        except Exception:
            continue

    print_bloque_centrado([
        Fore.GREEN + f"[+] Optimización de tareas completada.",
        Fore.WHITE + f"    Tareas desactivadas: {desactivadas}\n",
    ])
    return True
def serviciosTelemetria():
    interfaz()
    columnas = get_cols()
    servicios = [
        "DiagTrack", 
        "diagnosticshub.standardcollector.service", 
        "dmwappushservice", 
        "DcpSvc",
        "WdiServiceHost"
    ]

    print_bloque_centrado([Fore.YELLOW + f"[*] Deteniendo {len(servicios)} servicios de rastreo..."])

    for servicio in servicios:
        subprocess.run(["sc", "stop", servicio], capture_output=True, text=True)
        subprocess.run(["sc", "config", servicio, "start=", "disabled"], capture_output=True, text=True)

    comandos_reg = [
        ['reg', 'add', 'HKLM\\Software\\Microsoft\\PolicyManager\\default\\WiFi\\AllowAutoConnectToWiFiSenseHotspots', '/v', 'value', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKLM\\Software\\Microsoft\\PolicyManager\\default\\WiFi\\AllowWiFiHotSpotReporting', '/v', 'value', '/t', 'REG_DWORD', '/d', '0', '/f'],
        
        ['reg', 'add', 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\System', '/v', 'PublishUserActivities', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKLM\\SOFTWARE\\Policies\\Microsoft\\SQMClient\\Windows', '/v', 'CEIPEnable', '/t', 'REG_DWORD', '/d', '0', '/f'],
        
        ['reg', 'add', 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'DisableEngine', '/t', 'REG_DWORD', '/d', '1', '/f'],
        ['reg', 'add', 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'SbEnable', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'AITEnable', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'DisableInventory', '/t', 'REG_DWORD', '/d', '1', '/f'],
        ['reg', 'add', 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'DisablePCA', '/t', 'REG_DWORD', '/d', '1', '/f'],
        ['reg', 'add', 'HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'DisableUAR', '/t', 'REG_DWORD', '/d', '1', '/f'],
        
        ['reg', 'add', 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Device Metadata', '/v', 'PreventDeviceMetadataFromNetwork', '/t', 'REG_DWORD', '/d', '1', '/f'],
        ['reg', 'add', 'HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\SQMLogger', '/v', 'Start', '/t', 'REG_DWORD', '/d', '0', '/f'],
        ['reg', 'add', 'HKLM\\SOFTWARE\\Microsoft\\PolicyManager\\current\\device\\System', '/v', 'AllowExperimentation', '/t', 'REG_DWORD', '/d', '0', '/f']
    ]

    if sys.maxsize > 2**32:
        comandos_reg.extend([
            ['reg', 'add', 'HKLM\\SOFTWARE\\Wow6432Node\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'DisableEngine', '/t', 'REG_DWORD', '/d', '1', '/f'],
            ['reg', 'add', 'HKLM\\SOFTWARE\\Wow6432Node\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'SbEnable', '/t', 'REG_DWORD', '/d', '0', '/f'],
            ['reg', 'add', 'HKLM\\SOFTWARE\\Wow6432Node\\Policies\\Microsoft\\Windows\\AppCompat', '/v', 'DisablePCA', '/t', 'REG_DWORD', '/d', '1', '/f']
        ])

    print_bloque_centrado([Fore.YELLOW + "[*] Aplicando políticas de privacidad en el Registro..."])

    for cmd in comandos_reg:
        try:
            subprocess.run(cmd, capture_output=True, check=False)
        except:
            continue

    print_bloque_centrado([
        Fore.GREEN + "[+] Telemetría y servicios deshabilitados con éxito.",
        Fore.WHITE + "    Nota: Algunos cambios requieren reiniciar el PC."
    ])
    return True
def telemetria():
    if tareasTelemetria(): 
        if serviciosTelemetria(): return True
        else: return False           
    else: return False


def windows_tweaks():
    global OPCIONES_DE_RENDIMIENTO, MODO_OSCURO, PLAN_ENERGIA, LIMPIEZA, TELEMETRIA, MODO_JUEGO
    while True:
        interfaz()
        cols = get_cols()
        
        opciones = [
            f"{Fore.GREEN if OPCIONES_DE_RENDIMIENTO else Fore.WHITE}[1] Opciones de rendimiento visual",
            f"{Fore.GREEN if MODO_OSCURO else Fore.WHITE}[2] {'Desactivar ' if MODO_OSCURO else ''}Modo Oscuro",
            f"{Fore.GREEN if PLAN_ENERGIA else Fore.WHITE}[3] Aplicar Plan de Energia (Maximo Rendimiento)",
            f"{Fore.GREEN if LIMPIEZA else Fore.WHITE}[4] Borrar archivos temporales",
            f"{Fore.GREEN if TELEMETRIA else Fore.WHITE}[5] Desactivar Telemetria",
            f"{Fore.GREEN if MODO_JUEGO else Fore.WHITE}[6] Desactivar Modo Juego",
            f"{Fore.WHITE}[7] Volver"
        ]
        
        print_bloque_centrado(opciones, titulo="[+] Windows 10/11 Tweaks")
        
        prompt = "> "
        ancho_input = 2 
        margen_input = (cols - ancho_input) // 2
        x = input("\n" + (" " * margen_input) + prompt)
        
        if x == '1':
            if opcionesDeRendimiento(): OPCIONES_DE_RENDIMIENTO = True; time.sleep(1)
            else: print_bloque_centrado([Fore.RED + "[~] Error al aplicar, intente nuevamente"])
        elif x == '2':
            if MODO_OSCURO:
                if desactivarModoOscuro(): MODO_OSCURO = False; time.sleep(1)
                else: print_bloque_centrado([Fore.RED + "[~] Error al aplicar, intente nuevamente"])
            else:
                if activarModoOscuro(): MODO_OSCURO = True; time.sleep(1)
                else: print_bloque_centrado([Fore.RED + "[~] Error al aplicar, intente nuevamente"])
        elif x == '3':
            if aplicar_alto_rendimiento(): PLAN_ENERGIA = True; time.sleep(1)
            else: print_bloque_centrado([Fore.RED + "[~] Error al aplicar, intente nuevamente"])
                
        elif x == '4':
            if limpiarTemporales():
                LIMPIEZA = True
                print("\n")
                print_bloque_centrado([Fore.YELLOW + "[~] Presione cualquier tecla para volver.."])
                msvcrt.getch()
        elif x == '5':
            if telemetria():
                TELEMETRIA = True
                print("\n")
                print_bloque_centrado([Fore.YELLOW + "[~] Presione cualquier tecla para volver.."])
                msvcrt.getch()
        elif x == '6':
            if desactivarModoJuego():
                MODO_JUEGO = True
                print("\n")
                print_bloque_centrado([Fore.YELLOW + "[~] Presione cualquier tecla para volver.."])
                msvcrt.getch()
        elif x == '7': break

def menu():
    global OPCIONES_DE_RENDIMIENTO, MODO_OSCURO, PLAN_ENERGIA, LIMPIEZA, TELEMETRIA
    if not check_net():
        interfaz()
        print_bloque_centrado([Fore.RED + "[!] Error: Sin conexión a Internet."])
        sys.exit(2)
    
    interfaz()
    check_updates()

    while True:
        interfaz()
        cols = get_cols()
        
        if OPCIONES_DE_RENDIMIENTO and MODO_OSCURO and PLAN_ENERGIA and LIMPIEZA and TELEMETRIA and MODO_JUEGO:
            txt_tweaks = Back.GREEN + Fore.BLACK + "[1] Windows 10/11 Tweaks" + Back.RESET
        else:
            txt_tweaks = "[1] Windows 10/11 Tweaks"

        opciones_main = [txt_tweaks, "[2] Salir"]
        print_bloque_centrado(opciones_main)

        prompt = "> "
        ancho_input = 5
        margen_input = (cols - ancho_input) // 2
        x = input("\n" + (" " * margen_input) + prompt)
        
        if x == '1': windows_tweaks()
        elif x == '2': sys.exit()

if __name__ == "__main__":
    try:
        checkLatestTagName()
        menu()
    except Exception:
        import traceback
        os.system('cls')
        cols = get_cols()
        print_bloque_centrado([
            Fore.RED + "[~] Se ha detectado un error:",
        ])
        traceback.print_exc()
        print("\n")
        print_bloque_centrado([Fore.YELLOW + "Presiona ENTER para salir.."])
        input()
