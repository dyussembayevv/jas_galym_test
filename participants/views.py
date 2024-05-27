from django.shortcuts import render, get_object_or_404
from .models import Participant
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    top_participants = Participant.objects.order_by('-points')[:10]
    return render(request, 'index.html', {'top_participants': top_participants})


@login_required
def participant_detail(request, id):
    participant = get_object_or_404(Participant, pk=id)

    if request.method == 'POST':
        participant.name = request.POST.get('name', participant.name)
        participant.points = request.POST.get('points', participant.points)
        participant.save()

    return render(request, 'participant_detail.html', {'participant': participant})
