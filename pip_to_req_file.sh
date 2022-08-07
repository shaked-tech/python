#!/bin/bash

## Optional: ########################
# Given version of Package
version="${2}"
# Path to the requirments file
req_file='./requirments.txt'
# Non empty value will create a backup file got 'requitments.txt' with the given suffix
backup_suffix=''
#####################################

# Package name to be installed by pip
lib="${1}"

## Check if file has an empty line at the end
req_last_line=$(tail -1 ${req_file} | cat -e)
if [[ "${req_last_line}" != *$ ]]; then
    add="\n"
else
    add=''
fi
# echo "last line: ${req_last_line}, (add: '${add}')" 

# Edit verison for pip install
if [[ ${version} ]]; then
    install_version="==$version"
fi

echo "Installing ${1}${install_version}"
pip install ${1}${install_version}

version=$(pip show ${1} | grep 'Version:' | cut -d' ' -f2)

if [[ $(grep ${1} ${req_file}) ]]; then
    echo "chaning in file (s/${1}.*/${1}${install_version}/)"
    sed -i"${backup_suffix}" "s/${1}.*/${1}${install_version}/" ${req_file}
else
    echo "Creating new Requirments file (${req_file})"
    printf "${add}${1}==${version}" >> ${req_file}
fi

echo "added ${1}==${version} to ${req_file} file"
