#!/usr/bin/env python3
import json
import os

def read_cfg(cfg_path):
    """Lee un archivo config.cfg y devuelve un diccionario."""
    cfg = {}
    with open(cfg_path) as f:
        for line in f:
            if "=" in line:
                key, val = line.strip().split("=", 1)
                cfg[key.strip()] = val.strip()
    return cfg

def main():
    legacy_dir = "legacy"
    cfg_path = os.path.join(legacy_dir, "config.cfg")
    run_path = os.path.join(legacy_dir, "run.sh")

    # Validar existencia
    if not os.path.exists(cfg_path) or not os.path.exists(run_path):
        print("No se encontró config.cfg o run.sh en el directorio legacy/")
        return

    config = read_cfg(cfg_path)
    port = int(config.get("PORT", 8080))

    # === Generar network.tf.json ===
    network = {
        "variable": [
            {
                "port": [
                    {
                        "type": "number",
                        "default": port,
                        "description": "Puerto del servicio legacy"
                    }
                ]
            }
        ]
    }

    with open("network.tf.json", "w") as f:
        json.dump(network, f, indent=4)
    print("Generado network.tf.json")

    # === Generar main.tf.json ===
    main = {
        "resource": {
            "local_server": {
                "legacy_app": {
                    "triggers": {
                        "port": port,
                        "script": run_path
                    }
                }
            }
        }
    }

    with open("main.tf.json", "w") as f:
        json.dump(main, f, indent=4)
    print("Generado main.tf.json")

    print("Migración completada: Infraestructura declarada con Terraform.")

if __name__ == "__main__":
    main()
