#!/bin/bash
docker run -t -i -v $(pwd)/data:/code/data open-elevation /code/create-dataset.sh
