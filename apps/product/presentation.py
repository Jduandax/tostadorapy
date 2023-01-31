from .serializers import PresentationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Presentation
from rest_framework import status


class PresentationList(APIView):
    def get(self, request):
        presentation = Presentation.objects.all()
        presentation = PresentationSerializer(presentation, many=True).data
        return Response(presentation)

    # Creacion de presentaciones

    def post(self, request):
        presentation = PresentationSerializer(data=request.data)
        if presentation.is_valid():
            presentation.save()
            return Response(presentation.data, status=status.HTTP_200_OK)
        return Response(presentation.errors, status=status.HTTP_400_BAD_REQUEST)


class EditPresentation(APIView):
    def get(self, request, pk):
        presentation = Presentation.objects.get(pk=pk)
        presentation=PresentationSerializer(presentation,data=request.data)
        if presentation.is_valid():
            presentation.save()
            return Response(presentation.data)
        return Response(presentation.errors)
