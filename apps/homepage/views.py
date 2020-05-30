from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.response import Response


class HomepageView(GenericAPIView):
    def get(self, request):
        # TODO: update stats from other models when created
        data = {
            'about': AboutSerializer(About.objects.all(), many=True).data,
            'statistics': StatisticsSerializer(Statistics.objects.all(), many=True).data,
            'events': EventSerializer(Event.objects.all(), many=True).data,
            'winners': WinnerSerializer(Winner.objects.all(), many=True).data,
            'staffs': StaffSerializer(Staff.objects.all().order_by('?')[:5], many=True).data,
            'sponsors': SponsorSerializer(Sponsor.objects.all().order_by('sponsor_class'), many=True).data,
            'quotes': QuoteSerializer(Quote.objects.all().order_by('?')[:5], many=True).data,
            'socials': SocialSerializer(Social.objects.all(), many=True).data
        }
        return Response(data)


class StaffsView(GenericAPIView):
    def get(self, request):
        data = {
            'staffs': StaffSerializer(Staff.objects.all(), many=True).data
        }
        return Response(data)
