from django.shortcuts import render
from drf_yasg import openapi
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from .serializers import *
from rest_framework.response import Response
from apps.accounts.models import *
from drf_yasg.utils import swagger_auto_schema, swagger_serializer_method


class HomepageView(GenericAPIView):
    serializer_class = [FAQSerializer, AboutSerializer]

    @swagger_auto_schema(
        operation_description="Returns all needed Inf. for Homepage",
        responses={200: openapi.Response(description="Homepage is not the response and it is just a dictionary",
                                         schema=HomepageSerializer)},
        tags=['Homepage'],
    )
    def get(self, request):
        data = {
            'about': AboutSerializer(About.objects.all(), many=True).data,
            'videos': VideoSerializer(Video.objects.all(), many=True).data,
            'statistics': StatisticsSerializer(Statistics.objects.all(), many=True).data,
            'faq': FAQSerializer(FAQ.objects.all(), many=True).data,
            'coming_soon': EventSerializer(
                Event.objects.all().filter(countdownable=True).order_by('date').first()).data,
            'events': EventSerializer(Event.objects.all().order_by('date'), many=True).data,
            'winners': WinnerSerializer(Winner.objects.all(), many=True).data,
            'staffs': StaffSerializer(Staff.objects.all().order_by('?')[:5], many=True).data,
            'sponsors': SponsorSerializer(Sponsor.objects.all().order_by('sponsor_class'), many=True).data,
            'quotes': QuoteSerializer(Quote.objects.all().order_by('?')[:5], many=True).data,
            'socials': SocialSerializer(Social.objects.all(), many=True).data,

            'register_count': Profile.objects.count(),
            # TODO: Add Team and pre
            # 'team_count': Team.objects.count(),
            # 'pre_register_count': PreReg.objects.count(),
        }
        return Response(data)


class StaffsView(GenericAPIView):

    def get_queryset(self):
        return StaffTeam.objects.all()

    @swagger_auto_schema(
        operation_description="Returns all Staffs divided by their teams",
        responses={200: StaffTeamSerializer(many=True)},
        tags=['Homepage'],
    )
    def get(self, request):
        return Response(StaffTeamSerializer(self.get_queryset(), many=True).data)

