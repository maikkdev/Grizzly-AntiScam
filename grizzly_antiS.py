#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# ===== BANNER =====
def banner():
    print(Fore.CYAN + "="*50)
    print(Fore.MAGENTA + Style.BRIGHT + "        GRIZZLY - WEBHOOK TOOL")
    print(Fore.YELLOW + "         Gestion - Seguridad - Mensajes")
    print(Fore.CYAN + "="*50 + "\n")

banner()

# ===== USO RESPONSABLE E INSTRUCCIONES =====
def instrucciones():
    print(Fore.YELLOW + Style.BRIGHT + "USO RESPONSABLE, EDUCATIVO Y TERMINOS LEGALES\n")
    
    print(Fore.CYAN + "INSTRUCCIONES DE USO")
    print(Fore.CYAN + "1. Este script solo debe usarse en tus propias webhooks de Discord.")
    print(Fore.CYAN + "2. Usa el script solo con fines educativos o para gestionar tus mensajes.")
    print(Fore.CYAN + "3. No intentes usar este script para atacar o afectar webhooks de otros usuarios.")
    print(Fore.CYAN + "4. Antes de enviar mensajes multiples, revisa que la webhook sea tuya y no cause abuso de la plataforma.")
    print(Fore.CYAN + "5. Evita enviar spam excesivo que pueda violar las normas de Discord.\n")
    
    print(Fore.YELLOW + "TERMINOS LEGALES Y RESPONSABILIDAD")
    print(Fore.CYAN + "1. Cualquier uso indebido de este script para danar terceros es ilegal.")
    print(Fore.CYAN + "2. El autor de este script no se responsabiliza por danos ocasionados por mal uso.")
    print(Fore.CYAN + "3. Usuarios que violen leyes locales, nacionales o internacionales pueden ser perseguidos legalmente.")
    print(Fore.CYAN + "4. Al usar este script, aceptas estas condiciones y reconoces tu responsabilidad.\n")
    
    print(Fore.YELLOW + "COMO USAR EL SCRIPT")
    print(Fore.CYAN + "1. Ejecuta el script en tu entorno Python 3 compatible (Linux, Termux, Windows).")
    print(Fore.CYAN + "2. Ingresa tu webhook cuando el script lo pida.")
    print(Fore.CYAN + "3. Elige una opcion del menu: ver info, editar, enviar mensaje, enviar spam, eliminar webhook.")
    print(Fore.CYAN + "4. Sigue las instrucciones en pantalla para cada opcion.")
    print(Fore.CYAN + "5. Recuerda siempre usar con moderacion y responsabilidad.\n")
    
    input(Fore.GREEN + "Presiona ENTER para continuar..." + Fore.RESET)

instrucciones()

# ===== Input de webhook =====
WEBHOOK = input(Fore.YELLOW + "Webhook -> " + Fore.RESET).strip()
if not WEBHOOK:
    print(Fore.RED + "Webhook invalida")
    exit()

# ===== Funciones =====
def ver_info():
    try:
        res = requests.get(WEBHOOK)
        data = res.json()
        print(Fore.CYAN + "\nInformacion de la webhook")
        print(Fore.GREEN + f"Nombre       : {data.get('name')}")
        print(Fore.GREEN + f"Avatar       : {data.get('avatar')}")
        print(Fore.GREEN + f"Canal ID     : {data.get('channel_id')}")
        print(Fore.GREEN + f"Servidor ID  : {data.get('guild_id')}\n")
    except Exception as e:
        print(Fore.RED + f"Error al obtener info: tu webhook quizas haiga sido eliminada o el link es incorrecto")

def editar_nombre():
    nuevo_nombre = input(Fore.YELLOW + "Nuevo nombre -> " + Fore.RESET)
    try:
        requests.patch(WEBHOOK, json={"name": nuevo_nombre})
        print(Fore.GREEN + "Nombre actualizado\n")
    except Exception as e:
        print(Fore.RED + f"Error al actualizar nombre: tu webhook quizas haiga sido eliminada o el link es incorrecto")

def editar_avatar():
    url_avatar = input(Fore.YELLOW + "URL del avatar -> " + Fore.RESET)
    try:
        requests.patch(WEBHOOK, json={"avatar": url_avatar})
        print(Fore.GREEN + "Avatar actualizado\n")
    except Exception as e:
        print(Fore.RED + f"Error al actualizar avatar: tu webhook quizas haiga sido eliminada o el link es incorrecto")

def enviar_mensaje():
    msg = input(Fore.YELLOW + "Mensaje -> " + Fore.RESET)
    try:
        requests.post(WEBHOOK, json={"content": msg})
        print(Fore.GREEN + "Mensaje enviado\n")
    except Exception as e:
        print(Fore.RED + f"Error al enviar mensaje: tu webhook quizas haiga sido eliminada o el link es incorrecto")

def enviar_spam():
    msg = input(Fore.YELLOW + "Enviar spam ->  " + Fore.RESET)
    print(Fore.CYAN + "\nEnviando spam...\n")
    for i in range(1,21):  # envia 20 mensajes por defecto
        try:
            requests.post(WEBHOOK, json={"content": msg})
            print(Fore.MAGENTA + f"[{i}/20] Enviado")
        except Exception as e:
            print(Fore.RED + f"[{i}/20] Error: tu webhook quizas haiga sido eliminada o el link es incorrecto")
        time.sleep(0)
    print(Fore.GREEN + "\nEl spam ha iniciado\n")

def eliminar_webhook():
    confirm = input(Fore.RED + "Esto eliminara la webhook permanentemente. Continuar y/n -> " + Fore.RESET).lower()
    if confirm == "y":
        try:
            res = requests.delete(WEBHOOK)
            if res.status_code == 204:
                print(Fore.GREEN + "Webhook eliminada correctamente")
                exit()
            else:
                print(Fore.RED + f"Error al eliminar webhook. Status: {res.status_code}")
        except Exception as e:
            print(Fore.RED + f"Error: tu webhook quizas haiga sido eliminada o el link es incorrecto")
    else:
        print(Fore.YELLOW + "Cancelado\n")

# ===== Menu =====
def menu():
    print(Fore.CYAN + Style.BRIGHT + "INFORMACION")
    print(Fore.GREEN + "[1]" + Fore.RESET + " Ver informacion de la webhook")
    print(Fore.MAGENTA + Style.BRIGHT + "- EDICION - ")
    print(Fore.GREEN + "[2]" + Fore.RESET + " Editar nombre")
    print(Fore.GREEN + "[3]" + Fore.RESET + " Editar avatar URL")
    print(Fore.YELLOW + Style.BRIGHT + "- USOS -")
    print(Fore.GREEN + "[4]" + Fore.RESET + " Enviar 1 mensaje")
    print(Fore.GREEN + "[5]" + Fore.RESET + " Enviar spam")
    print(Fore.RED + Style.BRIGHT + "- ELIMINAR -")
    print(Fore.RED + "[6]" + Fore.RESET + " Eliminar webhook")
    print(Fore.RED + "[7]" + Fore.RESET + " Salir\n")
    choice = input(Fore.CYAN + "Opcion -> " + Fore.RESET)
    return choice.strip()

# ===== Loop principal =====
while True:
    op = menu()
    if op == "1":
        ver_info()
    elif op == "2":
        editar_nombre()
    elif op == "3":
        editar_avatar()
    elif op == "4":
        enviar_mensaje()
    elif op == "5":
        enviar_spam()
    elif op == "6":
        eliminar_webhook()
    elif op == "7":
        print(Fore.RED + "Abandonando ...")
        break
    else:
        print(Fore.RED + "Opcion invalida\n")