#!/bin/bash

IFS=$'\n'
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "$script_dir"

test_modified="$(git diff --name-only $TRAVIS_COMMIT_RANGE test.sh)"

if [ -z "$TRAVIS_COMMIT_RANGE" ] || [ ! -z "$test_modified" ]; then
    notebooks=($(git ls-files *.ipynb | grep -v \.ipynb_checkpoints))
else
    notebooks=($(git diff --name-only $TRAVIS_COMMIT_RANGE | grep \.ipynb$ | grep -v \.ipynb_checkpoints))
fi

retval=0

for notebook in "${notebooks[@]}"; do
    docker run -v "$script_dir:/notebooks" callysto/pims-r py.test --nbval-lax "/notebooks/$notebook"
    [ $? -ne 0 ] && retval=1
done

exit $retval
