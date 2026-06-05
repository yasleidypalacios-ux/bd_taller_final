import requests
from pymongo import MongoClient

# Conexión a MongoDB Atlas
MONGO_URI = "mongodb+srv://yasleidy:taller2026@cluster0.hdrwulj.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["taller4_db"]
coleccion = db["raw_data"]

# Limpiar colección
coleccion.drop()
print("Colección limpiada.")

# Llamada a la API con campos específicos
print("Descargando datos de la API...")
campos = "name,capital,region,subregion,population,area,languages"
response = requests.get(f"https://restcountries.com/v3.1/all?fields={campos}")
paises = response.json()

print(f"Países descargados: {len(paises)}")

# Insertar datos crudos en MongoDB
coleccion.insert_many(paises)
print(f"Datos insertados en MongoDB: {coleccion.count_documents({})} documentos.")

client.close()
print("¡Ingesta completada!")