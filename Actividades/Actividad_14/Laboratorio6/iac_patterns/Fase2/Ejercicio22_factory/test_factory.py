from factory import NullResourceFactory, TimestampedNullResourceFactory
import json

# Crear recurso con la fábrica base
base = NullResourceFactory.create("base_resource")
print("Recurso base:")
print(json.dumps(base, indent=2), "\n")

# Crear recurso con formato personalizado (YYYYMMDD-HHMMSS)
custom = TimestampedNullResourceFactory.create("custom_resource", "%Y%m%d-%H%M%S")
print("Recurso con formato personalizado:")
print(json.dumps(custom, indent=2), "\n")

# Validaciones básicas
assert "resource" in custom
assert "timestamp" in custom["resource"][0]["null_resource"][0]["custom_resource"][0]["triggers"]

print("Prueba exitosa - TimestampedNullResourceFactory genera correctamente el timestamp.")
