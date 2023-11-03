#!/bin/sh

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL	
	CREATE DATABASE portfolio;
	GRANT ALL PRIVILEGES ON DATABASE portfolio TO userpostg;
EOSQL