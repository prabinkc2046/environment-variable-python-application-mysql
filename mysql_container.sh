docker run -d --name localhost -e MYSQL_ROOT_PASSWORD=prabin123 \
-e MYSQL_USER=python -e MYSQL_PASSWORD=python -e MYSQL_DATABASE=database \
--network host mysql:latest
