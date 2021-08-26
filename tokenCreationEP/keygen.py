from datetime import datetime
from random import randint
from TFAuth.utils import insert,TFAuth

def keygen(id):
    token={
        "UserId":id,
        "Token": randint(1000,9999),
        "CreateAt":datetime.now(),
        "Duration":120
    }
    try:
        insert(token,TFAuth)
        return token["Token"]
    except:
        return print("hubo un error erroneo")

