from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.serializers import SelectionSerializer, SelectionCreateSerializer

from ads.permissions import IsSelectionOwner


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()
    default_serializer = SelectionSerializer
    serializer_classes = {
        'create': SelectionCreateSerializer,
    }

    default_permission = [AllowAny(), ]
    permissions_list = {"create": [IsAuthenticated()],
                        "update": [IsAuthenticated(), IsSelectionOwner()],
                        "partial_update": [IsAuthenticated(), ],
                        "destroy": [IsAuthenticated(), ],
                        }

    def get_my_permissions(self):
        return self.permissions_list.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)
