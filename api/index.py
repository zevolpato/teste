import os
import sys
import django
import logging
from pathlib import Path

# Configura logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("=== Inicializando Django WSGI Handler ===")

# Adiciona a raiz do projeto ao Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
logger.info(f"BASE_DIR: {BASE_DIR}")

# Configura o módulo de settings do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
logger.info(f"DJANGO_SETTINGS_MODULE: mysite.settings")

# Verifica variáveis críticas
db_url = os.getenv('DATABASE_URL')
logger.info(f"DATABASE_URL presente: {bool(db_url)}")
logger.info(f"DEBUG: {os.getenv('DEBUG')}")

try:
    # Setup Django
    django.setup()
    logger.info("Django setup concluído com sucesso")
    
    # Importa e exporta a aplicação WSGI
    from mysite.wsgi import application
    logger.info("Aplicação WSGI importada com sucesso")
    
    # Handler para Vercel
    handler = application
    logger.info("Handler configurado e pronto")
    
except Exception as e:
    logger.error(f"Erro ao inicializar Django: {str(e)}", exc_info=True)
    
    # Fallback: cria uma aplicação minimalista que retorna erro
    def handler(environ, start_response):
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain; charset=utf-8')]
        start_response(status, response_headers)
        return [b'Erro ao inicializar Django: Verifique DATABASE_URL e outras variáveis de ambiente']
    
    logger.info("Usando handler de fallback")

logger.info("=== Inicialização concluída ===")


