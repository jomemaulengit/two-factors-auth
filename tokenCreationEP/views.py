from django.http import HttpResponse
from bson.objectid import ObjectId
from bson.errors import InvalidId
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from .keygen import keygen
from TFAuth.utils import JSONEncoder, personas
from .sendEmail import Mail
import logging

logging.basicConfig(level=logging.DEBUG, filename='loggin.log',
                    format='%(asctime)s %(levelname)s:%(message)s')
logger = logging.getLogger()


@api_view(['POST'])
def catch_id(request):
    try:
        id = ObjectId(request.data["id"])
        doc = personas.find_one({"_id": id})
        document = JSONEncoder().encode(doc)
        key = keygen(id)
        isValidEmail = Mail(doc["email"], key)
        if isValidEmail:
            logger.info(
                f"func: catch_id: id:{id} correcto, email enviado a {doc['email']}")
            return HttpResponse(document)
        else:
            logger.error(
                f'el email registrado no es un recipiente valido (tal vez no existe)')
            return HttpResponse('error al enviar el email')
    except KeyError as e:
        logger.error(f'func: catch_id: invalid dict key, expected "id" ')
        return HttpResponse(f'invalid dict key')
    except InvalidId as e:
        logger.error(
            f'func: catch_id: el ObjectId no coincide con ninguna persona registrada')
        return HttpResponse(f'el ObjectId no coincide con ninguna persona registrada')
    except TypeError as e:
        logger.error(
            f'func: catch_id: ObjectId must be String or ObjectId instance')
        return HttpResponse(f'ObjectId must be String or ObjectId instance')
    except ParseError as e:
        logger.error(f'func: catch_id: 400 Bad request')
        return HttpResponse(f'error 400 bad request')
    except Exception as e:
        logger.error(f'func: catch_id: unexpected error of type: {type(e)}')
        return HttpResponse(f'unexpected error of type {type(e)}')
