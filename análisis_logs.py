#leer archivos logs simulados
#detectar intentos fallidos
#extraer IP de intentos sospechosos


import re
from collections import defaultdict

RUTA_LOG = "auth.log"

regex_fallo = r"Failed password .* from (\d+\.\d+\.\d+\.\d+)"

intentos_por_ip = defaultdict(int)

try:
	with open(RUTA_LOG, "r") as archivo:
    	for linea in archivo:
            match = re.search(regex_fallo, linea)
            if match:
                ip = match.group(1)
                intentos_por_ip[ip] += 1
                
                
	if intentos_por_ip:
        print("Intentos fallidos derectados:\n")
        for ip, count in intentos_por_ip.items():
            print(f"IP: {ip} - {count} intentos fallidos")
        
    else:
    	print("No se detectaron intentos dacceso fallidos.")
        
except FileNotFoundError:
    print(f"ARCHIVO NO ENCONTRADO: {RUTA_LOG}")
    
    
    
