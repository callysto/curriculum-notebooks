#!/bin/bash

if [ -z "$TRAVIS_COMMIT_RANGE" ]; then
    notebooks=($(git ls-files *.ipynb | grep -v \.ipynb_checkpoints))
else
    notebooks=($(git diff --name-only $TRAVIS_COMMIT_RANGE | grep \.ipynb$))
fi

for notebook in ${notebooks[@]}; do
    docker run -v $TRAVIS_BUILD_DIR:/notebooks callysto/pims-r py.test --nbval-lax "/notebooks/$notebook"
done
