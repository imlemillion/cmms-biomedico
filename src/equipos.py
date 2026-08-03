# Registro de estado de equipos biomédicos
# Autor: Lemillion
# Descripción: Programa que registra el estado operativode equipos médicos y genera un resumen porcentual.

import os
import json
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class Criticidad (str, Enum):
    ALTA = "Alta"
    MEDIA = "Media"
    BAJA = "Baja"

@dataclass
class Equipo:
    nombre: str
    serie: str
    estado: str
    criticidad: Optional[Criticidad] = None
    criticidad_justificacion: str = ""
    proximo_mantenimiento: Optional[str] = None

    def to_dict(self) -> dict: #convertir objeto a texto plano para JSON
        return {
            "nombre": self.nombre,
            "serie": self.serie,
            "estado": self.estado,
            "criticidad": self.criticidad.value if self.criticidad else None, #expresion condicional o ternaria if/else en una sola linea
            "criticidad_justificacion": self.criticidad_justificacion,
            "proximo_mantenimiento": self.proximo_mantenimiento,
        }
    @staticmethod
    def from_dict(data: dict) -> "Equipo":
        return Equipo(
            nombre=data["nombre"],
            serie=data["serie"],
            estado=data["estado"],
            criticidad=Criticidad(data["criticidad"]) if data.get("criticidad") else None,
            criticidad_justificacion=data.get("criticidad_justificacion", ""),
            proximo_mantenimiento=data.get("proximo_mantenimiento"),
        )

def saludar(nombre_hospital):
    print(f"=== BIENVENIDO - {nombre_hospital} ====\n")
    print(f"==== PROGRAMA DE REGISTRO DE EQUIPOS BIOMÉDICOS ===\n")

def cargar_datos(nombre_archivo="../data/equipos.json"):
    try:
        with open (nombre_archivo, "r") as archivo:
            equipos_dict = json.load(archivo) #conversion de json a python
            equipos = [Equipo.from_dict(e) for e in equipos_dict]
            print(f"Se cargaron {len(equipos)} equipos registrados. \n")
            return equipos
    except FileNotFoundError:
        return []

def registrar_equipos():
    equipos = []
    print("INGRESE CADA EQUIPO Y SU NÚMERO DE SERIE (SN). PRESIONE ENTER PARA TERMINAR.\n")
    while True:
        nombre = input("Nombre del equipo: ")
        if nombre == "":
            break
        serie = input("numero de serie: ")
        while True:
            estado = input(f"¿El {nombre} (SN: {serie}) está operativo? (si/no): ")
            if estado.lower() ==  "si" or estado.lower() == "no":
                break
            print("Por favor escriba ´si´ o ´no´. ")
        equipos.append(Equipo(
            nombre=nombre,
            serie=serie,
            estado=estado.lower()
        ))
        print(f" {nombre} está registrado.\n")
    return equipos

def mostrar_resumen(equipos):
    total = len(equipos)
    operativos = [e for e in equipos if e.estado == "si"]     #el estado ES IGUAL (==) a "si"
    mantenimiento = [e for e in equipos if e.estado != "si"] #el estado ES DIFERENTE != a "si"
    
    print(f"\n--- RESUMEN ---")
    print(f"\n Equipos operativos: {len(operativos)} ({len(operativos)/total*100:.1f}%)")
    for e in operativos:
        print(f"      - {e.nombre} - S/N: {e.serie}")
    
    print(f"\n Equipos que requieren mantenimiento: {len(mantenimiento)} ({len(mantenimiento)/total*100:.1f}%)")
    for e in mantenimiento:
        print(f"      - {e.nombre} - S/N: {e.serie}")

def guardar_datos(equipos, nombre_archivo="../data/equipos.json"):
    print(f"Guardando en: {os.getcwd()}")
    equipos_dict = [e.to_dict() for e in equipos] #list comprehension para converir a diccionario
    with open(nombre_archivo, "w") as archivo:
        json.dump(equipos_dict, archivo, indent=8)                 #conversión de python a json
    print(f"\n Datos guardados en {nombre_archivo}")

#software architecture
if __name__ == "__main__":
    saludar("CMQ MORENO")
    
    respuesta = input("¿Desea cargar los equipos registrados anteriormente? (si/no): ")
    if respuesta.lower() == "si":
        equipos = cargar_datos()
    else:
        equipos = []
        
    equipos += registrar_equipos()        # equipos = equipos + registrar_equipos() (los anteriores más los nuevos). Todos juntos en una sola lista.
    mostrar_resumen(equipos)
    guardar_datos(equipos)