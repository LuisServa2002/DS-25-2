#!/usr/bin/env python3
import os
import json
import shutil
import click

# ============================
# CONFIGURACIÓN CLI CON CLICK
# ============================

@click.command()
@click.option("--count", default=10, help="Cantidad de entornos a generar.")
@click.option("--prefix", default="app", help="Prefijo de los entornos (por defecto: app).")
@click.option("--port", default=8000, help="Puerto base inicial.")
def main(count, prefix, port):
    """
    Genera múltiples entornos Terraform (.tf.json) basados en una plantilla de módulo.
    Permite definir cantidad, prefijo y puerto base desde la CLI.
    """
    MODULE_DIR = "modules/simulated_app"
    OUT_DIR = "environments"

    # Limpiar entornos previos
    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)

    api_key = os.environ.get("API_KEY", None)
    if not api_key:
        print("Advertencia: No se encontró la variable de entorno API_KEY.")
    else:
        print("Clave API detectada (no se guardará en disco).")

    # Generar entornos
    for i in range(1, count + 1):
        name = f"{prefix}{i}"
        network = f"net{i}"

        # Ejemplo de dependencia: el tercero depende del segundo
        if name == f"{prefix}3":
            network = f"net2-peered"

        env = {"name": name, "network": network, "port": port + i}
        render_and_write(env, MODULE_DIR, OUT_DIR, api_key)

    print(f"\nGenerados {count} entornos en '{OUT_DIR}/'")

# ============================
# FUNCIÓN DE GENERACIÓN
# ============================

def render_and_write(env, MODULE_DIR, OUT_DIR, api_key):
    env_dir = os.path.join(OUT_DIR, env["name"])
    os.makedirs(env_dir, exist_ok=True)

    # Copiar definición base de variables
    shutil.copyfile(
        os.path.join(MODULE_DIR, "network.tf.json"),
        os.path.join(env_dir, "network.tf.json")
    )

    # Crear triggers
    triggers = {
        "name": env["name"],
        "network": env["network"],
        "port": env["port"]
    }

    if api_key:
        triggers["api_key_ref"] = "${var.api_key}"

    # Construir main.tf.json
    config = {
        "resource": [
            {
                "local_server": [
                    {
                        env["name"]: [
                            {
                                "triggers": triggers,
                                "provisioner": [
                                    {
                                        "local-exec": {
                                            "command": (
                                                f"echo 'Arrancando servidor "
                                                f"{env['name']} en red {env['network']} "
                                                f"por el puerto {env['port']}'"
                                            )
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

    # Guardar archivo
    with open(os.path.join(env_dir, "main.tf.json"), "w") as fp:
        json.dump(config, fp, sort_keys=True, indent=4)

    print(f"Entorno generado: {env['name']} (red: {env['network']}, puerto: {env['port']})")


if __name__ == "__main__":
    main()
