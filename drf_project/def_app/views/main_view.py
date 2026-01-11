from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import productserializers
from rest_framework import status

@api_view(["GET",'POST'])
def product_view(request):
    if request.method=='POST':
        serializer = productserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"product created","data":serializer.data},status=status.HTTP_201_CREATED)
        
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='GET':
        return Response()
       
        
        