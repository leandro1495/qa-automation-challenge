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
pytest api_tests/
```

Para ejecutar una prueba específica:
```bash
pytest api_tests/tests/test_users.py
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
behave web_tests/features/
```
---

## 3.Pruebas de UI en la App Móvil

## Caso de Uso: Marcado de un Número en el Marcador Telefónico

### Descripción del Caso de Prueba
Objetivo: Verificar que un usuario pueda marcar correctamente un número en la aplicación de teléfono en un dispositivo Android utilizando la interfaz de la app (marcador telefónico).

### Escenario
El usuario ingresa un número (por ejemplo, "123456789") en el teclado numérico de la app de teléfono y se asegura de que el número aparezca correctamente en la pantalla del dispositivo sin ningún formato adicional.

### Pasos:
1. Abrir la app de teléfono en un dispositivo Android.
2. Acceder al teclado numérico para ingresar los dígitos.
3. Ingresar el número "123456789" en el teclado numérico, verificando que cada tecla se presione correctamente.
4. Verificar que el número ingresado en la pantalla del dispositivo sea igual al número esperado sin formato adicional (sin paréntesis, espacios ni guiones).

## Herramientas Utilizadas

* Appium: Para la automatización de pruebas móviles en dispositivos Android.
* pytest: Framework de testing para ejecutar las pruebas.
* Python: Lenguaje de programación utilizado para escribir las pruebas.
* AppiumBy: Utilizado para localizar los elementos en la app móvil.

**Nota:** Se podría utilizar una biblioteca de expresiones regulares para limpiar la entrada (eliminar caracteres no numéricos) si fuera necesario validar un número con formato.

## Estructura del Proyecto
```bash
├── mobile_tests/
│    └── config/
│          └── capabilities.py # Contiene dic de la app a testear
│    └── pages/
│          └── dialer_page.py   # Página que encapsula la lógica de interacción con la app de teléfono
│    └── tests/
│           └── test_dialer.py  # Contiene el test para marcar el número en la app
```

## Como ejecutar las pruebas

### 1. Iniciar el servidor de Appium: Asegúrate de tener Appium corriendo en tu máquina. Si no lo tienes, puedes instalarlo con el siguiente comando:
```bash
npm install -g appium
```
Luego, inicia el servidor de Appium ejecutando(Host Local):
```bash
appium -p 4724
```

### 2. Ejecutar las pruebas: Puedes ejecutar las pruebas móviles con pytest usando el siguiente comando
```bash
pytest mobile_tests/tests
```

### 3. Ver los resultados: El resultado de las pruebas se mostrará en la terminal. Si todo está configurado correctamente, deberías ver un mensaje de éxito si la prueba pasa:
```bash
✅ Test completado con éxito
```


