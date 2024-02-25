from rest_framework import status, decorators
from rest_framework.response import Response
from ...model_builder import Fields


@decorators.api_view(["GET"])
def GetSupprotedFields (request) :
    try:
        data = Fields()
        return Response(data.get_supprted_fields(),status=status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)