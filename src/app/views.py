from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponseRedirect("/admin/")
