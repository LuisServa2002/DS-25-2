"""
Patrón Factory (Variación del Ejercicio 2.2)

Extiende la fábrica base `NullResourceFactory` para permitir definir un formato
de timestamp personalizado al crear recursos Terraform del tipo `null_resource`.
"""

from typing import Dict, Any
import uuid
from datetime import datetime


class NullResourceFactory:
    """
    Fábrica para crear bloques de recursos `null_resource` en formato Terraform JSON.
    Cada recurso incluye triggers personalizados y valores únicos para garantizar idempotencia.
    """

    @staticmethod
    def create(name: str, triggers: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """
        Crea un bloque de recurso Terraform tipo `null_resource` con triggers personalizados.

        Args:
            name: Nombre del recurso dentro del bloque.
            triggers: Diccionario de valores personalizados que activan recreación del recurso.
                      Si no se proporciona, se inicializa con un UUID y un timestamp ISO.

        Returns:
            Diccionario compatible con la estructura JSON de Terraform para null_resource.
        """
        triggers = triggers or {}

        # Agrega un trigger por defecto: UUID aleatorio para asegurar unicidad
        triggers.setdefault("factory_uuid", str(uuid.uuid4()))

        # Agrega un trigger con timestamp actual en formato ISO
        triggers.setdefault("timestamp", datetime.utcnow().isoformat())

        return {
            "resource": [{
                "null_resource": [{
                    name: [{
                        "triggers": triggers
                    }]
                }]
            }]
        }


class TimestampedNullResourceFactory(NullResourceFactory):
    """
    Subclase que permite especificar un formato de fecha personalizado para el timestamp.
    """

    @staticmethod
    def create(name: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> Dict[str, Any]:
        """
        Crea un bloque de recurso con un timestamp formateado según el formato especificado.

        Args:
            name: Nombre del recurso dentro del bloque.
            fmt: Formato de fecha (por defecto: "%Y-%m-%d %H:%M:%S").

        Returns:
            Diccionario compatible con la estructura JSON de Terraform.
        """
        triggers = {
            "factory_uuid": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().strftime(fmt)
        }

        return {
            "resource": [{
                "null_resource": [{
                    name: [{
                        "triggers": triggers
                    }]
                }]
            }]
        }
