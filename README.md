# QA Automation Challenge

Este repositorio contiene un conjunto de pruebas automatizadas para demostrar habilidades en pruebas de integración, UI y mobile, utilizando **PyTest**, **Requests**, **Selenium + Behave** y **Appium**.

---
## 1. Pruebas de Integración de la API de Usuarios

Este proyecto contiene pruebas automatizadas para validar la gestión de usuarios en la API utilizando `pytest` y `requests`.

## Casos de Prueba

### 1. Obtener la lista de usuarios
**Escenario:**
- **Given** la API está disponible
- **When** realizo una solicitud `GET` a `/users?page=2`
- **Then** la respuesta debe tener un código de estado `200`
- **And** la respuesta debe contener una lista de usuarios

### 2. Crear un nuevo usuario
**Escenario:**
- **Given** la API está disponible
- **When** realizo una solicitud `POST` a `/users` con los siguientes datos:
  ```json
  {
    "name": "morpheus",
    "job": "leader"
  }
  ```
- **Then** la respuesta debe tener un código de estado `201`
- **And** la respuesta debe contener los datos del usuario creado

### 3. Crear múltiples usuarios con datos parametrizados
**Escenario:**
- **Given** la API está disponible
- **When** realizo una solicitud `POST` a `/users` con diferentes combinaciones de datos:
  ```json
  [
    { "name": "morpheus", "job": "leader" },
    { "name": "neo", "job": "the one" }
  ]
  ```
- **Then** la respuesta debe tener un código de estado `201`
- **And** la respuesta debe contener los datos correctos del usuario creado

### 4. Actualizar un usuario existente
**Escenario:**
- **Given** la API está disponible y existe un usuario
- **When** realizo una solicitud `PUT` a `/users/{id}` con los siguientes datos:
  ```json
  {
    "name": "morpheus",
    "job": "zion resident"
  }
  ```
- **Then** la respuesta debe tener un código de estado `200`
- **And** la respuesta debe contener los datos actualizados del usuario

### 5. Eliminar un usuario
**Escenario:**
- **Given** la API está disponible y existe un usuario
- **When** realizo una solicitud `DELETE` a `/users/{id}`
- **Then** la respuesta debe tener un código de estado `204`

## Configuración y Ejecución

### Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### Ejecución de Pruebas
Para ejecutar todas las pruebas:
```bash
pytest tests/api_tests/
```

Para ejecutar una prueba específica:
```bash
pytest tests/api_tests/test_users.py::test_create_user
```

### Uso de Fixtures
- Se utiliza `@pytest.fixture` para gestionar la sesión HTTP y optimizar las conexiones.
- Se crea y elimina automáticamente un usuario de prueba con `new_user`.
- Se parametrizan pruebas de creación de usuario con `@pytest.mark.parametrize`.



---

## 2. Pruebas de UI en la Web

# Pruebas de UI en la Web

Las pruebas de UI se implementan utilizando **Selenium** y **Behave**, definiendo escenarios en formato **Gherkin**.

## Caso de Uso: Búsqueda en Wikipedia

**Feature:** Búsqueda en Wikipedia  
*Como usuario quiero buscar información en Wikipedia para obtener artículos relevantes.*

**Escenario: Búsqueda de un término válido**  
- **Given** el usuario está en la página de inicio de Wikipedia  
- **When** busca "Selenium"  
- **Then** el primer resultado debe contener "Selenium"

## Estructura del Proyecto Web

- **features/**: Contiene los archivos `.feature` con los escenarios en Gherkin.  
  - `search.feature`
- **steps/**: Contiene los archivos con la implementación de los pasos (steps) en Python para Behave.  
  - `test_search.py`
- **page_objects/**: Contiene los Page Objects que encapsulan la lógica de interacción con la web.  
  - `home_page.py`  
  - `search_results_page.py`
- **base_page.py**: Clase base para los Page Objects.

## Ejecución de las Pruebas Web

Para ejecutar las pruebas de UI definidas con Behave:
```bash
behave tests/web_tests/features/

---
