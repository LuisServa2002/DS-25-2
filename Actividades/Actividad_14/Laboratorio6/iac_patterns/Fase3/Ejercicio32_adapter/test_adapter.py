from iac_patterns.Fase2.Ejercicio22_factory.factory import NullResourceFactory
from iac_patterns.Fase3.Ejercicio32_adapter.adapter import MockBucketAdapter
import json

# Crear un bloque base null_resource usando la fábrica
base = NullResourceFactory.create("demo_bucket")

# Adaptar a un bucket simulado
adapter = MockBucketAdapter(base)
bucket = adapter.to_bucket()

# Mostrar resultado formateado
print(json.dumps(bucket, indent=2))

# Validación simple
assert "mock_cloud_bucket" in bucket["resource"], "El adapter no generó el recurso esperado"
print("Prueba exitosa - Adapter transformó correctamente el recurso.")
