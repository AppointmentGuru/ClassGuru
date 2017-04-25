from rest_framework import routers, serializers, viewsets
from .models import Class
from .serializers import ClassSerializer

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get_queryset(self):
        return Class.objects.all()


router = routers.DefaultRouter()
router.register(r'classes', ClassViewSet)
