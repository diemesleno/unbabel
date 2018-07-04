#!/bin/bash

echo "====================================================="
echo "Please, wait while I configure the environment"
echo "====================================================="

echo "Cloning proccess finished"

echo "Buiding with the docker, soon you can access on http://localhost:8000 "

docker-compose up --build

echo "Finsished docker proccess"

echo "====================================================="
echo " Thank you! "
echo "====================================================="
