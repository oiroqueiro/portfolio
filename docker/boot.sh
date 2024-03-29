#!/bin/sh

set -e

# Merging host directory to the container directory

cp -r mounted/img/ portfolio/static/
cp -f mounted/content.xlsx ./content.xlsx

while true; do
    # Attempt to perform database migrations
    flask db upgrade

    # Check for errors
    if [ $? -eq 0 ]; then
        # Check if UPDATE_DATA is set to True
        if [ "$UPDATE_DATA" = "True" ]; then
            # Insert data
            python /portfolio/insert_data.py
            echo "Data insertion completed successfully."
        else
            echo "UPDATE_DATA is not set to True. Skipping data insertion."
        fi
        break # Exit the loop
    else
        echo "Error during database migrations. Retry in 5 seconds"
        sleep 5        
    fi
done

exec gunicorn -b :5000 --access-logfile - --error-logfile - portfolio:portfolio
