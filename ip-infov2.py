#
# CREATED BY: JERRYFS-BIT
#

import urllib.request
import shodan
import sys
from ipapi import location
from colorama import Fore
from os import system, name
from pyfiglet import figlet_format

API_KEY = "uNtSN7XpWeLTFBX7Tf6lm22XFAB0bp60"
api = shodan.Shodan(API_KEY)


def Cscreen():
    if name == "posix":
        system("clear")
    else:
        system("cls")


def SearchMYIP():
    lista = "0123456789."
    ip = ""
    dato = urllib.request.urlopen("http://checkip.dyndns.org").read()
    for x in str(dato):
        if x in lista:
            ip += x
    return str(ip)


def searchIP(addr_IP):
    ip = location(addr_IP)
    host = api.host(addr_IP)

    url = "http://ip-api.com/json/" + addr_IP + "?fields=city"
    req_city = urllib.request.urlopen(url)
    city = str(req_city.read()).replace("'", "").replace(
        '"', "").replace("{", "").replace("}", "").replace("bcity:", "")

    print(Fore.WHITE + figlet_format('IP-INFO V2') + Fore.RESET)
    print(Fore.YELLOW + "CREATED BY: JerryFS-bit <-> https://github.com/JerryFS-bit" + Fore.RESET)

    print('-----------------------------------------------------------------------------------')
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Direccion IP      : {}'.format(ip['ip']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Version IP        : {}'.format(ip['version']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] ASN               : {}'.format(ip['asn']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] ORG               : {}'.format(ip['org']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] ISP               : {}'.format(host['isp']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Latitud           : {}'.format(ip['latitude']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Longitud          : {}'.format(ip['longitude']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Zona Horaria      : {}'.format(ip['timezone']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Capital de Pais   : {}'.format(ip['country_capital']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Pais              : {}'.format(ip['country_name']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Codigo de Pais    : {}'.format(ip['country_code']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Ciudad            : {}'.format(city))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET +
          '] Codigo de llamada : {}'.format(ip['country_calling_code']))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET + '] Dominios          : {}'.format(
        str(host['domains']).replace("['", "").replace("']", "")))
    print(' [' + Fore.GREEN + 'Ok' + Fore.RESET + '] Nombre de Host    : {}'.format(
        str(host['hostnames']).replace("['", "").replace("']", "")))
    print('-----------------------------------------------------------------------------------')


try:
    if len(sys.argv) == 1:
        print(' [' + Fore.YELLOW + 'ERROR' + Fore.RESET +
              '] Es necesario un argumento! ->> Ejemplo: [ip-infov2.py A.B.C.D], [ip-infov2.py myip]')
    else:
        if (sys.argv[1] == 'myip'):
            IP = SearchMYIP()
            searchIP(IP)
        else:
            IP = sys.argv[1]
            Cscreen()
            searchIP(IP)
except (shodan.APIError):
    if shodan.APIError:
        print(' [' + Fore.YELLOW + 'ALERT' + Fore.RESET +
              '] No se encuentra informacion disponible para esta direccion IP !')
