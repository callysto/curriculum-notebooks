#!/bin/bash

IFS=$'\n'
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
notebook_dir="$(basename $script_dir)"
mount_point=/callysto

cd "$script_dir"

test_modified="$(git diff --name-only $COMMIT_RANGE test.sh)"

if [ -z "$COMMIT_RANGE" ] || [ ! -z "$test_modified" ]; then
    notebooks=($(git ls-files '*.ipynb' | grep -v \.ipynb_checkpoints))
else
    notebooks=($(git diff --name-only --diff-filter=d $COMMIT_RANGE | grep \.ipynb$ | grep -v \.ipynb_checkpoints))
fi

# Copy notebooks to a volume and chown them to avoid permissions issues
vid=$(docker volume create)
cid=$(docker create -v "$vid:$mount_point" callysto/pims-r)
docker cp "$script_dir" "$cid:$mount_point"
docker rm $cid > /dev/null
docker run --rm -u root -v "$vid:$mount_point" callysto/pims-r chown -R jupyter "$mount_point/$notebook_dir"

retval=0

for notebook in "${notebooks[@]}"; do
    docker run --rm -v "$vid:$mount_point" callysto/pims-r py.test --nbval-lax --disable-pytest-warnings "$mount_point/$notebook_dir/$notebook"
    [ $? -ne 0 ] && retval=1
done

docker volume rm $vid > /dev/null

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
