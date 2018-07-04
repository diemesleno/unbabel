#!/bin/bash

echo "====================================================="
echo "Please, wait while I configure the environment"
echo "====================================================="

echo "Cloning proccess finished"

echo "Buiding with the docker"

docker-compose up --build

echo "Finsished docker proccess"

echo "Performing some tests"

docker-compose exec website py.test project/tests

echo "Tests finished"

echo "====================================================="
echo "Done! You can now access  http://localhost:8000 and try the app"
echo "====================================================="
