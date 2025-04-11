🧠 MEGAPROMPT DJANGO + API-FOOTBALL (Modo Automático)

Actúa como un arquitecto de software y desarrollador full-stack senior especializado en Django (backend), PostgreSQL (BBDD) y Bootstrap 5 (frontend).
Quiero que diseñes una aplicación web completa que consuma datos desde la API-Football, los almacene en una base de datos local, y los muestre al usuario desde esa base de datos, no desde la API en tiempo real.
Trabaja en modo automático paso a paso, siendo tú quien me guíe como si fueras mi CTO. Yo solo te confirmo si avanzamos o no a la siguiente fase.
Usa mejores prácticas, estructuras limpias, normalización en modelos, relaciones claras, código completo y ejemplos ejecutables.

🎯 Objetivo del Proyecto:
•	Obtener datos de fútbol profesional desde la API-Football (ligas, equipos, partidos, clasificaciones).
•	Almacenarlos en PostgreSQL localmente usando Django ORM.
•	Visualizarlos desde la base de datos mediante un frontend responsive en Bootstrap 5.

📌 Endpoints de API-Football a cubrir:
•	/leagues → info de ligas y copas
•	/teams → equipos por liga/temporada
•	/fixtures → partidos, resultados, fechas
•	/standings → clasificaciones actuales
•	/players (opcional)

Considera que los datos de la API:
•	Tienen estructuras JSON anidadas
•	Tienen claves únicas (id, fixture_id, etc.)
•	Requieren normalización (ej: no repetir info de ligas, equipos, países)

📁 Arquitectura esperada del proyecto:
bash
CopiarEditar
futbolstats/
├── core/              # Utilidades generales y lógica compartida
├── leagues/           # Modelos y vistas para ligas, países, temporadas
├── teams/             # Equipos
├── fixtures/          # Partidos
├── standings/         # Clasificación por temporada y liga
├── templates/         # HTML con Bootstrap 5
├── static/            # CSS, JS, imágenes
├── futbolstats/       # Configuración del proyecto
├── manage.py
└── .env               # API key y variables sensibles

🧪 Funcionalidades clave que debe incluir:
•	Sincronización de datos desde la API mediante comandos de Django (python manage.py sync_fixtures)
•	Modelos correctamente diseñados: League, Country, Season, Team, Fixture, Standing
•	Relaciones bien normalizadas (ForeignKey, OneToOne)
•	Plantillas responsivas con Bootstrap: uso de base.html, blocks, extends
•	Componente visual: tabla de partidos, cards de equipos, dropdowns por temporada/liga
•	Manejo seguro de API key con django-environ y .env

🔐 Seguridad:
•	API key no se expone nunca en el código fuente
•	Uso de .env + django-environ

🧭 Modo de trabajo:
Guíame tú mismo por las siguientes fases:
1.	🔎 Revisión de la API-Football y definición de modelos (iniciada)
2.	📁 Estructura del proyecto y creación de apps
3.	🧬 Modelado de datos completo y migraciones
4.	🔄 Consumo de la API y persistencia en PostgreSQL
5.	👀 Front-End básico con Bootstrap 5 para listar partidos
6.	⏰ Sincronización de datos (manual o programada)
7.	📦 Mejora UX: filtros, búsqueda, paginación
8.	🛡️ Seguridad, entorno, despliegue