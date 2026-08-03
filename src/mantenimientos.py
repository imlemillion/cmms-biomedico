import os
import json
from enum import Enum
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
import uuid

class Prioridad(str, Enum): #convertir Enum a texto plano para guardar en JSON
    ALTA = "Alta"
    MEDIA = "Media"
    BAJA = "Baja"

class TipoMantenimiento(str, Enum):
    PREVENTIVO = "Preventivo"
    CORRECTIVO = "Correctivo"

class EstadoMantenimiento(str, Enum):
    PENDIENTE = "Pendiente"
    EN_PROCESO = "En proceso"
    RESUELTO = "Resuelto"

@dataclass
class Mantenimiento:
    equipo_id: str
    tipo: TipoMantenimiento
    mantenimiento_id: str = field(default_factory=lambda: str(uuid.uuid4())) #uuid4 de forma aleatoria
    prioridad: Prioridad = Prioridad.MEDIA
    estado: EstadoMantenimiento = EstadoMantenimiento.PENDIENTE
    fecha_programada: Optional[str] = None
    fecha_reporte: Optional[str] = None
    fecha_resolucion: Optional[str] = None
    tecnico_responsable: str = ""
    descripcion_falla: str = ""
    observaciones_tecnicas: str = ""

    def downtime_horas(self) -> Optional[float]:
        if self.fecha_reporte and self.fecha_resolucion:
            reporte = datetime.fromisoformat(self.fecha_reporte)
            resolucion = datetime.fromisoformat(self.fecha_resolucion)
            delta = resolucion - reporte
            return round(delta.total_seconds() /3600, 2)
        return None

    def esta_vencido(self, referencia: Optional[str] = None) -> bool:
        if self.tipo != TipoMantenimiento.PREVENTIVO or not self.fecha_programada:
            return False
        ref = datetime.fromisoformat(referencia) if referencia else datetime.now()
        programada = datetime.fromisoformat(self.fecha_programada)
        return programada < ref and self.estado != EstadoMantenimiento.RESUELTO

    def to_dict(self) -> dict:
        return {
            "mantenimiento_id": self.mantenimiento_id,
            "equipo_id": self.equipo_id,
            "tipo": self.tipo.value,
            "prioridad": self.prioridad.value,
            "estado": self.estado.value,
            "fecha_programada": self.fecha_programada,
            "fecha_reporte": self.fecha_reporte,
            "fecha_resolucion": self.fecha_resolucion,
            "tecnico_responsable": self.tecnico_responsable,
            "descripcion_falla": self.descripcion_falla,
            "observaciones_tecnicas": self.observaciones_tecnicas,
        }
    @staticmethod
    def from_dict(data: dict) -> "Mantenimiento":
        return Mantenimiento(
            mantenimiento_id=data["mantenimiento_id"],
            equipo_id=data["equipo_id"],
            tipo=TipoMantenimiento(data["tipo"]),
            prioridad=Prioridad(data["prioridad"]),
            estado=EstadoMantenimiento(data["estado"]),
            fecha_programada=data.get("fecha_programada"),
            fecha_reporte=data.get("fecha_reporte"),
            fecha_resolucion=data.get("fecha_resolucion"),
            tecnico_responsable=data.get("tecnico_responsable", ""),
            descripcion_falla=data.get("descripcion_falla", ""),
            observaciones_tecnicas=data.get("observaciones_tecnicas", ""),
        )

def guardar_mantenimientos(mantenimientos, nombre_archivo="../data/mantenimientos.json"):
    print(f"Guardando en: {os.getcwd()}")
    mantenimientos_dict = [m.to_dict() for m in mantenimientos]
    with open(nombre_archivo, "w") as archivo:
        json.dump(mantenimientos_dict, archivo, indent=8)
    print(f"\n Datos guardados en {nombre_archivo}")