docker network create -d bridge task

cd manipulator/ && docker build -t manipulator .
docker run -d --name manipulator --network task manipulator
cd ..

cd controller/ && docker build -t controller .
docker run -d --name controller --network task controller
cd ..

docker-compose -f sensors/dc-sensors.yaml build
docker-compose -f sensors/dc-sensors.yaml up

docker logs controller
docker logs manipulator > manipulator.log

docker stop controller manipulator
docker rm controller
docker rm manipulator