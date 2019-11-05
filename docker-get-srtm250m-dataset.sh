#!/bin/bash
mkdir data
docker run -t -i -v $(pwd)/data:/code/data open-elevation /code/create-dataset.sh
