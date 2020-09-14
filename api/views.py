from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics  # contains filters so spec subject belong to spec users
from rest_framework import viewsets
from rest_framework.exceptions import (ValidationError, PermissionDenied)
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import Subject, Topic
from api.serializers import SubjectSerializer, TopicSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    # means user must be logged in to system to create a subject
    permission_classes = (IsAuthenticated,)

    # convert data back and forth
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all().filter(
            owner = self.request.user
        )
        return queryset

    def create(self, request, *args, **kwargs):
        # check if the subject already exists for the current logged in user
        subject = Subject.objects.filter(
            name = request.data.get('name'),
            owner = request.user
        )
        if subject:
            msg = 'A subject with that name already exists'
            raise ValidationError(msg)
        # create comes from ModelViewSet
        # need to overwrite the create method that comes from ModelViewSet
        return super().create(request)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def destroy(self, request, *args, **kwargs):  # perform destroy asks before deleting
        # get subject from URL
        subject = Subject.objects.get(pk = self.kwargs["pk"])
        # if subject doesn't belong to owner, then user is not allowed to delete subject
        if not request.user == subject.owner:
            # raise an error message
            raise PermissionDenied("You cannot delete this subject")
        super().destroy(request, *args, **kwargs)
        return Response(
            {
                'message': f'{subject} has been deleted',
                'status': status.HTTP_200_OK
            }
        )
      
# allows us to create a list at the same time (don't need list, retrieve, patch, update, etc. methods)
class SubjectTopic(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TopicSerializer

    def get_queryset(self):
        # print(self.kwargs.get("subject_pk"))
        # subject_pk from URL
        # check if pk is in URL
        if self.kwargs.get("subject_pk"):
            # if it is in URL, get the key
            subject = Subject.objects.get(pk = self.kwargs["subject_pk"])
            queryset = Topic.objects.filter(
                owner = self.request.user,
                subject = subject,
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class SingleSubjectTopic(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TopicSerializer

    def get_queryset(self):
        # if id for subject & id for topic from URL both match database entries
        if self.kwargs.get("subject_pk") and self.kwargs.get("pk"):
            subject = Subject.objects.get(pk = self.kwargs["subject_pk"])
            queryset = Topic.objects.filter(
                pk = self.kwargs["pk"],
                owner = self.request.user,
                subject = subject,
            )
            return queryset


class TopicViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TopicSerializer

    def get_queryset(self):
        queryset = Topic.objects.all().filter(
            owner = self.request.user
        )
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Only logged in users with accounts can create a topic"
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def update(self, request, *args, **kwargs):
        topic = Topic.objects.get(pk = self.kwargs["pk"])
        if not request.user == topic.owner:
            raise PermissionDenied(
                "You have no permissions to edit this topic"
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        topic = Topic.objects.get(pk = self.kwargs["pk"])
        if not request.user == topic.owner:
            raise PermissionDenied(
                "You have no permissions to delete this topic"
            )
        super().destroy(request, *args, **kwargs)
        return Response(
            {
                "message": f'{topic} has been deleted',
                "status": status.HTTP_200_OK
            }
        )

