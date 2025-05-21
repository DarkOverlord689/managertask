from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Simulación de usuarios
fake_users_db = {
    "usuario@correo.com": {
        "email": "usuario@correo.com",
        "hashed_password": pwd_context.hash("contraseña123"),
        "nombre": "Usuario de Prueba"
    }
}
