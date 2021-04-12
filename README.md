# ETL DATA PROCESSOR
DS 3003 Project

The data processed in this ETL Data Processor contains records of Olympic medals that have been won from 1924 to 2006. It also provides information about the location the Olympics was held at, what type of medal was won, the event type and discipline, and more. 

This container performs part of the ETL pipeline process and completes the following: 
- remotely fetches Olympic medal data from a url as a csv file
- removes the 'Discipline' and 'Event' columns
- provides summary information regarding medals won by the USA
- converts the csv file to a json file
- writes the file to disk.

How to use this container?

Directions: 

1. Open up command prompt. 
2. Type this line into the command prompt and press enter:

	docker pull sejalpatrikar/etlserver:latest
	
   This can also be found at https://hub.docker.com/r/sejalpatrikar/etlserver/tags?page=1&ordering=last_updated

3. Retrieving json file??
