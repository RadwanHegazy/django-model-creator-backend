from rest_framework import status, decorators
from rest_framework.response import Response
from ..serializers import ModelSerailizer


@decorators.api_view(["POST"])
def CreateModel (request) :
    try:
        data = request.data
        serializer = ModelSerailizer(data=data)
        if serializer.is_valid() : 
            return Response(serializer.generate_model(),status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)