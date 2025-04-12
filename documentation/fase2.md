
---

# ✅ FASE 2 (con proyecto llamado `django_futbol`)

---

## 🎯 Estructura esperada del proyecto

```
django_futbol/
├── core/              # Lógica compartida, comandos, helpers
├── leagues/           # Modelos de ligas, países, temporadas
├── teams/             # Equipos y estadios
├── fixtures/          # Partidos, resultados, eventos
├── standings/         # Tabla de posiciones
├── templates/         # HTML base con Bootstrap
├── static/            # CSS, JS, imágenes
├── django_futbol/     # Configuración principal del proyecto
├── manage.py
└── .env               # Claves privadas y configuración de entorno
```

---

## 🛠️ PASO A PASO CON `django_futbol`

### 1. Crear el proyecto base

```bash
django-admin startproject django_futbol .
```

Esto crea una carpeta `django_futbol/` con los archivos principales del proyecto (settings, urls, etc.)

---

### 2. Crear las apps funcionales

```bash
python manage.py startapp core
python manage.py startapp leagues
python manage.py startapp teams
python manage.py startapp fixtures
python manage.py startapp standings
```

---

### 3. Configurar apps en `django_futbol/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps del proyecto
    'core',
    'leagues',
    'teams',
    'fixtures',
    'standings',
]
```

---

### 4. Configuración de `templates` y `static`

```bash
mkdir templates static
```

Ajustes en `settings.py`:

```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ... other settings ...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Modified this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ... other settings ...

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

---

### 5. Manejo seguro de claves con `.env`

Instalamos:

```bash
pip install django-environ
```

Archivo `.env` en la raíz:

```
API_FOOTBALL_KEY=tu_api_key_aqui
DEBUG=True
```

Y en `settings.py` (parte superior):

```python
import environ
env = environ.Env()
environ.Env.read_env()

API_FOOTBALL_KEY = env("API_FOOTBALL_KEY")
DEBUG = env.bool("DEBUG", default=False)
```

---

### 6. Template base con Bootstrap 5

Archivo: `templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}FútbolStats{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="/">⚽ FútbolStats</a>
</nav>

<div class="container mt-4">
    {% block content %}{% endblock %}
</div>
</body>
</html>
```

---

### 7. (Opcional) .gitignore para tu proyecto

```
*.pyc
__pycache__/
.env
db.sqlite3
/static/
/media/
```

---

## ✅ Resultado de FASE 2

| Elemento                           | Estado |
|------------------------------------|--------|
| Proyecto Django creado             | ✅     |
| Apps funcionales creadas           | ✅     |
| `.env` y configuración segura      | ✅     |
| Templates y static configurados    | ✅     |
| Estructura profesional lista       | ✅     |

---
