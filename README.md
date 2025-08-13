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

### 1️⃣ Clonar o repositório ou baixar o arquivo zip e descompactar
```bash
git clone https://github.com/seu-usuario/DJANGO_API.git
cd DJANGO_API
```
### 2️⃣ Criar ou ativar ambiente virtual (como já existe um, pelo linux basta indicar no "activate" na bin
Lembre de rodar com permissões de administrador no windows, se tiver dificuldades, aconselho usar o gitbash, e seguir com comandos linux/bash
```bash
python -m venv venv # Linux/Mac
source venv/bin/activate  # Linux/Mac

python -m venv venv      # Windows
.\venv\Scripts\activate    # Windows
```
### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```
#### OUTPUT ESPERADO:
<img width="1539" height="246" alt="image" src="https://github.com/user-attachments/assets/a65f5333-6ab6-4b3c-b9a7-d722d5916d59" />

### 5️⃣ Acessar a API e documentação

    API base: http://127.0.0.1:8000/api/

    Swagger: http://127.0.0.1:8000/swagger/

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

---
# Aparência esperada do swagger:
<img width="1792" height="968" alt="image" src="https://github.com/user-attachments/assets/5b0f9496-cd13-466b-9e7c-92a14afd5431" />

Sinta-se livre para testar a API por completo, mas se preferir, aqui vai um percurso para testar a maioria das funcionalidades

## EXECUTE REQUISIÇÕES NOS SEGUINTES ENDPOINTS:

### 1. Criar uma trilha
#### Clique em ***Try it Out***
<img width="989" height="822" alt="image" src="https://github.com/user-attachments/assets/da5e37ec-f207-4d47-8056-45f1fcd3e114" />
#### Defina o JSON de acordo com o exemplo e clique em Execute:
<img width="1555" height="871" alt="image" src="https://github.com/user-attachments/assets/774ab1fa-946a-4c4d-91bb-69afd31bb468" />

### 2. Listar Trilhas Criadas
<img width="1423" height="906" alt="image" src="https://github.com/user-attachments/assets/006a8e9a-6742-49a0-8c19-cba0ad060c91" />

#### Pode utilizar o CRUD de trilhas no endpoint: trails/{id}

### 3. Criar uma Etapa nessa trilha: 
<img width="859" height="935" alt="image" src="https://github.com/user-attachments/assets/ee0b9250-d2cb-49fd-af49-f91b0cd98002" />
obs: Fornecer o ID da trilha no endpoint e a posição da etapa, exemplo:
se essa é sua primeira etapa, então "Position" : 1, se for sua segunda etapa: "Position" : 2
Dessa forma, fica flexivel definir qual o lugar de cada etapa dentro da trilha de aprendizado

### 4. Liste as Etapas dessa trilha
<img width="1143" height="919" alt="image" src="https://github.com/user-attachments/assets/a557ea23-7af0-4ec0-9bb9-26673e29f962" />

### 5. Adicione um Link na sua etapa
<img width="997" height="805" alt="image" src="https://github.com/user-attachments/assets/222e2740-6df2-478e-adda-c9bb8ed01826" />

### 6. Adicione uma conexão/ligação na etapa, Podendo ser apenas um dos campos, o JSON de ATTACHMENT é flexivel e aceita nulos e espaços brancos
<img width="853" height="922" alt="image" src="https://github.com/user-attachments/assets/faacdc30-bd98-48ff-b6a8-304b5c80c659" />

### 7. Atualize o estado de assistido ou não por esses endpoints:
<img width="1426" height="110" alt="image" src="https://github.com/user-attachments/assets/20d99944-800a-4371-86e6-e656ab2bc816" />

### 8. Por fim, liste a trilha toda de forma detalhada utilizando:
<img width="1278" height="848" alt="image" src="https://github.com/user-attachments/assets/c1513a11-9344-47d9-838b-91799608d18a" />


## Tudo que foi listado e criado, possui um CRUD próprio para atualização e exclusão no banco de dados diretamente
Entretando num projeto real, talvez seja melhor utilizar SQLITE ou MongoDB para CACHE, e só depois migrar para um banco de dados mySQL ou PostgreSQL

