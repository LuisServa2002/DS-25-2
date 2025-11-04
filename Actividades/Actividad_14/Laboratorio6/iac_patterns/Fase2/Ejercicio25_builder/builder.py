"""
Patrón Builder (Ejercicio 2.5 – Builder personalizado)

Permite construir jerarquías Terraform modulares combinando Factory, Prototype y Composite.
Incluye el método `build_group` que genera submódulos con múltiples recursos clonados.
"""

from typing import Dict, Any
import os
import json

# Relative imports from sibling packages
from ..Ejercicio22_factory.factory import NullResourceFactory
from ..Ejercicio24_composite.composite import CompositeModule
from ..Ejercicio23_prototype.prototype import ResourcePrototype

class InfrastructureBuilder:
    """Builder fluido que combina los patrones Factory, Prototype y Composite para crear módulos Terraform."""

    def __init__(self, env_name: str) -> None:
        """Inicializa el builder con un nombre de entorno y una instancia de módulo compuesto."""
        self.env_name = env_name
        self.module = CompositeModule()

    # === Método base existente ===

    def build_null_fleet(self, count: int = 5) -> "InfrastructureBuilder":
        """
        Construye una flota de `null_resource` clonados a partir de un prototipo base.
        Cada recurso tiene un trigger identificador con el índice correspondiente.
        """
        base_proto = ResourcePrototype(NullResourceFactory.create("placeholder"))

        for i in range(count):
            def mutator(d: Dict[str, Any], idx=i) -> None:
                res_block = d["resource"][0]["null_resource"][0]
                original_name = next(iter(res_block.keys()))
                new_name = f"{original_name}_{idx}"
                res_block[new_name] = res_block.pop(original_name)
                res_block[new_name][0]["triggers"]["index"] = idx

            clone = base_proto.clone(mutator).data
            self.module.add(clone)

        return self

    # === Nuevo método solicitado ===
    def build_group(self, name: str, size: int) -> "InfrastructureBuilder":
        base = NullResourceFactory.create(name)
        proto = ResourcePrototype(base)
        group = CompositeModule()
    
        for i in range(size):
            def mut(block: Dict[str, Any], idx=i) -> None:
                print(f"Debug - Block structure: {json.dumps(block, indent=2)}")  # Add this line
                res_block = block["resource"][0]["null_resource"][0]  # Fix: Access list indices
                original_name = next(iter(res_block.keys()))
                new_name = f"{name}_{idx}"
                res_block[new_name] = res_block.pop(original_name)
                
            group.add(proto.clone(mut).data)
    
        self.module.add({"module": {name: group.export()}})
        return self    

    # === Método adicional existente ===

    def add_custom_resource(self, name: str, triggers: Dict[str, Any]) -> "InfrastructureBuilder":
        """Agrega un recurso null personalizado al módulo compuesto."""
        self.module.add(NullResourceFactory.create(name, triggers))
        return self

    # === Método final de exportación ===

    def export(self, path: str) -> None:
        """Exporta la configuración generada a un archivo JSON Terraform válido."""
        data = self.module.export()
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        print(f"[Builder] Terraform JSON escrito en: {path}")
