#!/bin/sh
# Rudimentary script for generating dist files and uploading them to PyPi. Will prompt for PyPi credentials.

python -m build
twine upload dist/*