from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from psycopg2.extras import DateRange

from booking.models import Booking
from hotel.models import Room


class BookingDetailView(generic.DetailView):
    model = Booking
    template_name = 'booking/detail.html'


class DetailView(generic.DetailView):
    def post(self, request):
        room_id = request.POST.get('room')
        start = request.POST.get('checkIn')
        end = request.POST.get('checkOut')
        if not start or not end:
            return HttpResponse()
        room = Room.objects.get(pk=room_id)
        Booking.objects.create(
            room=room,
            period=DateRange(start, end))
        return HttpResponse()
