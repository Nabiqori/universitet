from django.shortcuts import *
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
    if request.method == "POST":
        Yonalish.objects.create(
            nom=request.POST.get('nom'),
            aktiv=request.POST.get('aktiv') == 'on',
        )
        return redirect("/yonalishlar/")
    return render(request,"yonalishlar_qoshish.html")

def fanlar_qoshish_view(request):
    if request.method == "POST":
        yonalish_id = request.POST.get('yonalish')


        if yonalish_id != 'None':  # Agar 'None' bo'lmasa, 'Yonalish' instansiyasini olish
            yonalish = Yonalish.objects.get(id=yonalish_id)
        else:
            yonalish=None
        Fan.objects.create(
            nom=request.POST.get('nom'),
            asosiy=request.POST.get('asosiy') == 'on',
            yonalish=yonalish,

        )
        return redirect("/fanlar/")
    yonalishlar = Yonalish.objects.all()
    context={
        "yonalishlar":yonalishlar,
    }
    return render(request,"fanlar_qoshish.html", context)

def ustoz_qoshish_view(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        jins = request.POST.get('jins')
        yosh = request.POST.get('yosh')
        daraja = request.POST.get('daraja')
        fan_id = request.POST.get('fan')


        fan = None
        if fan_id != 'None':
            fan = Fan.objects.get(id=fan_id)


        Ustoz.objects.create(
            nom=nom,
            jins=jins,
            yosh=yosh,
            daraja=daraja,
            fan=fan
        )

        return redirect("/ustozlar/")

    fanlar = Fan.objects.all()
    context = {
        "fanlar": fanlar,
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
        nom = request.POST.get("nom")
        yosh = request.POST.get("yosh")
        daraja = request.POST.get("daraja")
        jins = request.POST.get("jins")
        fan_id = request.POST.get("fan_id")


        fan = Fan.objects.get(id=fan_id) if fan_id != 'None' else None

        ustoz.nom = nom
        ustoz.yosh = yosh
        ustoz.daraja = daraja
        ustoz.jins = jins
        ustoz.fan = fan
        ustoz.save()

        return redirect("/ustozlar/")

    fanlar = Fan.objects.exclude(id=ustoz.fan.id).order_by("nom")
    context = {
        "ustoz": ustoz,
        "fanlar": fanlar,
    }
    return render(request, "ustoz_update.html", context)
