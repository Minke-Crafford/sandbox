#!/bin/bash

# File and directory utilities
# Source this file in other scripts: source utils/file-utils.sh

# Check if a file exists
file_exists() {
    [ -f "$1" ]
}

# Check if a directory exists
dir_exists() {
    [ -d "$1" ]
}

# Create directory if it doesn't exist
ensure_dir() {
    local dir="$1"
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "Created directory: $dir"
    fi
}

# Get file size in human-readable format
get_file_size() {
    if [ -f "$1" ]; then
        du -h "$1" | cut -f1
    else
        echo "File not found"
    fi
}

# Count files in a directory
count_files() {
    local dir="${1:-.}"
    if [ -d "$dir" ]; then
        find "$dir" -type f | wc -l
    else
        echo "0"
    fi
}
