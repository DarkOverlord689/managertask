# 🌐 Proyecto Full Stack: FastAPI + React

Este proyecto combina un backend desarrollado con **FastAPI** y un frontend en **React**, utilizando  **JWT** para la autenticación segura de usuarios.

---

## 🧠 Stack Tecnológico

### 🔙 Backend – FastAPI

- **Framework**: FastAPI – Marco web moderno y de alto rendimiento.
- **Base de datos**: MongoDB (NoSQL).
- **Autenticación**: JWT (JSON Web Tokens) para autenticación segura.

---

## ▶️ Instalación y Ejecución del Backend

### 📌 Requisitos Previos

- Python 3.9 o superior


### 🛠️ Pasos para ejecutar el backend

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio/backend

# 2. Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate       # En Windows: venv\Scripts\activate

# 3. Crear el archivo de dependencias requirements.txt
echo "uvicorn==0.22.0
motor==3.5.1
pydantic==1.10.21
pydantic_core==2.27.2
pymongo==4.8.0
python-jose==3.3.0
passlib==1.7.4
python-multipart==0.0.6
email-validator==2.0.0
python-dotenv==1.0.0
bcrypt==4.0.1
authlib" > requirements.txt

# 4. Instalar las dependencias
pip install -r requirements.txt



# 6. Ejecutar el servidor FastAPI
uvicorn main:app --reload
