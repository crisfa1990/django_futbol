
---

# ✅ **FASE 1 — Análisis exhaustivo de API-Football v3 y modelado de dominio Django**

---

## 📚 Sitio oficial de documentación:
[https://www.api-football.com/documentation-v3](https://www.api-football.com/documentation-v3)

API RESTful que provee estadísticas en tiempo real y datos históricos de:
- Ligas y Copas
- Equipos
- Partidos (Fixtures)
- Clasificación
- Estadios, Árbitros, Jugadores, Eventos y más

Requiere autenticación por API key, incluida en los headers.

---

## 🔐 Autenticación y formato general

**Todas las peticiones usan el siguiente header:**
```http
x-apisports-key: TU_API_KEY
```

**Todas las respuestas JSON v3** están **anidadas** y organizadas bajo el array `response`.

---

## 🧩 ENDPOINTS FUNDAMENTALES

### 1. `/leagues`
**Obtiene todas las ligas disponibles + temporadas por liga**

📘 Ejemplo de respuesta:
```json
{
  "response": [
    {
      "league": {
        "id": 39,
        "name": "Premier League",
        "type": "League",
        "logo": "https://..."
      },
      "country": {
        "name": "England",
        "code": "GB",
        "flag": "https://..."
      },
      "seasons": [
        {
          "year": 2023,
          "start": "2023-08-12",
          "end": "2024-05-19",
          "current": true,
          "coverage": {
            "fixtures": {
              "events": true,
              "lineups": true,
              "statistics_fixtures": true,
              "statistics_players": true
            },
            "standings": true,
            "players": true
          }
        }
      ]
    }
  ]
}
```

🔁 **Relaciones clave:**
- `League` → `Country`  
- `Season` embebida dentro de la respuesta, se repite por cada año

### 2. `/teams?league=X&season=YYYY`
Devuelve todos los equipos que participaron en una liga y temporada específica.

📘 Ejemplo de respuesta:
```json
{
  "response": [
    {
      "team": {
        "id": 33,
        "name": "Manchester United",
        "code": "MUN",
        "country": "England",
        "founded": 1878,
        "national": false,
        "logo": "https://..."
      },
      "venue": {
        "id": 556,
        "name": "Old Trafford",
        "address": "Sir Matt Busby Way",
        "city": "Manchester",
        "capacity": 74879,
        "surface": "grass",
        "image": "https://..."
      }
    }
  ]
}
```

📌 Observaciones:
- La sede (`venue`) puede relacionarse directamente con `team` (FK o OneToOne)

---

### 3. `/fixtures?league=X&season=YYYY`
Información completa del partido (fecha, equipos, resultado, goles, estado).

📘 Ejemplo de respuesta:
```json
{
  "response": [
    {
      "fixture": {
        "id": 123456,
        "referee": "Anthony Taylor",
        "timezone": "UTC",
        "date": "2024-08-12T18:00:00+00:00",
        "venue": {
          "id": 556,
          "name": "Old Trafford",
          "city": "Manchester"
        },
        "status": {
          "long": "Match Finished",
          "short": "FT",
          "elapsed": 90
        }
      },
      "league": {
        "id": 39,
        "name": "Premier League",
        "country": "England",
        "season": 2023,
        "round": "Regular Season - 1"
      },
      "teams": {
        "home": {
          "id": 33,
          "name": "Manchester United",
          "winner": false,
          "logo": "..."
        },
        "away": {
          "id": 34,
          "name": "Liverpool",
          "winner": false,
          "logo": "..."
        }
      },
      "goals": {
        "home": 2,
        "away": 2
      },
      "score": {
        "halftime": { "home": 1, "away": 1 },
        "fulltime": { "home": 2, "away": 2 },
        "extratime": null,
        "penalty": null
      }
    }
  ]
}
```

📌 Observaciones:
- Este endpoint mezcla información de: fixture, league, teams, venue, score
- Ideal para poblar modelos: `Fixture`, `Team`, `Venue`, `League`, `Season`

---

### 4. `/standings?league=X&season=YYYY`

📘 Ejemplo:
```json
{
  "response": [
    {
      "league": {
        "id": 39,
        "name": "Premier League",
        "season": 2023,
        "standings": [
          [
            {
              "rank": 1,
              "team": {
                "id": 33,
                "name": "Manchester United",
                "logo": "..."
              },
              "points": 79,
              "goalsDiff": 25,
              "all": {
                "played": 38,
                "win": 24,
                "draw": 7,
                "lose": 7,
                "goals": {
                  "for": 78,
                  "against": 53
                }
              },
              "form": "WDLWW"
            }
          ]
        ]
      }
    }
  ]
}
```

📌 Notas:
- Tabla está anidada dentro de `standings` ➜ lista de listas (agrupadas por grupos si hay)
- Puede ser útil desanidar esta estructura al persistirla

---

## 🧠 RESUMEN DE ENTIDADES Y MODELOS PROPUESTOS

| Modelo       | Campos clave                                                                 |
|--------------|-------------------------------------------------------------------------------|
| **Country**  | name, code, flag                                                             |
| **League**   | api_id, name, type, logo, country (FK)                                       |
| **Season**   | year, start, end, current, league (FK)                                       |
| **Team**     | api_id, name, logo, founded, country                                         |
| **Venue**    | api_id, name, city, capacity, surface, team (O2O o FK)                       |
| **Fixture**  | api_id, date, status, referee, home_team, away_team, league, season, venue   |
| **Standing** | rank, team (FK), league (FK), season (FK), puntos, PG, PE, PP, GF, GC, form  |

---

## 🔄 Relaciones del sistema (Diagrama conceptual mejorado)

```plaintext
Country ───< League ───< Season ───< Fixture ──> Venue
   ↑                  ↑                    ↑        ↑
   └──── Team ────────┘                    │        │
        │                                  └────────┘
        └──────> Standing ────>─────────────┘
```

---
### 1. Country (País)
Un país es la entidad base que agrupa varias ligas y equipos.
📌 Ejemplo: Inglaterra ➜ Premier League, Manchester United, Liverpool...

Relación:

Un Country puede tener muchas Leagues

Un Country puede tener muchos Teams

### 2. League (Liga o Copa)
Cada liga pertenece a un país.
📌 Ejemplo: La Premier League pertenece a Inglaterra

Relación:

Una League pertenece a un Country (ForeignKey)

Una League tiene muchas Seasons (temporadas)

### 3. Season (Temporada)
Cada liga se juega durante múltiples temporadas.
📌 Ejemplo: Premier League 2022, Premier League 2023, etc.

Relación:

Una Season pertenece a una League

Una Season contiene muchos Fixtures (partidos)

### 4. Team (Equipo)
Cada equipo pertenece a un país, y juega en ligas durante distintas temporadas.
📌 Ejemplo: Liverpool pertenece a Inglaterra y juega la Premier League 2023

Relación:

Un Team pertenece a un Country

Un Team puede aparecer en muchos Fixtures (como local o visitante)

Un Team tiene una Standing por cada temporada/league combinada

### 5. Fixture (Partido)
Un partido es el evento central del sistema: dos equipos, una liga, una temporada, un resultado, una fecha.

Relaciones:

Un Fixture pertenece a una Season y a una League

Tiene un home_team y un away_team (ambos son Team)

Puede tener un Venue (estadio del partido)

### 6. Venue (Estadio)
Los estadios se pueden vincular tanto a los equipos como a los partidos.

Relación:

Un Venue puede usarse en varios Fixtures

Opcionalmente, puede asociarse a un Team (como estadio local)

### 7. Standing (Clasificación)
Representa la posición de un equipo en una temporada específica.

Relación:

Una Standing pertenece a una Team, una League y una Season

Hay una entrada por equipo en cada jornada/clasificación

## ✅ Resultados de FASE 1

| Aspecto               | Estado |
|------------------------|--------|
| Revisión de estructura JSON de todos los endpoints | ✅ |
| Identificación completa de entidades clave         | ✅ |
| Definición de relaciones y estructuras normalizadas| ✅ |
| Preparación para modelado en Django ORM            | ✅ |

---