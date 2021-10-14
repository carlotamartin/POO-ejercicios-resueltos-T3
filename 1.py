class Animal:
    def __init__(self, age = "0", name = "Godzilla"):
        '''constructor of an animal
        :param age: age of the animal: By default -> 0
        :param name: name of the animal. By Default: Godzilla
        :returns an instance of the Animal Class (One animal)
        '''
    # Todos estos atributos son públicos

    self.age = age # public attribute
    self.name = name # public attribute
    self.vivo = True
    Animal.numAnimales +=1
    def saluda():
        print('Hola')

    def mostrarNombre(self):
        print(self.nombre)
        def mostrarEdad(self):
            print(self.edad)

    def saluda(self, saludo='Hola', receptor = 'nuevo amigo'):
        print(saludo + " " + receptor)


    @staticmethod
    def add(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return " ".join((a, b))
        else:
            raise TypeError

    def mostrarNombre(self):
        print(self.nombre)
    def mostrarEdad(self):
        print(self.edad)