# 📚 API de Trilhas de Aprendizado

Este projeto é uma API REST desenvolvida com Django e Django REST Framework para gerenciar trilhas de aprendizado, as etapas em cada trilha (steps), links e anexos.
(Readme.md foi feito com ajuda de I.A, porém cuidadosamente revisado.)

## Tecnologias Utilizadas
- Python 3.x
- Django 5.x
- Django REST Framework
- SQLite (banco de dados padrão, mas pode ser substituído por mySQL ou postgreSQL, para mais escalabilidade)
- drf-yasg (Swagger para documentação)

---

## Funcionalidades:

- CRUD de **Trilhas**
- CRUD de **Etapas**
- CRUD de **Links** relacionados a etapas
- CRUD de **Anexos** relacionados a etapas
- Validações customizadas para garantir consistência dos dados
- Documentação automática com Swagger
- Campos de auditoria (`created_at`)
- Automações e otimizações de requisições, pensando na perfomace geral da aplicação
    Linha que indica automaticamente o número de etapas de uma trilha.
---

## Ideias não implementadas:

- Autenticação com usuário
- Categorizar trilhas. Pensando numa aplicação real, agrupar trilhas por algo em comum pode ser interessante.
---

## 📦 Instalação

### 1️⃣ Clonar o repositório ou baixar zip e descompactar
```bash
git clone https://github.com/seu-usuario/DJANGO_API.git
cd DJANGO_API
```
### 2️⃣ Criar ou ativar ambiente virtual (como já existe um, pelo linux basta indicar no "activate" na bin
```bash
source api_venv/bin/activate  # Linux/Mac

python -m venv venv      # Windows
venv\Scripts\activate    # Windows
```
### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```
### 5️⃣ Acessar a API e documentação

    API base: http://127.0.0.1:8000/api/

    Swagger: http://127.0.0.1:8000/swagger/

    Painel Admin: http://127.0.0.1:8000/admin/

📌 Endpoints Principais
Trilhas

    GET /trails/ → Lista todas as trilhas

    POST /trails/ → Cria nova trilha

    GET /trails/{id}/ → Detalhes de uma trilha

    PUT/PATCH /trails/{id}/ → Atualiza trilha

    DELETE /trails/{id}/ → Remove trilha

Steps

    GET /steps/

    POST /steps/

    GET /steps/{id}/

    PUT/PATCH /steps/{id}/

    DELETE /steps/{id}/

Links

    GET /links/

    POST /links/

    GET /links/{id}/

    PUT/PATCH /links/{id}/

    DELETE /links/{id}/

Attachments

    GET /attachments/

    POST /attachments/

    GET /attachments/{id}/

    PUT/PATCH /attachments/{id}/

    DELETE /attachments/{id}/
