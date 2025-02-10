from django.shortcuts import *

from .form import FanForm, YonalishForm, UstozForm
from .models import *

def home_view(request):
    return render(request, 'index.html')
def fanlar_view(request):
    fanlar = Fan.objects.all()
    context = {
        'fanlar': fanlar,
    }
    return render(request, 'fanlar.html', context)

def yonalishlar_view(request):
    yonalishlar = Yonalish.objects.all()
    context = {
        'yonalishlar': yonalishlar,
    }
    return render(request, 'yonalishlar.html', context)

def ustozlar_view(request):
    ustozlar = Ustoz.objects.all()
    context = {
        'ustozlar': ustozlar,
    }
    return render(request, 'ustozlar.html', context)

def yonalishlar_qoshish_view(request):
    form = YonalishForm
    if request.method == "POST":
        yonalish_form= YonalishForm(request.POST)
        yonalish_form.save()
        return redirect("/yonalishlar/")
    return render(request,"yonalishlar_qoshish.html",{"form":form})

def fanlar_qoshish_view(request):
    form = FanForm
    if request.method == "POST":
        fan_form = FanForm(request.POST)
        fan_form.save()
        return redirect("/fanlar/")
    context={
        "form":form,
    }
    return render(request,"fanlar_qoshish.html", context)

def ustoz_qoshish_view(request):
    form = UstozForm
    if request.method == "POST":
        ustoz_form = UstozForm(request.POST)
        ustoz_form.save()

        return redirect("/ustozlar/")

    fanlar = Fan.objects.all()
    context = {
        "form": form,
    }

    return render(request, "ustozlar_qoshish.html", context)
def fan_update_view(request, pk):

    if request.method == "POST":
        if request.POST.get('yonalish_id') == '':
            yonalish_id = None
        else:
            yonalish_id = Yonalish.objects.get(id=request.POST.get("yonalish_id"))
        fan = Fan.objects.filter(pk=pk)
        fan.update(
            nom=request.POST.get("nom"),
            asosiy=request.POST.get('asosiy') == 'on',
            yonalish=yonalish_id,
        )
        return redirect("/fanlar/")
    fan = get_object_or_404(Fan, pk=pk)
    if fan.yonalish:
        yonalishlar = Yonalish.objects.exclude(id=fan.yonalish.id).order_by("nom")
    else:
        yonalishlar = Yonalish.objects.all().order_by("nom")

    context = {
        "fan": fan,
        "yonalishlar": yonalishlar,
    }
    return render(request, "fan_update.html", context)
def yonalish_update_view(request, pk):
    yonalish= Yonalish.objects.filter(pk=pk)
    if request.method == "POST":
        yonalish.update(
            nom=request.POST.get('nom'),
            aktiv=request.POST.get('aktiv') == 'on',
        )
        return redirect("/yonalishlar/")
    yonalish = get_object_or_404(Yonalish, pk=pk)
    context = {
        'yonalish':yonalish,
    }
    return render(request, 'yonalish_update.html', context)
def ustoz_update_view(request, pk):
    ustoz = get_object_or_404(Ustoz, pk=pk)

    if request.method == "POST":
        fan_id = request.POST.get("fan_id")


        fan = Fan.objects.get(id=fan_id)
        ustoz.nom = request.POST.get("nom")
        ustoz.yosh = request.POST.get("yosh")
        ustoz.daraja = request.POST.get("daraja")
        ustoz.jins = request.POST.get("jins")
        ustoz.fan = request.POST.get("fan_id")
        ustoz.save()

        return redirect("/ustozlar/")

    fanlar = Fan.objects.exclude(id=ustoz.fan.id).order_by("nom")
    context = {
        "ustoz": ustoz,
        "fanlar": fanlar,
    }
    return render(request, "ustoz_update.html", context)
