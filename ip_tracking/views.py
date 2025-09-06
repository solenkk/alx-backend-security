from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({
        'message': 'IP tracking is working!',
        'your_ip': request.META.get('REMOTE_ADDR')
    })
