"""
Patrón Adapter
Convierte un bloque Terraform de tipo `null_resource` en un recurso simulado `mock_cloud_bucket`.
Permite reutilizar la estructura existente sin modificar la clase original.
"""

class MockBucketAdapter:
    def __init__(self, null_block: dict):
        """Recibe el bloque original tipo null_resource."""
        self.null = null_block

    def to_bucket(self) -> dict:
        """
        Convierte el bloque `null_resource` en `mock_cloud_bucket`,
        mapeando los triggers como parámetros del bucket.
        """
        # Navega correctamente por la estructura del recurso
        name = list(self.null["resource"][0]["null_resource"][0].keys())[0]
        triggers = self.null["resource"][0]["null_resource"][0][name][0]["triggers"]

        return {
            "resource": {
                "mock_cloud_bucket": {
                    name: {
                        "name": name,
                        **triggers
                    }
                }
            }
        }
