from django.shortcuts import render
from django.contrib.auth.decorators import login_required

NAME_ORGANIZATION = 'СБТ'


# Create your views here.
@login_required
def index(request):
    context = {
        'title': f'Учебный портал {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'info/index.html', context=context)


@login_required
def study(request):
    context = {
        'title': f'Доступные курсы от {NAME_ORGANIZATION}',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'info/study.html', context=context)


@login_required
def studying(request):
    context = {
        'title': f'Охрана труда с изменениями сентября 2022',
        'name': NAME_ORGANIZATION,
    }
    if request.method == 'POST':
        pass
    return render(request, 'info/studying.html', context=context)
