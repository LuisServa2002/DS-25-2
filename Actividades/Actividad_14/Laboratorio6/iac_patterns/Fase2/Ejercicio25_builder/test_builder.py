import os
import sys
import json

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from iac_patterns.Fase2.Ejercicio25_builder.builder import InfrastructureBuilder

def main():
    # Create builder instance
    builder = InfrastructureBuilder(env_name="dev")

    # Build group of 3 resources under "app" submodule
    builder.build_group("app", 3)

    # Export result
    os.makedirs("terraform", exist_ok=True)
    builder.export("terraform/main_builder.tf.json")

    # Load and show content
    with open("terraform/main_builder.tf.json", "r") as f:
        data = json.load(f)

    print(json.dumps(data, indent=2))

    # Validation: should have module -> app -> resource structure
    assert "module" in data
    assert "app" in data["module"]
    assert "resource" in data["module"]["app"]
    print("Prueba exitosa - Estructura 'module -> app -> resource' generada correctamente.")

if __name__ == "__main__":
    main()