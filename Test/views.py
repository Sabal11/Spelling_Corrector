from django.http import HttpResponse

def Welcome(request):
    return HttpResponse('sabal')