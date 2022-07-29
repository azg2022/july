from dganjo.http import HttpResponse
from dganjo.shortcut import Redirect


def index(request):

    return HttpResponse('ok')

def login(request): 

    return Redirect('index')
