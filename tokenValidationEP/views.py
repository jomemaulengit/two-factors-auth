import logging
import pymongo
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from django.http import HttpResponse
from TFAuth.utils import TFAuth
from bson.objectid import ObjectId
from bson.errors import InvalidId
from .validation import validation

logger = logging.getLogger()

@api_view(['POST'])
def validate(request):
    try:
        # =========REQUEST DATA
        request_id = ObjectId(request.data["UserId"])
        request_tkn = request.data['Token']
        # =========QUERY DATA
        persona = TFAuth.find({"UserId": request_id}).sort("CreateAt", pymongo.DESCENDING).limit(1)[0]
        persona_tkn=persona['Token']
        create_at=persona['CreateAt']
        duration=persona['Duration']
        # ==========VALIDATE REQUEST/QUERY
        is_valid=validation(request_tkn,persona_tkn,duration,create_at)
        logger.info(f'func: validate: {request_id} validado correctamente')
        return HttpResponse(f'{is_valid}')
    except KeyError as e:
        logger.error(f'func: catch_id: invalid dict key, expected "UserId" & "Token" ')
        return HttpResponse(f'invalid dict key')
    except ParseError as e:
        logger.error(f'func: catch_id: 400 Bad request')
        return HttpResponse(f'error 400 bad request')
    except InvalidId as e:
        logger.error(
            f'func: catch_id: el ObjectId no coincide con ninguna persona registrada')
        return HttpResponse(f'el ObjectId no coincide con ninguna persona registrada')
    except TypeError as e:
        logger.error(
            f'func: catch_id: ObjectId must be String or ObjectId instance')
        return HttpResponse(f'ObjectId must be String or ObjectId instance')
    except Exception as e:
        logger.error(f'func: validate: unexpected error of type: {type(e)}')
        return HttpResponse(e)
