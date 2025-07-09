# Projeto Django - Notas

Um projeto Django simples para gerenciamento de notas.

## Configuração do Ambiente

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd "Django - Visao Geral e Primeiro App"
```

### 2. Crie um ambiente virtual
```bash
python -m venv env
```

### 3. Ative o ambiente virtual
**Windows:**
```bash
env\Scripts\activate
```

**Linux/Mac:**
```bash
source env/bin/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Execute as migrações
```bash
cd proj_test
python manage.py migrate
```

### 6. Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```

O projeto estará disponível em `http://127.0.0.1:8000/`

## Estrutura do Projeto

- `proj_test/` - Diretório principal do projeto Django
- `notas/` - App Django para gerenciamento de notas
- `requirements.txt` - Dependências do projeto

## Apps

- **notas** - Aplicação para gerenciamento de notas
