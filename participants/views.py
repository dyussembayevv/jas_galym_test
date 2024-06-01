from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Participant
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    top_participants = Participant.objects.order_by('-points')[:10]
    return render(request, 'index.html', {'top_participants': top_participants})


# Forms in views.py
class ChangeNameForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name']

class ChangePointsForm(forms.Form):
    points = forms.IntegerField(label='Add Points', min_value=1)


@login_required
def participant_detail(request, id):
    participant = get_object_or_404(Participant, id=id)

    if request.method == 'POST':
        if 'change_name' in request.POST:
            name_form = ChangeNameForm(request.POST, instance=participant)
            points_form = ChangePointsForm()
            if name_form.is_valid():
                name_form.save()
                return redirect('participant_detail', id=participant.id)
        elif 'change_points' in request.POST:
            name_form = ChangeNameForm(instance=participant)
            points_form = ChangePointsForm(request.POST)
            if points_form.is_valid():
                participant.points += points_form.cleaned_data['points']
                participant.save()
                return redirect('participant_detail', id=participant.id)
    else:
        name_form = ChangeNameForm(instance=participant)
        points_form = ChangePointsForm()

    return render(request, 'participant_detail.html', {
        'participant': participant,
        'name_form': name_form,
        'points_form': points_form
    })
'''

class ChangeNameForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name']

class ChangePointsForm(forms.Form):
    points = forms.IntegerField(label='Points', min_value=1)

@login_required
def participant_detail(request, id):
    participant = get_object_or_404(Participant, id=id)

    name_form = ChangeNameForm(instance=participant)
    add_points_form = ChangePointsForm()
    subtract_points_form = ChangePointsForm()

    if request.method == 'POST':
        if 'change_name' in request.POST:
            name_form = ChangeNameForm(request.POST, instance=participant)
            add_points_form = ChangePointsForm()
            subtract_points_form = ChangePointsForm()
            if name_form.is_valid():
                name_form.save()
                return redirect('participant_detail', id=participant.id)
        elif 'add_points' in request.POST:
            name_form = ChangeNameForm(instance=participant)
            add_points_form = ChangePointsForm(request.POST)
            subtract_points_form = ChangePointsForm()
            if add_points_form.is_valid():
                participant.points += add_points_form.cleaned_data['points']
                participant.save()
                return redirect('participant_detail', id=participant.id)
        elif 'subtract_points' in request.POST:
            name_form = ChangeNameForm(instance=participant)
            add_points_form = ChangePointsForm()
            subtract_points_form = ChangePointsForm(request.POST)
            if subtract_points_form.is_valid():
                participant.points -= subtract_points_form.cleaned_data['points']
                participant.save()
                return redirect('participant_detail', id=participant.id)

    return render(request, 'participant_detail.html', {
        'participant': participant,
        'name_form': name_form,
        'add_points_form': add_points_form,
        'subtract_points_form': subtract_points_form
    })
'''
