#!/bin/bash

declare -A cli
cli[git]="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git"
cli[npm]="https://nodejs.org/en/"
cli[cdk]="https://docs.aws.amazon.com/cdk/latest/guide/cli.html"
cli[aws]="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html"
cli[curl]="https://curl.haxx.se/download.html"
cli[python3]="https://www.python.org/downloads/"

for i in ${!cli[*]}
do 
    if ! command -v ${i}> /dev/null
    then
        echo "Checking CLI: ${i} could not be found - Installation link: ${cli[${i}]}"
    else
        echo "CLI: ${i} -- OK "
    fi
done
echo ""
echo "This script doesn't check if you have properly configured the required tools. "
echo "Please refer to the section FIRST, THING FIRST on main README.md file for further information."