#!/bin/bash

# Simple hello world script
# Usage: ./hello.sh [name]

NAME=${1:-"World"}

echo "Hello, $NAME!"
echo "Current date: $(date)"
echo "Current user: $(whoami)"
