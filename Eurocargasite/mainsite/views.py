from django.shortcuts import render


def index(request):

    context = {
        "key": 0,
    }
    return render(request, "mainsite/index.html", context)


def about(request):

    context = {
        "key": 0,
    }
    return render(request, "mainsite/about.html", context)


def land_services(request):

    context = {
        "key": 0,
    }
    return render(request, "mainsite/land_services.html", context)


def air_services(request):

    context = {
        "key": 0,
    }
    return render(request, "mainsite/air_services.html", context)


def other_services(request):

    context = {
        "key": 0,
    }
    return render(request, "mainsite/other_services.html", context)


def sea_services(request):

    context = {
        "key": 0,
    }
    return render(request, "mainsite/sea_services.html", context)


def team(request):

    context = {
        "key": 0,
    }
    return render(request, "mainsite/team.html", context)
