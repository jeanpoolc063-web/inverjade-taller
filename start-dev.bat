@echo off
REM Script para iniciar INVERJADE con Docker en Windows

echo 🚀 Iniciando INVERJADE con Docker Compose...

REM Verificar si Docker está instalado
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker no está instalado. Por favor, instala Docker Desktop.
    exit /b 1
)

docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker Compose no está instalado.
    exit /b 1
)

echo 📦 Construyendo imágenes Docker...
docker-compose build

echo 🔄 Levantando servicios...
docker-compose up -d

echo ⏳ Esperando a que la base de datos esté lista...
timeout /t 10

echo 🔄 Ejecutando migraciones...
docker-compose exec backend python manage.py migrate

echo 👤 Creando superusuario...
docker-compose exec -T backend python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').delete(); User.objects.create_superuser('admin', 'admin@inverjade.local', 'admin123')"

echo.
echo ✅ ¡INVERJADE está listo!
echo.
echo 🌐 Accesos:
echo    Frontend: http://localhost:5173
echo    Backend API: http://localhost:8000/api
echo    Admin Panel: http://localhost:8000/admin
echo    Usuario: admin
echo    Contraseña: admin123
echo.
echo 📝 Para ver los logs:
echo    docker-compose logs -f
echo.
echo 🛑 Para detener:
echo    docker-compose down
pause
