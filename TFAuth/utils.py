from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,ObjectId):
            return str(o)
        return json.JSONEncoder.default(self,o)

client = MongoClient(host="127.0.0.1", port=int(
    27017))
db = client["susulan"]
personas = db["persona"]
TFAuth = db["config_doble_validacion"]

def insert(document,collection):
    collection.insert_one(document)










# {
#     "rut":"20.237.701-8",
#     "nombre":"guillermo",
#     "ape_paterno":"maulen",
#     "ape_materno":"adasme",
#     "email":"maulenadasmeguillermo@gmail.com",
#     "direccion":"chalaco 177",
#     "ubicacion_gps":["12.76.456","12.123.234"],
# }
