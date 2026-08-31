#!/bin/bash

# Script para iniciar el desarrollo con Docker

echo "🚀 Iniciando INVERJADE con Docker Compose..."

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado. Por favor, instala Docker."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose no está instalado. Por favor, instala Docker Compose."
    exit 1
fi

echo "📦 Construyendo imágenes Docker..."
docker-compose build

echo "🔄 Levantando servicios..."
docker-compose up -d

echo "⏳ Esperando a que la base de datos esté lista..."
sleep 10

echo "🔄 Ejecutando migraciones..."
docker-compose exec backend python manage.py migrate

echo "👤 Creando superusuario..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').delete(); User.objects.create_superuser('admin', 'admin@inverjade.local', 'admin123')" | docker-compose exec -T backend python manage.py shell

echo ""
echo "✅ ¡INVERJADE está listo!"
echo ""
echo "🌐 Accesos:"
echo "   Frontend: http://localhost:5173"
echo "   Backend API: http://localhost:8000/api"
echo "   Admin Panel: http://localhost:8000/admin"
echo "   Usuario: admin"
echo "   Contraseña: admin123"
echo ""
echo "📝 Para ver los logs:"
echo "   docker-compose logs -f"
echo ""
echo "🛑 Para detener:"
echo "   docker-compose down"
