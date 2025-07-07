# 💰 Gestor de Finanzas Personales – Backend API

Este proyecto es un sistema de gestión de gastos y abonos personales, construido con **Django Rest Framework**. Permite llevar el control de tus cuentas, categorías de gasto y transacciones de forma segura, autenticada con **JWT**.

---

## 🚀 Características

- 🔐 Autenticación basada en JSON Web Tokens (JWT)
- 📄 Documentación interactiva de la API con Swagger y ReDoc (`drf-yasg`)
- 📦 CRUD completo para:
  - Cuentas
  - Categorías
  - Transacciones (ingresos/gastos)
- 🛡️ Endpoints protegidos con permisos `IsAuthenticated`

---

## 📁 Estructura de la API

| Recurso       | Endpoint base         | Acceso    |
| ------------- | --------------------- | --------- |
| Cuentas       | `/api/accounts/`      | Protegido |
| Categorías    | `/api/categories/`    | Protegido |
| Transacciones | `/api/transactions/`  | Protegido |
| JWT Login     | `/api/token/`         | Público   |
| Refresh Token | `/api/token/refresh/` | Público   |

---

## 🧪 Requisitos

- Python 3.10+
- pip
- virtualenv (opcional)

---

## ⚙️ Instalación

```bash
# 1. Clona el proyecto
git clone https://github.com/tuusuario/gestor-finanzas-django.git
cd gestor-finanzas-django

# 2. Crea y activa el entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Crea el archivo .env (si usas variables de entorno)
cp .env.example .env

# 5. Aplica las migraciones
python manage.py migrate

# 6. Crea un superusuario (opcional)
python manage.py createsuperuser

# 7. Ejecuta el servidor
python manage.py runserver
```

📚 Documentación de la API
Una vez en funcionamiento, accede a:

Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/
