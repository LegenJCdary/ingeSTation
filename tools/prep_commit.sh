#!/bin/bash


# Revert steps performed in prep_test.sh - remove sys.path extension from test scripts and add
# application name to import statements.

while read -r file; do
	for x in {1..5}; do
		sed -i '1d' "$file"
	done
done < <(git ls-files tests/**/*.py)

while read -r file; do
	for x in {1..5}; do
		sed -i '1d' "$file"
	done
done < <(git ls-files tests/**/**/*.py)

while read -r file; do
	sed -i 's/modules/ingestation\.modules/g' "$file"
done < <(git ls-files '*.py')
