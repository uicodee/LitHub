# FastAPI Template
Simple FastAPI template using Domain Driven Design Hexagon

To run this example - create .env file and fill, then use:
```
docker-compose up --build -d
```

To run migrations:
```
alembic revision --autogenerate -m "init"
```
```
alembic upgrade head
```