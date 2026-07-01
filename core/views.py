from django.shortcuts import render
from django.http import JsonResponse
from .models import Note


def index(request):
    try:
        notes = Note.objects.all()[:10]
        return render(request, 'core/index.html', {'notes': notes})
    except Exception as e:
        return render(request, 'core/index.html', {'notes': [], 'error': str(e)})


def health(request):
    """Endpoint de health check sem acessar banco de dados"""
    return JsonResponse({
        'status': 'ok',
        'message': 'API Django está funcionando'
    })

