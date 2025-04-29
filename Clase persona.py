
class Persona:
    especie: str = "Homo sapiens"
    def __init__(self, edad: int, nombre: str):
        self.edad = edad
        self.nombre = nombre
    def greet(self):
        print(f"La persona {self.nombre} te está saludando! (Dile hola >:c)")
    def is_older_than (self, persona: "Persona"):
        return (self.edad > persona.edad)
    
if __name__ == "__main__":
    persona_1 = Persona(edad = 42, nombre = "Juanito Alimaña")
    persona_2 = Persona(edad = 47, nombre = "Pedro Navaja")

    persona_1.greet()

    print(f"{persona_1.nombre} es mayor que {persona_2.nombre}"
          if persona_1.is_older_than(persona_2) else
          f"{persona_1.nombre} es menor que {persona_2.nombre}")