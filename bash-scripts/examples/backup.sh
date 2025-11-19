#!/bin/bash

# File backup script
# Usage: ./backup.sh <source_file> [destination_directory]

set -e  # Exit on error

SOURCE_FILE="$1"
DEST_DIR="${2:-.}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

if [ -z "$SOURCE_FILE" ]; then
    echo "Error: No source file specified"
    echo "Usage: $0 <source_file> [destination_directory]"
    exit 1
fi

if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: Source file '$SOURCE_FILE' does not exist"
    exit 1
fi

if [ ! -d "$DEST_DIR" ]; then
    echo "Error: Destination directory '$DEST_DIR' does not exist"
    exit 1
fi

FILENAME=$(basename "$SOURCE_FILE")
BACKUP_NAME="${FILENAME}_backup_${TIMESTAMP}"
BACKUP_PATH="${DEST_DIR}/${BACKUP_NAME}"

echo "Backing up '$SOURCE_FILE' to '$BACKUP_PATH'..."
cp "$SOURCE_FILE" "$BACKUP_PATH"

echo "Backup complete!"
echo "Backup location: $BACKUP_PATH"
