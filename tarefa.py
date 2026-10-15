# Importamos Faker para generar datos ficticios
from faker import Faker
# Importamos la librería random para selecciones aleatorias
import random

# Inicializamos el generador de datos falsos
fake = Faker()

# creamos el dicionario para almacenar los usuario
usuarios = {}

#Generamos una lista de códigos
codigos = list(range(1, 16))

# bucle que almacena en el dicionario datos de los usuarios por cada código
for codigo in codigos:
    usuarios[codigo] = {
        "nome": fake.name(),
        "dirección": fake.address(),
        "correo_electrónico": fake.email(),
        "teléfono": fake.phone_number(),
    }

# Muestro los usuarios con los datos ficticios creados
for codigo in usuarios:
    dato = usuarios[codigo]
    print(f"Código: {codigo}")
    print(f"Nome: {dato['nome']}")
    print(f"Dirección: {dato['dirección']}")
    print(f"Correo: {dato['correo_electrónico']}")
    print(f"Teléfono: {dato['teléfono']}")
    print(f"")

# Muestro el usuario afortunado
codigo_afortunado = random.choice(list(usuarios.keys()))  # elegir un código de la lista aleatorio
usuario_afortunado = usuarios[codigo_afortunado]  #recuperamos al usuario de ese código 
print(f"O usuario chamado {usuario_afortunado['nome']} foi o afortunado!") #mostramos el usuario elegido
