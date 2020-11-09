#!/bin/bash

declare -A cli
cli[git]="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git"
cli[npm]="https://nodejs.org/en/"
cli[cdk]="https://docs.aws.amazon.com/cdk/latest/guide/cli.html"
cli[aws]="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html"
cli[curl]="https://curl.haxx.se/download.html"
cli[artillery]="https://artillery.io/docs/guides/getting-started/installing-artillery.html"
cli[python]="https://www.python.org/downloads/"

for i in ${!cli[*]}
do 
    if ! command -v ${i}> /dev/null
    then
        echo "Checking CLI: ${i} could not be found - Installation link: ${cli[${i}]}"
    else
        echo "CLI: ${i} -- OK "
    fi
done

