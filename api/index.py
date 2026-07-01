import os
import sys
import django
from pathlib import Path

# Adiciona a raiz do projeto ao Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Configura o módulo de settings do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Setup Django
django.setup()

# Importa e exporta a aplicação WSGI
from mysite.wsgi import application

# Handler para Vercel
handler = application

