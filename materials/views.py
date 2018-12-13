from django.shortcuts import render

from .models import Hardware


def materials_list(request):
    hardwares = Hardware.objects.all()[:100]

    context = {"hardwares": hardwares}

    return render(request, "materials_list.html", context)
