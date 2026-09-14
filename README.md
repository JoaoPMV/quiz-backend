# Quiz - API

API backend da aplicação **Quiz**, responsável por autenticação de usuários e fornecimento de perguntas para o frontend.

---

## Objetivo

Fornecer serviços de backend para:

- cadastro e autenticação de usuários
- proteção de rotas com JWT
- integração com banco de dados PostgreSQL
- gerenciamento de perguntas do quiz (3.716 perguntas no banco)

---

## Tecnologias Utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- PostgreSQL (Neon)
- JWT (autenticação)
- bcrypt
- python-dotenv
- Flask-CORS

---

## Funcionalidades

- Cadastro de usuários
- Login com geração de token JWT
- Rotas protegidas por token
- Endpoint de perguntas para o quiz
- Seed de perguntas no banco

---

## Melhorias Futuras

- [ ] Validação avançada de payload
- [ ] Rate limiting
- [ ] Logs e monitoramento
- [ ] Histórico de desempenho por usuário

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.10+
- PostgreSQL (ou conta no Neon)
- `pip` e `venv`

### 1. Clonar o repositório

```bash
git clone https://github.com/JoaoPMV/quiz-backend.git
```

### 2. Acessar a pasta do projeto

```bash
cd quiz-backend
```

### 3. Criar e ativar ambiente virtual

```bash
python -m venv venv
```

Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com:

```env
DATABASE_URL=sua_string_de_conexao_postgresql
JWT_SECRET=seu_segredo_jwt
FRONTEND_URL=http://localhost:5173
```

> Se usar `.env.local`, lembre de carregar explicitamente no `config.py`.

### 6. Executar a API

```bash
python app.py
```

A API ficará disponível em:

```bash
http://localhost:5000
```

---

## Seed de perguntas

Para popular perguntas no banco:

```bash
python -m seeders.seed_questions
```

---

## Frontend da Aplicação

Este repositório contém apenas o backend da aplicação.  
O frontend está disponível em:  
https://github.com/JoaoPMV/quiz-frontend

---

## Autor

Desenvolvido por **JoaoPMV**  
GitHub: https://github.com/JoaoPMV
