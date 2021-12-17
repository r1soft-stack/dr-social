from django.http import HttpResponse
from django.template import loader


def index(request):
    """

    :param request:
    :return:
    """
    template = loader.get_template('main/index.html')
    context = {
        'main_content': {'title': 'Ristrutturatori Planetari - welcome traveller!!'},
    }
    return HttpResponse(template.render(context, request))


def login(request):
    """

    :param request:
    :return:
    """
    template = loader.get_template('main/login.html')
    context = {
        'main_content': {'title': 'Ristrutturatori Planetari - login'},
    }
    return HttpResponse(template.render(context, request))
