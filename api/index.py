import os
import sys
from pathlib import Path

# Adiciona a raiz do projeto ao Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Configura o módulo de settings do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Importa e exporta a aplicação WSGI
from mysite.wsgi import application

# Handler para Vercel
handler = application
