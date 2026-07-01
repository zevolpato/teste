# teste

Projeto Django mínimo para testes em sala de aula.

Configurações principais:
- Banco: Supabase via `DATABASE_URL` (Postgres)
- Deploy: Vercel (builder `@vercel/python`)

Como usar localmente:

1. Crie e ative um virtualenv:

```bash
python -m venv env
source env/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Configure variáveis de ambiente (opcional):

```bash
export SECRET_KEY='chave_local'
export DEBUG=1
# se for usar Supabase, defina DATABASE_URL fornecida pelo Supabase
export DATABASE_URL='postgres://...'
```

4. Rode migrações e crie um superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Deploy para Vercel (resumo):

- Instale o `vercel` CLI e faça login.
- Configure as variáveis de ambiente no dashboard do Vercel: `DATABASE_URL`, `SECRET_KEY`, `DEBUG`.
- Rode `vercel` na raiz do projeto e siga o assistente.

Observações:
- Este projeto é propositalmente simples para uso em aulas e provas de conceito.
- Para produção, revise `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, configurações de SSL e segurança.

