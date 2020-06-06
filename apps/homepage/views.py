from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.response import Response
from apps.accounts.models import *
from drf_yasg.utils import swagger_auto_schema


class HomepageView(GenericAPIView):
    def get(self, request):
        data = {
            'about': AboutSerializer(About.objects.all(), many=True).data,
            'videos': VideoSerializer(Video.objects.all(), many=True).data,
            'statistics': StatisticsSerializer(Statistics.objects.all(), many=True).data,
            'faq': FAQSerializer(FAQ.objects.all(), many=True).data,
            'coming_soon': EventSerializer(Event.objects.all().filter(countdownable=True).order_by('date').first()).data,
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
    serializer_class = StaffTeamSerializer
    def get(self, request):
        data = {'teams': StaffTeamSerializer(StaffTeam.objects.all(), many=True).data}
        return Response(data)


