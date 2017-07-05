git clone https://github.com/gtesseyre/docker-images.git

### List running containers 
	docker ps 

### List container images store locally 
	docker images 

### Run a container 
	docker run --name docker-web-server -d -p 8080:80 gtesseyre/docker-web-server:1.0

### Execute a shell in a container
	docker exec -it docker-web-server bash 

### Look at a container logs 
	docker logs docker-web-server

### Inspect a container 
	docker inspect docker-web-server

### Stop a container 
	docker stop docker-web-server

### List all containers including the stopped ones 
	docker ps -a

### Delete a container
	docker rm docker-web-server

### Build a container 
	docker build -t gtesseyre/docker-web-server:latest .

### Push container to DockerHub 
	docker push gtesseyre/docker-web-server:latest
