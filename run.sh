docker network create -d bridge task
cd controller/ && docker build -t controller .
docker run -d --name controller --network task controller
cd ..
docker-compose -f sensors/dc-sensors.yaml build
docker-compose -f sensors/dc-sensors.yaml up