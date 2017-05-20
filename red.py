#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import commands
import os

# Scritp aviso ip no autorizadas con conexion establecida en receptor, realizado por www.linuxzone.online
# Para ejecutar el script use python /ubicacionscript/red.py
# Introduce las ips conocidas que desees marcar como autorizadas, ejemplo:
#ip_autorizadas = ['192.168.1.45','88.2.82.201']
ip_autorizadas = []
 
conexiones=commands.getoutput("netstat -ntu | grep ESTAB | awk '{print $5}' |sed -e 's/::ffff://'| cut -d: -f1 | sort") 
 
conexiones = conexiones.split('\n')
texto = ''

for linea in conexiones:
    if not linea in ip_autorizadas:
        texto+="Acceso no Autorizado = "+linea+"\n"
    		
#En xxxx sustituir por el chat_id de telegram, En yyyy sustituir por el token key de telegram de vuestro bot-	
if texto:
    exitCode =  os.system('/usr/bin/curl --silent --output /dev/null --data-urlencode "chat_id=xxxx" --data-urlencode "text=%s" "https://api.telegram.org/botyyyy/sendMessage" &' % (texto))
