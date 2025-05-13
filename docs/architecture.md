# Arquitectura

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
