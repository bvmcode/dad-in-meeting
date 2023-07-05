from django.shortcuts import render
from .models import Meeting


def in_meeting(request):
    meeting = Meeting.objects.get()
    if meeting.meeting:
        return render(request, "in_meeting.html")
    return render(request, "not_in_meeting.html")
