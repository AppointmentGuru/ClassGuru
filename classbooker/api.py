from rest_framework import routers, serializers, viewsets
from .models import Class
from .serializers import ClassSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


router = routers.DefaultRouter()
router.register(r'classes', ClassViewSet)
