from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from .models import *
from rest_framework.serializers import ModelSerializer


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class StatisticsSerializer(ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class WinnerSerializer(ModelSerializer):
    class Meta:
        model = Winner
        fields = '__all__'


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class StaffTeamSerializer(ModelSerializer):
    class Meta:
        model = StaffTeam
        fields = '__all__'


class SponsorSerializer(ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class SocialSerializer(ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class FAQSerializer(ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class HomepageSerializer(ModelSerializer):

    class Meta:
        model = Homepage
        fields = '__all__'
        depth = 3



