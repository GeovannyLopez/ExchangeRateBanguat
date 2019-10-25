# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Configuracion API"),
			"items": [
				{
					"type": "doctype",
                    "label": _("Configuracion API"),
					"name": "Configuracion API",
					"description": _("Doctype de prueba")
				},
				{
					"type": "doctype",
					"label": _("Registro API"),
					"name": "Registro API",
					"description": _("Ejemplo encuesta"),
				}
			]
		}
	]