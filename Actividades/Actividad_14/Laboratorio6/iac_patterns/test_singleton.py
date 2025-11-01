from singleton import ConfigSingleton

# Se crea una instancia inicial
c1 = ConfigSingleton("dev")
created = c1.created_at
c1.set("timeout", 30)

# Se limpia la configuración
c1.reset()

assert c1.settings == {}
assert c1.created_at == created

# Se comprueba unicidad
c2 = ConfigSingleton("prod")
assert c1 is c2  # Mismo objeto
print("Prueba exitosa - Singleton y reset() funcionan correctamente.")
