#!/bin/bash


# Extend sys.path with ./src path - enables running pytest directly on source code
while read -r file; do
	sed -i '1s/^/\n/' "$file"
	sed -i '1s/^/sys.path.append(src_path)\n/' "$file"
	sed -i '1s/^/src_path = os.path.join(os.path.abspath(__file__).rsplit(os.sep, 4)[0], "src")\n/' "$file"
	sed -i '1s/^/import sys\n/' "$file"
	sed -i '1s/^/import os\n/' "$file"
done < <(git ls-files tests/**/*.py)

while read -r file; do
        sed -i '1s/^/\n/' "$file"
        sed -i '1s/^/sys.path.append(src_path)\n/' "$file"
        sed -i '1s/^/src_path = os.path.join(os.path.abspath(__file__).rsplit(os.sep, 4)[0], "src")\n/' "$file"
        sed -i '1s/^/import sys\n/' "$file"
        sed -i '1s/^/import os\n/' "$file"
done < <(git ls-files tests/**/**/*.py)

# Remove application name from import statements - enables source code execution and running pylint
# directly on source code
while read -r file; do
	sed -i 's/ingestation\.modules/modules/g' "$file"
done < <(git ls-files '*.py')
