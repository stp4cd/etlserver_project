# ETL DATA PROCESSOR
DS 3003 Project

This container performs part of the ETL pipeline and completes the following: 
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
