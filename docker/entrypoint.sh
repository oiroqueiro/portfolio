 #!/bin/bash

# Set the Elasticsearch password
ELASTIC_PASSWORD=esNre*lLpoeSG5dFXuV

# Reset the password for the 'elastic' user
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic -p $ELASTIC_PASSWORD

# Start the Elasticsearch process
exec /usr/share/elasticsearch/bin/elasticsearch

