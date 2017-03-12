#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DavidMendezGuardado'

from bs4 import BeautifulSoup
import requests

URL = "http://blog.desdelinux.net/"

# Se Realiza peticion a la web
req = requests.get(URL)

# Comprobar que la peticion devuelva un StatusCode = 200
STATUS_CODE = req.status_code
if STATUS_CODE == 200:
    # Pasamos el contenido HTML de la web a un objeto
    html = BeautifulSoup(req.text, "html.parser")
    # Obtenemos todas las etiquetas en donde esta la informacion a obtener
    entradas = html.find_all('div', {'class': 'td_module_2'})
    # Recorremos todas las entradas para extraer la iformacion requerida
    for i, entrada in enumerate(entradas):
        titulo = entrada.find('h3', {'class': 'entry-title td-module-title'}).getText()
        autor = entrada.find('span', {'class': 'td-post-author-name'}).getText()

        # Imprimimos la informacion
        print "%d - %s | %s" % (i + 1, titulo, autor)
else:
    print "Status Code %d" % STATUS_CODE
