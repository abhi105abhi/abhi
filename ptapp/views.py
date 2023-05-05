from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LeadForm, TutorForm
import telegram

def home(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save()
            send_telegram_message(lead, 'lead')
            return HttpResponseRedirect(reverse('home'))
    else:
        form = LeadForm()
    context = {'form': form}
    return render(request, 'home.html', context)

def tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            tutor = form.save()
            print(tutor.__dict__)
            send_telegram_message(tutor, 'tutor')
            return HttpResponseRedirect(reverse('tutor'))
    else:
        form = TutorForm()
    context = {'form': form}
    return render(request, 'tutor.html', context)


def send_telegram_message(data, data_type):
    bot_token = '6126864087:AAHff76skhhsD3sbuEtVAP7K51Ej3dedNoc'
    chat_id = '6041296700'
    message = f'New {data_type} submission:\n'
    for key, value in data.__dict__.items():
        if key == '_state':
            continue
        message += f'{key}: {value}\n'
    bot = telegram.Bot(token=bot_token)
    bot.sendMessage(chat_id=chat_id, text=message)
