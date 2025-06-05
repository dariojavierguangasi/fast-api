# FastAPI Project 

Proyecto base para aplicaciones web modernas usando **FastAPI**, **SQLAlchemy**, y **Alembic** para la gestión de base de datos.

---

## 🚀 Características principales

- API web rápida y asíncrona con FastAPI.
- Gestión de base de datos con SQLAlchemy y soporte para PostgreSQL.
- Migraciones de base de datos automáticas usando Alembic.
- Estructura modular y limpia para escalabilidad y buenas prácticas.
- Documentación interactiva de la API generada automáticamente (Swagger/OpenAPI y Redoc).

---

## 🗂️ Estructura de carpetas recomendada

```
app/
├── api/            # Rutas y endpoints
├── exceptions/     # Excepciones personalizadas
├── db/             # Modelos, migraciones y conexión a la base de datos
├── schemas/        # Esquemas Pydantic (serialización y validación)
├── services/       # Lógica de negocio o servicios
├── main.py         # Punto de entrada de la aplicación
alembic/            # Directorio de migraciones Alembic
```

---

## ⚙️ Instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/tu_usuario/fastapi_project_template.git
cd fastapi_project_template
```

2. **Crea un entorno virtual y activa**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala dependencias**

```bash
pip install -r requirements.txt
```


---

## 🛠️ Migraciones con Alembic

1. **Crear una nueva migración tras modificar modelos**

```bash
alembic revision --autogenerate -m "Describir el cambio"
```

2. **Aplicar migraciones a la base de datos**

```bash
alembic upgrade head
```

---

## 🏃‍♂️ Ejecución local

```bash
uvicorn app.main:app --reload --port 5000
```

Accede a la documentación automática en:
- Swagger UI: [http://localhost:5000/docs](http://localhost:5000/docs)
- ReDoc: [http://localhost:5000/redoc](http://localhost:5000/redoc)

---
