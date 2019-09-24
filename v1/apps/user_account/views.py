from rest_framework import generics
from v1.apps.user_account.models import Profile
from v1.apps.user_account.permission import IsOwnerOrReadOnly


# Create your views here.
class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileCreateView(generics.CreateAPIView):
    serializer_class = ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )