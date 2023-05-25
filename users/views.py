from rest_framework import mixins, generics, permissions

from users.models import UserProfile, Client
from users.serializers import UserProfileSerializer, ClientSerializer


class UserProfileCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientRetrieveUpdateDeleteView(mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     generics.GenericAPIView):
    queryset = Client.objects.all()
    lookup_field = 'username'
    serializer_class = ClientSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ClientListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
