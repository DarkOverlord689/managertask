# Guía de Despliegue

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
