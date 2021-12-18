from django.http import HttpResponse
from django.template import loader

# TODO create model for those views


def not_found(request, exception):
    """
    Default 404 page
    :param request:
    :param exception
    :return:
    """
    template = loader.get_template('common/404.html')
    context = {
        'main_content': {'title': 'Ristrutturatori Planetari - Page not found'}
    }
    return HttpResponse(template.render(context, request))


def server_error(request):
    """
    Default 500 page
    :param request:
    :return:
    """
    template = loader.get_template('common/500.html')
    context = {
        'main_content': {'title': 'Ristrutturatori Planetari - Internal server error'},
    }
    return HttpResponse(template.render(context, request))


def index(request):
    """
    Default backend landing page
    :param request:
    :return:
    """
    template = loader.get_template('main/index.html')
    context = {
        'main_content': {'title': 'Ristrutturatori Planetari - welcome traveller!!'},
        'body_content': {'card':
                            {
                                'header': 'Welcome dr-social navigator!',
                                'content': 'Chose where you go!',
                                'admin_button': 'Administration',
                                'frontend_button': 'DR-Socialization',
                            },
                         },
    }
    return HttpResponse(template.render(context, request))

