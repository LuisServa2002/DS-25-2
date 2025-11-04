from prototype import ResourcePrototype, add_welcome_file
import json
import os

# Recurso base
base_resource = {
    "resource": [{
        "null_resource": [{
            "app_0": [{
                "triggers": {
                    "factory_uuid": "abcd-1234",
                    "timestamp": "2025-01-01T00:00:00Z"
                }
            }]
        }]
    }]
}

# Crear prototipo y clonar con el mutador
proto = ResourcePrototype(base_resource)
clone = proto.clone(add_welcome_file)

# Crear carpeta terraform si no existe
os.makedirs("terraform", exist_ok=True)

# Guardar el JSON final para Terraform
with open("terraform/main_clone.tf.json", "w", encoding="utf-8") as f:
    json.dump(clone.data, f, indent=2, ensure_ascii=False)

print("Archivo 'main_clone.tf.json' generado sin reemplazar el existente.")