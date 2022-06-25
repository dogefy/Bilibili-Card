from django.http import HttpResponse
from . import build_card


def card(request):
    uid = request.GET['uid']
    data = build_card.main(uid)
    return HttpResponse(data, content_type='image/svg+xml')
