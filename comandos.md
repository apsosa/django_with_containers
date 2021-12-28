

docker-compose -f local.yml up
docker-compose -f local.yml down

export COMPOSE_FILE=local.yml

Con rm mata el docker al final de la ejecucion
docker-compose run --rm django python manage.py <comando>

Habilitar debugguer 
docker-compose up
docker-compose ps
docker rm -f <ID>

$ docker-compose run --rm --service-ports django


Para corre django de manera independiente:
consola 1:

  docker-compose up
consola 2:

  docker-compose ps
  docker rm -f <name>
  docker-compose run --rm --service-ports django