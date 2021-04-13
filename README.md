# ETL DATA PROCESSOR
DS 3003 Project

The data processed in this ETL Data Processor contains records of Olympic medals that have been won from 1924 to 2006. It also provides information about the location the Olympics was held at, what type of medal was won, the event type and discipline, and more. 

This container performs part of the ETL pipeline process and completes the following: 
- Remotely fetches Olympic medal data from a url as a csv file
- Removes the 'Discipline' and 'Event' columns
- Provides summary information regarding medals won by the USA in 2006
- Converts the csv file to a json file
- Writes the file to disk

# How to use this container?

Directions: 

1. Open up command prompt. 
2. Type this line into the command prompt to pull the container:
	```
	docker pull sejalpatrikar/etlserver:latest
	```
   This can also be found at https://hub.docker.com/r/sejalpatrikar/etlserver/tags?page=1&ordering=last_updated

3. Then, run the container in detached mode using the following command:

        docker run --name <the_container_name> -d -p 5000:5000 sejalpatrikar/etlserver

4. The container should be accessible on port 5000. Use following command: 
	```
	curl http://localhost:5000
	```
5. The logs can be viewed using the following command: 
	```
	docker logs <the_container_name> > output.log
	```
   The file "output.log" contains the stdout output of the script.
                
6. The file written by the container is "usa_2006.json". Retrieve the JSON file using the following command:
	```
	docker cp <the_container_name>:/code/usa_2006.json .
	```

   
   
