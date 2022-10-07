# Todo-list

## Lista de tarefas com django, django rest framework e vue.js

## Instruções

Abra o windows powershell na pasta que deseja clonar o projeto

```bash
git clone https://github.com/guilhermelbo/crud
cd crud
```
### Para executar o servidor:

Estando na pasta crud

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Para executar o cliente:

Estando na pasta crud

```bash
cd frontend
npm install
npm run serve
```
