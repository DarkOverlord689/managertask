#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para generar la estructura de directorios de un proyecto Git
con arquitectura completa (frontend, backend, infraestructura, etc.)
"""

import os
import sys

def create_directory(path):
    """Crea un directorio si no existe"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Creado: {path}")
    else:
        print(f"Ya existe: {path}")

def create_file(path, content="# Placeholder\n"):
    """Crea un archivo con contenido si no existe"""
    if not os.path.exists(path):
        with open(path, 'w', encoding="utf-8") as f:
            f.write(content)
        print(f"Creado: {path}")
    else:
        print(f"Ya existe: {path}")

def generate_project_structure(base_dir="."):
    """Genera la estructura completa del proyecto"""
    # Estructura principal
    directories = [
        # GitHub
        ".github",
        
        # Frontend
        "frontend/public",
        "frontend/src/components",
        "frontend/src/features",
        "frontend/src/hooks",
        "frontend/src/redux",
        "frontend/src/services",
        "frontend/src/utils",
        
        # Backend
        "backend/services/api-gateway",
        "backend/services/tasks",
        "backend/services/users",
        "backend/services/notifications",
        "backend/services/search",
        "backend/services/analytics",
        "backend/shared",
        
        # Infraestructura
        "infrastructure/docker",
        "infrastructure/kubernetes",
        "infrastructure/terraform",
        "infrastructure/scripts",
        
        # Monitoreo
        "monitoring/prometheus",
        "monitoring/grafana",
        "monitoring/elk",
        "monitoring/alerts",
        
        # Pruebas de carga
        "load-testing/jmeter",
        "load-testing/k6",
        
        # Documentación
        "docs/assets",
        "docs/api",
        
        # Base de datos
        "database/migrations",
        "database/seeds",
        "database/schema"
    ]
    
    # Crear directorios
    for directory in directories:
        create_directory(os.path.join(base_dir, directory))
        # Agregar un README.md básico en cada directorio para mantener la estructura en git
        create_file(os.path.join(base_dir, directory, "README.md"), 
                    f"# {directory.split('/')[-1].capitalize()}\n\nDescripción del propósito de este directorio.\n")
    
    # Crear archivos específicos
    files = {
        "frontend/src/App.tsx": """import React from 'react';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Mi Aplicación</h1>
        <p>Bienvenido a mi aplicación React</p>
      </header>
    </div>
  );
}

export default App;
""",
        "frontend/vite.config.js": """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
  },
});
""",
        "frontend/package.json": """{
  "name": "mi-proyecto-frontend",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.16.0",
    "@reduxjs/toolkit": "^1.9.5",
    "react-redux": "^8.1.2",
    "axios": "^1.5.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.4",
    "vite": "^4.4.9",
    "typescript": "^5.2.2"
  },
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
""",
        "backend/package.json": """{
  "name": "mi-proyecto-backend",
  "version": "0.1.0",
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.5.0",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "jsonwebtoken": "^9.0.2"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.6.4"
  },
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest"
  }
}
""",
        "docker-compose.yml": """version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    depends_on:
      - api-gateway

  api-gateway:
    build: ./backend/services/api-gateway
    ports:
      - "4000:4000"
    volumes:
      - ./backend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    depends_on:
      - mongodb
      - redis

  tasks-service:
    build: ./backend/services/tasks
    volumes:
      - ./backend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    depends_on:
      - mongodb

  users-service:
    build: ./backend/services/users
    volumes:
      - ./backend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    depends_on:
      - mongodb

  mongodb:
    image: mongo:6.0
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

  redis:
    image: redis:7.0
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  mongodb_data:
  redis_data:
""",
        ".env.example": """# Variables de entorno para desarrollo

# Frontend
VITE_API_URL=http://localhost:4000/api
VITE_APP_ENV=development

# Backend
NODE_ENV=development
PORT=4000
MONGODB_URI=mongodb://mongodb:27017/miapp
REDIS_URI=redis://redis:6379
JWT_SECRET=your-secret-key-here
JWT_EXPIRES_IN=1d

# Servicios
TASKS_SERVICE_URL=http://tasks-service:4001
USERS_SERVICE_URL=http://users-service:4002
NOTIFICATIONS_SERVICE_URL=http://notifications-service:4003
""",
        ".gitignore": """# Dependencias
node_modules/
.pnp/
.pnp.js

# Testing
coverage/

# Producción
build/
dist/
out/

# Misc
.DS_Store
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Editor directories and files
.idea/
.vscode/
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# Python
__pycache__/
*.py[cod]
*$py.class
venv/
env/
.env/

# Terraform
.terraform/
*.tfstate
*.tfstate.backup
*.tfplan

# Logs
logs/
*.log
""",
        "README.md": """# Mi Proyecto Full Stack

## Descripción
Este proyecto implementa una arquitectura moderna de aplicación full stack con microservicios.

## Estructura del Proyecto
```
├── .github/                  # Configuraciones de GitHub (Actions, etc.)
├── frontend/                 # Aplicación frontend con React
│   ├── public/               # Archivos estáticos
│   ├── src/                  # Código fuente React
│   │   ├── components/       # Componentes reutilizables
│   │   ├── features/         # Módulos de funcionalidades
│   │   ├── hooks/            # Custom hooks
│   │   ├── redux/            # Configuración y slices de Redux
│   │   ├── services/         # Servicios de API
│   │   ├── utils/            # Utilidades
│   │   └── App.tsx           # Componente raíz
│   ├── vite.config.js        # Configuración de Vite
│   └── package.json          # Dependencias frontend
├── backend/                  # Servicios de backend
│   ├── services/             # Microservicios
│   │   ├── api-gateway/      # API Gateway
│   │   ├── tasks/            # Servicio de tareas
│   │   ├── users/            # Servicio de usuarios
│   │   ├── notifications/    # Servicio de notificaciones
│   │   ├── search/           # Servicio de búsqueda
│   │   └── analytics/        # Servicio de analíticas
│   ├── shared/               # Código compartido entre servicios
│   └── package.json          # Dependencias backend
├── infrastructure/           # Archivos de infraestructura
│   ├── docker/               # Configuraciones Docker
│   ├── kubernetes/           # Manifiestos de Kubernetes
│   ├── terraform/            # Configuración de infraestructura como código
│   └── scripts/              # Scripts de automatización
├── monitoring/               # Configuraciones de monitoreo
│   ├── prometheus/           # Configuración de Prometheus
│   ├── grafana/              # Dashboards de Grafana
│   ├── elk/                  # Configuración de ELK Stack
│   └── alerts/               # Configuración de alertas
├── load-testing/             # Herramientas y configuraciones de pruebas de carga
│   ├── jmeter/               # Escenarios de JMeter
│   └── k6/                   # Scripts de k6
├── docs/                     # Documentación
│   ├── assets/               # Imágenes y recursos
│   ├── api/                  # Documentación de la API (OpenAPI)
│   ├── architecture.md       # Detalles de arquitectura
│   ├── deployment.md         # Guía de despliegue
│   └── load-testing.md       # Documentación de pruebas de carga
├── database/                 # Migraciones y scripts de DB
│   ├── migrations/           # Archivos de migración
│   ├── seeds/                # Datos iniciales
│   └── schema/               # Definición de esquemas
├── docker-compose.yml        # Configuración de Docker Compose para desarrollo
├── .env.example              # Plantilla de variables de entorno
├── .gitignore                # Archivos ignorados por Git
└── README.md                 # Este archivo
```

## Requisitos
- Node.js >= 18
- Docker y Docker Compose
- Python 3 (para scripts de utilidad)

## Instalación
1. Clona este repositorio
2. Copia `.env.example` a `.env` y configura las variables de entorno
3. Ejecuta `docker-compose up -d` para iniciar todos los servicios

## Desarrollo
- Frontend: `cd frontend && npm run dev`
- Backend (servicio específico): `cd backend/services/[servicio] && npm run dev`

## Licencia
MIT
""",
        "docs/architecture.md": """# Arquitectura

## Visión General
Este proyecto utiliza una arquitectura de microservicios para el backend, con React en el frontend.

## Componentes Principales

### Frontend
- Framework: React con TypeScript
- Estado global: Redux Toolkit
- Enrutamiento: React Router
- Estilo: CSS Modules / Styled Components
- Bundler: Vite

### Backend
- Arquitectura: Microservicios
- Gateway: API Gateway (Express)
- Comunicación: REST APIs + Message Queue
- Autenticación: JWT
- Base de datos: MongoDB (principal), Redis (caché)

### Infraestructura
- Contenedores: Docker
- Orquestación: Kubernetes
- CI/CD: GitHub Actions
- Monitoreo: Prometheus + Grafana

## Diagrama de Arquitectura

```
[Cliente Web] --> [API Gateway] --> [Microservicios]
                                      |
                                      |--> [Bases de datos]
```

## Flujo de Datos
1. El cliente realiza solicitudes al API Gateway
2. El Gateway autentica y enruta las solicitudes al microservicio apropiado
3. Los microservicios procesan la solicitud y devuelven la respuesta
4. El Gateway agrega las respuestas y las devuelve al cliente
""",
        "docs/deployment.md": """# Guía de Despliegue

## Entornos
- Desarrollo: Máquinas locales, Docker Compose
- Staging: Kubernetes en la nube
- Producción: Kubernetes en la nube con alta disponibilidad

## Despliegue en Desarrollo
```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down
```

## Despliegue en Kubernetes
```bash
# Aplicar configuraciones
kubectl apply -f infrastructure/kubernetes/

# Verificar despliegue
kubectl get pods
```

## CI/CD Pipeline
1. Pruebas automáticas en cada PR
2. Construcción de imágenes en merge a main
3. Despliegue automático en staging
4. Despliegue manual a producción

## Rollback
En caso de problemas, usar:
```bash
kubectl rollout undo deployment/[nombre-deployment]
```
"""
    }
    
    for file_path, content in files.items():
        create_file(os.path.join(base_dir, file_path), content)

def main():
    """Función principal del script"""
    print("Generador de estructura de directorios para proyecto Git")
    print("=" * 60)
    
    # Verificar argumentos
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        base_dir = input("Ingrese la ruta del directorio base (Enter para directorio actual): ").strip()
        if not base_dir:
            base_dir = "."
    
    print(f"\nCreando estructura en: {os.path.abspath(base_dir)}")
    print("-" * 60)
    
    # Generar la estructura
    generate_project_structure(base_dir)
    
    print("\n¡Estructura de directorios creada con éxito!")
    print("Recuerda inicializar Git con 'git init' si aún no lo has hecho.")

if __name__ == "__main__":
    main()