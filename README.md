# Python Celery example
- Insure `flask db upgrade`
# Build redis container
```shell
docker run -p 6379:6379 --name celery-redis -d redis
```
# Test redis
```shell
docker exec -it celery-redis redis-cli ping
```
# Flower setup 
```shell
celery -A worker.celery flower --port=5555
```
# Run worker - Windows
```shell
celery -A worker.celery worker --loglevel=info -P threads
```