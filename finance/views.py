from django.shortcuts import render_to_response


def index(request):
    return render_to_response('finance/index.html')


def budget(request):
    return render_to_response('finance/budget.html')
