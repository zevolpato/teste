#!/bin/bash

echo "=== Verificando variáveis de ambiente ==="
echo "DATABASE_URL: ${DATABASE_URL:-NOT SET}"
echo "DEBUG: ${DEBUG:-NOT SET}"
echo "SECRET_KEY: ${SECRET_KEY:-NOT SET}"

echo ""
echo "=== Instalando dependências ==="
pip install -r requirements.txt

echo ""
echo "=== Coletando arquivos estáticos ==="
python manage.py collectstatic --noinput

echo ""
echo "=== Executando migrations ==="
python manage.py migrate --noinput

echo ""
echo "=== Build concluído ==="
