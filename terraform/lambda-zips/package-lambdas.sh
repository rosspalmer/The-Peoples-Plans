#!/bin/bash

# Extract root project directory from current location
pat='^(.+)\/terraform'
 [[ "$PWD" =~ $pat ]]
root="${BASH_REMATCH[1]}"

# Package python lambdas
cd "${root}/packages/peoples-python"
zip -r "${root}/terraform/lambda-zips/python-lambdas.zip" ./*
