import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import User

# Crear usuarios de ejemplo
User.objects.all().delete()  # Limpiar usuarios existentes
User.objects.create(name='Usuario 1', email='usuario1@example.com')
User.objects.create(name='Usuario 2', email='usuario2@example.com')

print('Datos de ejemplo creados correctamente.')
