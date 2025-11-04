"""
Patrón Prototype (Ejercicio 2.3 – Mutaciones avanzadas con local_file)

Permite clonar un recurso Terraform y modificarlo mediante un mutator
que añade un bloque `local_file` y un trigger adicional sin alterar el original.
"""

import copy
from typing import Dict, Any, Callable


class ResourcePrototype:
    """
    Prototipo de recurso Terraform que puede ser clonado y modificado
    de forma independiente, siguiendo el patrón Prototype.
    """

    def __init__(self, resource_dict: Dict[str, Any]) -> None:
        """Inicializa el prototipo con un recurso base."""
        self._resource_dict = resource_dict

    def clone(self, mutator: Callable[[Dict[str, Any]], None] | None = None) -> "ResourcePrototype":
        """
        Clona el recurso original aplicando una mutación opcional.

        Args:
            mutator: Función opcional que recibe el clon y puede modificarlo.

        Returns:
            Nuevo objeto `ResourcePrototype` que contiene el recurso clonado y mutado.
        """
        new_dict = copy.deepcopy(self._resource_dict)  # Copia profunda del recurso
        if mutator:
            mutator(new_dict)  # Aplica los cambios al clon
        return ResourcePrototype(new_dict)

    @property
    def data(self) -> Dict[str, Any]:
        """Devuelve el recurso actual (original o clonado)."""
        return self._resource_dict


# === Mutador solicitado === #

def add_welcome_file(block: Dict[str, Any]) -> None:
    """
    Añade un trigger de bienvenida al recurso null_resource
    y un nuevo bloque local_file para generar 'bienvenida.txt'.

    Args:
        block: Estructura de recurso a modificar.
    """
    # Accede al bloque del recurso null_resource
    null_res = block["resource"][0]["null_resource"][0]
    resource_name = next(iter(null_res.keys()))
    triggers = null_res[resource_name][0]["triggers"]

    # Añade trigger adicional
    triggers["welcome"] = "¡Hola!"

    # Añade nuevo bloque local_file
    block["resource"].append({
        "local_file": [{
            "welcome_txt": [{
                "content": "Bienvenido",
                "filename": "${path.module}/bienvenida.txt"
            }]
        }]
    })
