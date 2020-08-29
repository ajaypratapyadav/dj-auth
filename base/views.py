from django.shortcuts import render


def index(request):
    """
    This method render user to home page
    :param request:
    :return:
    """
    return render(request, 'home.html')
