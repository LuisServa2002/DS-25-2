"""
Patrón Composite (Ejercicio 2.4 – Submódulos con Composite)

Permite agrupar múltiples recursos o submódulos Terraform dentro de una
única jerarquía lógica. El método `export()` combina tanto bloques `resource`
como `module`, generando una estructura Terraform JSON válida.
"""

from typing import List, Dict, Any


class CompositeModule:
    """
    Clase que agrupa múltiples recursos o submódulos Terraform en una estructura unificada.
    """

    def __init__(self) -> None:
        """Inicializa la lista de elementos hijos (recursos o módulos)."""
        self.children: List[Dict[str, Any]] = []

    def add(self, resource_dict: Dict[str, Any]) -> None:
        """
        Agrega un diccionario Terraform como hijo (puede contener 'resource' o 'module').

        Args:
            resource_dict: Diccionario representando un recurso o submódulo Terraform.
        """
        self.children.append(resource_dict)

    def export(self) -> Dict[str, Any]:
        """Exporta el módulo compuesto como un diccionario de recursos Terraform."""
        result: Dict[str, Any] = {"resource": {}}
        
        for child in self.children:
            if "resource" in child:
                for resource_block in child["resource"]:
                    for resource_type, resources in resource_block.items():
                        if resource_type not in result["resource"]:
                            result["resource"][resource_type] = {}
                        for resource in resources:
                            for name, config in resource.items():
                                result["resource"][resource_type][name] = config
    
            elif "module" in child:
                if "module" not in result:
                    result["module"] = {}
                result["module"].update(child["module"])
    
        # Remove empty resource block if no resources were added
        if not result["resource"]:
            del result["resource"]
            
        return result if result else {}