from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter #router para registrar las rutas automáticamente
from usuarios.api import RegistroUsuarioApi
from usuarios.apiLogin import LoginUsuarioApi, LogoutUsuarioApi,IngresoUsuarioApi



# 1. Crear el router
router =DefaultRouter()


# 2. Registrar el ViewSet en el router
router.register (r'usuarios', RegistroUsuarioApi) #CLASE DESDE EL ARCIVO VIEWS  con viewsets-  - Y CRUD - GET, POST ,PUT , PATCH, DELETE



urlpatterns = [
    path('', include(router.urls)),    # <-- Aquí registras las rutas  (GET -POST ) 
    path('login/', LoginUsuarioApi.as_view()),
    path('usuario/',IngresoUsuarioApi.as_view()),
    path('logout/',LogoutUsuarioApi.as_view()),
  
]





#GET → http://localhost:8000/api/usuarios/ → Listar todos los clientes
#POST → http://localhost:8000/api/usuarios/ → Crear un cliente
#PUT → http://localhost:8000/api/usuarios/1/ → Actualizar un cliente    
#DELETE → http://localhost:8000/api/usuarios/1/ → Eliminar un cliente