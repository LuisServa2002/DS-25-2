from composite import CompositeModule
import json
import os

# === Ejemplo de recursos Terraform === #
network_module = {
    "module": {
        "network": {
            "source": "./modules/network",
            "resource": {
                "null_resource": {
                    "net_a": {"triggers": {"name": "network-A"}}
                }
            }
        }
    }
}

app_module = {
    "module": {
        "app": {
            "source": "./modules/app",
            "resource": {
                "null_resource": {
                    "app_a": {"triggers": {"name": "app-A"}}
                }
            }
        }
    }
}

# === Construcción del Composite === #
root = CompositeModule()
root.add(network_module)
root.add(app_module)

# Exportar el módulo compuesto
merged = root.export()

# Crear carpeta terraform y guardar el JSON
os.makedirs("terraform", exist_ok=True)
with open("terraform/main_composite.tf.json", "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)

print("Archivo 'main_composite.tf.json' generado correctamente.")
print(json.dumps(merged, indent=2, ensure_ascii=False))
