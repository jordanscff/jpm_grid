# Grid Demo

This is a simple full stack Flask web app that renders a dynamic table (grid) based on API-driven configuration.

---

## Tech Stack

- Python 3.11
- Flask
- Jinja2
- Flasgger (Swagger UI)
- Docker
- Pytest

---

## Running the App

Make sure Docker is installed, then from the project directory:

```bash
docker build -t grid-app .
docker run -p 5001:5000 grid-app
```

---

## Access the App

| Feature       | URL                                 |
|---------------|-------------------------------------|
| Grid view     | http://localhost:5001/grid          |
| Example 2     | http://localhost:5001/grid?example=2|
| Config API    | http://localhost:5001/config        |
| Data API      | http://localhost:5001/data          |
| Swagger Docs  | http://localhost:5001/apidocs       |

---

## Running Tests

```bash
docker run -it grid-app pytest
```

---

## Notes
- No database is used — data is mocked in Python
- No frontend framework — server-rendered HTML via Jinja2
- Uses internal functions for config/data instead of self-calling HTTP routes

