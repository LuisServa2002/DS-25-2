"""
Patrón Singleton (Extensión del Ejercicio 2.1)

Asegura que una clase tenga una única instancia global, compartida en todo el sistema.
Esta versión incluye el método `reset()` que limpia las configuraciones sin alterar
la marca de creación (`created_at`). Además, la implementación es segura para hilos
(thread-safe).
"""

import threading
from typing import Any, Dict
from datetime import datetime, timezone


class SingletonMeta(type):
    """
    Metaclase Singleton segura para hilos (thread-safe).

    Controla que todas las clases que la utilicen compartan una única instancia global.
    Utiliza un candado (Lock) para prevenir condiciones de carrera en entornos concurrentes.
    """

    _instances: Dict[type, "ConfigSingleton"] = {}
    _lock: threading.Lock = threading.Lock()  # Controla el acceso concurrente

    def __call__(cls, *args, **kwargs):
        """
        Controla la creación de instancias: solo permite una única instancia por clase.
        Si ya existe, devuelve la existente. Si no, la crea protegida por un lock.
        """
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigSingleton(metaclass=SingletonMeta):
    """
    Clase Singleton que actúa como contenedor de configuración global.
    Todas las clases del sistema pueden consultar y modificar esta configuración compartida.
    """

    def __init__(self, env_name: str = "default") -> None:
        """
        Inicializa la configuración con un nombre de entorno y un timestamp de creación.

        Args:
            env_name: nombre del entorno o configuración (por defecto: "default").
        """
        self.env_name = env_name
        self.created_at = datetime.now(tz=timezone.utc).isoformat()  # Fecha de creación
        self.settings: Dict[str, Any] = {}  # Diccionario para guardar claves y valores

    def set(self, key: str, value: Any) -> None:
        """
        Establece un valor en la configuración global.

        Args:
            key: clave de configuración.
            value: valor asociado.
        """
        self.settings[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """
        Recupera un valor de la configuración global.

        Args:
            key: clave a consultar.
            default: valor por defecto si no existe la clave.

        Returns:
            Valor asociado o valor por defecto.
        """
        return self.settings.get(key, default)

    def reset(self) -> None:
        """
        Limpia todas las configuraciones del diccionario 'settings'
        sin alterar el nombre del entorno ni la marca de creación.
        """
        self.settings.clear()

    def __repr__(self) -> str:
        """
        Representación legible del estado actual de la configuración.
        """
        return f"<ConfigSingleton env='{self.env_name}' created_at='{self.created_at}' settings={self.settings}>"
