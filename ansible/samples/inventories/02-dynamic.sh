#!/bin/bash

if [[ "$1" == "--list" ]]; then
    cat << EOF
{
    "targets": {
        "hosts": [
            "192.168.122.161"
        ]
    }
}
EOF
elif [[ "$1" == "--host" ]]; then
    echo "{}"
else
    echo "Usage: $0 --list | --host <hostname>"
    exit 1
fi
