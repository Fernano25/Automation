**Test Plan - JSONPlaceholder API Testing**

**1. Descripción del Producto**

JSONPlaceholder es una API REST falsa en línea diseñada para testing y prototipado. Sirve como un backend simulado que proporciona endpoints REST estándar con datos de ejemplo estructurados. Es ampliamente utilizado por desarrolladores para:
Prácticas de consumo de APIs
Pruebas de integración
Demostraciones de frontend
Ejemplos educativos de REST APIs
Características principales:
100% gratuito y de acceso público
No requiere autenticación
Respuestas predecibles y consistentes
Estructura de datos realista (posts, usuarios, comentarios)
Soporte completo para operaciones CRUD (CREATE, READ, UPDATE, DELETE)

**2. Objetivos**
**Objetivos Principales**
Validar funcionalidad completa de los endpoints REST principales
Garantizar la calidad de las respuestas HTTP y estructuras de datos
Automatizar el proceso de testing para ejecución continua
Identificar regresiones en cambios futuros de la API
Documentar el comportamiento esperado de cada endpoint

**Objetivos Específicos**
Verificar códigos de estado HTTP correctos (200, 201, 404, etc.)
Validar schemas JSON de todas las respuestas
Probar operaciones CRUD completas (Create, Read, Update, Delete)
Implementar pruebas de negative testing
Establecer métricas de calidad y cobertura
Integrar con CI/CD mediante GitHub Actions

**3. Funcionalidades a Testear**

Endpoint	Método	Descripción	Casos de Prueba
/posts	GET	Obtener todos los posts	Validar estructura, cantidad, códigos HTTP
/posts/{id}	GET	Obtener post específico	IDs válidos/inválidos, datos completos
/posts	POST	Crear nuevo post	Validar creación, datos requeridos
/posts/{id}	PUT	Actualizar post existente	Actualización parcial/completa
/posts/{id}	DELETE	Eliminar post	Verificar eliminación, recurso no encontrado


**4. Tipos de Pruebas**

**4.1. Pruebas Exploratorias**
Objetivo: Descubrir comportamientos no documentados y edge cases
Actividades:
Probar límites de IDs (0, números negativos, decimales)
Enviar payloads con datos inesperados (null, vacíos, tipos incorrectos)
Probar caracteres especiales en campos de texto
Verificar comportamiento con headers HTTP inusuales
Testear rate limiting y performance bajo carga
Duración estimada: 2-3 horas por sprint

**4.2. Pruebas de Humo ("Smoke Testing")**
Objetivo: Verificar funcionalidad básica después de despliegues
Suite de Humo (5-7 minutos):
python

**Test Cases Críticos**
1. GET /posts → Status 200, array no vacío
2. GET /posts/1 → Status 200, estructura completa
3. POST /posts → Status 201, creación exitosa
4. GET /posts/1/comments → Status 200, comentarios relacionados
Criterio de Paso: 100% de los casos deben pasar para considerar estable

**4.3. Pruebas Funcionales**
Cobertura: 100% de endpoints documentados
Categorías:
Pruebas Positivas: Comportamiento esperado con datos válidos
Pruebas Negativas: Manejo de errores con datos inválidos
Pruebas de Validación: Schemas, tipos de datos, formatos
Pruebas de Integración: Flujos entre múltiples endpoints
Ejemplos específicos:
Crear post → Verificar creación → Actualizar → Verificar cambios → Eliminar
Obtener usuario → Verificar posts del usuario → Verificar comentarios en posts

**4.4. Pruebas de Regresión**
Objetivo: Detectar breaks en funcionalidad existente
Estrategia:
Suite completa: 30+ test cases (15-20 minutos)
Ejecución automática: Con cada pull request a main/development
Análisis de impacto: Foco en endpoints modificados + dependientes
Priorización:
P1: Endpoints principales (posts, users)
P2: Endpoints secundarios (comments, albums)
P3: Funcionalidades avanzadas (filtros, nested resources)

**5. Alcance y Limitaciones**

**Dentro del Alcance**
Todos los endpoints documentados de JSONPlaceholder
Validación de schemas JSON con Pydantic
Pruebas de códigos de estado HTTP
Operaciones CRUD completas
Integración con CI/CD (GitHub Actions)
Reportes automatizados de resultados

**Fuera del Alcance (Limitaciones)**
Performance testing (la API tiene rate limiting)
Security testing (no requiere autenticación)
Load testing (limitaciones del servicio gratuito)
UI testing (es puramente una API)
Testing de base de datos real (es una API falsa)
Supuestos Técnicos
La API mantiene consistencia en respuestas
No hay cambios breaking en versiones
Los datos de prueba son predecibles
La disponibilidad del servicio es estable

**6. Herramientas**
Herramienta	Versión	Propósito
Python	3.8+	Lenguaje de programación
Pytest	7.4+	Framework de testing
Requests	2.31+	Cliente HTTP para APIs
Pydantic	2.0+	Validación de schemas JSON


**Métricas y Reportes**
Cobertura de tests: 100% endpoints críticos
Tasa de paso: >95% estable
Tiempo ejecución: <5 minutos (smoke), <20 minutos (completa)
Reportes automáticos en cada ejecución CI/CD

**7. Cronograma**
Fase de Pruebas CRUD Completas (2 Semanas)
Actividad	Duración	Entregable
Pruebas POST/CREATE	1 día	Creación de recursos
Pruebas PUT/UPDATE	1 día	Actualización de recursos
Pruebas DELETE	1 día	Eliminación de recursos
Pruebas de negative testing	2 días	Manejo de errores


**8. Recursos**
QA, Automation QA, Manual QA, Documentador -> Fernando Mollo
PO and Project Manager -> Rina Espinoza

**Recursos de Software**
IDE: VS Code con extensiones Python
Control de Versiones: Git/GitHub
Gestión de Dependencias: pip + requirements.txt
Virtual Environment: venv (Python)
Métricas de Recursos
Tiempo de desarrollo estimado: 3 semanas (120 horas)
Costo infrastructure: $0 (herramientas gratuitas)
Mantenimiento mensual: 8-10 horas

**Métricas de Calidad Objetivo**
Métrica	Objetivo	Actual
Cobertura de Endpoints	100%	100%
Tasa de Paso	>95%	98%
Tiempo de Ejecución	<20 min	15 min
Automatización	100%	100%
Integración CI/CD	100%	100%
Este test plan asegura una estrategia comprehensiva para la automatización de pruebas de JSONPlaceholder, balanceando cobertura, eficiencia y mantenibilidad.

