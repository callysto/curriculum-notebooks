#!/bin/bash

IFS=$'\n'
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "$script_dir"

test_modified="$(git diff --name-only $TRAVIS_COMMIT_RANGE test.sh)"

if [ -z "$TRAVIS_COMMIT_RANGE" ] || [ ! -z "$test_modified" ]; then
    notebooks=($(git ls-files *.ipynb | grep -v \.ipynb_checkpoints))
else
    notebooks=($(git diff --name-only --diff-filter=d $TRAVIS_COMMIT_RANGE | grep \.ipynb$ | grep -v \.ipynb_checkpoints))
fi

retval=0

for notebook in "${notebooks[@]}"; do
    docker run -u "$UID" -v "$script_dir:/notebooks" callysto/pims-r py.test --nbval-lax --disable-pytest-warnings "/notebooks/$notebook"
    [ $? -ne 0 ] && retval=1
done

checkpoint_dirs=($(git ls-files *.ipynb_checkpoints/*))

if [ ${#checkpoint_dirs[@]} -ne 0 ]; then
    echo -e "\n===== These .ipynb_checkpoints directories should not be committed and need to be removed ====="
    echo "${checkpoint_dirs[*]}"
    retval=1
fi

bad_paths=($(git ls-files *.ipynb | grep " "))

if [ ${#bad_paths[@]} -ne 0 ]; then
    echo -e "\n===== Whitespace is not allowed in notebook paths, these files need to be renamed ====="
    echo "${bad_paths[*]}"
    retval=1
fi

exit $retval
