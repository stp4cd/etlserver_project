# ETL DATA PROCESSOR
DS 3003 Project

The data processed in this ETL Data Processor contains records of Olympic medals that have been won from 1924 to 2006. It also provides information about the location the Olympics was held at, what type of medal was won, the event type and discipline, and more. 

This container performs part of the ETL pipeline process and completes the following: 
- Remotely fetches Olympic medal data from a url as a csv file
- Removes the 'Discipline' and 'Event' columns
- Provides summary information regarding medals won by the USA
- Converts the csv file to a json file
- Writes the file to disk

How to use this container?

Directions: 

1. Open up command prompt. 
2. Type this line into the command prompt and press enter:

	docker pull sejalpatrikar/etlserver:latest
	
   This can also be found at https://hub.docker.com/r/sejalpatrikar/etlserver/tags?page=1&ordering=last_updated

3. Then type the following as your next command in your command prompt:

        docker run --name <the_image_name> -d -p 5000:5000 sejalpatrikar/etlserver
	
	curl http://localhost:5000
	
	docker logs <the_image_name> > output.log
        
    The file "output.log" contains the output of the script. 
    
4. Retrieve the JSON file
        
	docker cp <the_image_name>:/code/usa_2006.json
   
    The file written by the container is "usa_2006.json".
