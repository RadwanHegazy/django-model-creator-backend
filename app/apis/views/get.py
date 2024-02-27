from rest_framework import status, decorators
from rest_framework.response import Response
from ...model_builder import Fields
from ...models import UModel

@decorators.api_view(["GET"])
def GetSupprotedFields (request) :
    try:
        data = Fields()
        return Response(data.get_supprted_fields(),status=status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@decorators.api_view(["GET"])
def ViewDjModel (request, model_id) : 
    try :
        try:
            model = UModel.objects.get(id=model_id)
        except UModel.DoesNotExist :
            return Response({
                'message' : "model not found"
            },status=status.HTTP_404_NOT_FOUND)

        data = {
            'id' : str(model.id),
            'body' : model.body
        }

        return Response(data,status=status.HTTP_200_OK)

    except Exception as error :
        return Response({
            'message' : f"an error accoured : {error}"
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)