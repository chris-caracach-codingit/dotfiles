#!/bin/bash

# Directories
DOTFILES_DIR="$HOME/dotfiles"
QTILE_DIR="$DOTFILES_DIR/qtile/.config/qtile"
QTILE_TARGET="$HOME/.config/qtile"
CONFIG_FILE="config.py"

# Copy qtile config
if [[ -f "$QTILE_DIR/$CONFIG_FILE" ]]; then
    echo "Copying $CONFIG_FILE from $QTILE_DIR to $QTILE_TARGET..."

    # Ensure the target directory exists
    mkdir -p "$QTILE_TARGET"

    # Copy the file
    cp "$QTILE_DIR/$CONFIG_FILE" "$QTILE_TARGET/"

    if [[ $? -eq 0 ]]; then
        echo "Successfully copied $CONFIG_FILE to $QTILE_TARGET."
    else
        echo "Failed to copy $CONFIG_FILE." >&2
        exit 1
    fi
else
    echo "Error: $CONFIG_FILE not found in $QTILE_DIR." >&2
    exit 1
fi

# Execute stow for all folders except qtile
cd "$DOTFILES_DIR" || { echo "Failed to change directory to $DOTFILES_DIR." >&2; exit 1; }

for folder in */; do
    folder_name="${folder%/}"
    if [[ "$folder_name" != "qtile" ]]; then
        echo "Running stow for $folder_name..."
        stow "$folder_name"
        if [[ $? -eq 0 ]]; then
            echo "Successfully stowed $folder_name."
        else
            echo "Failed to stow $folder_name." >&2
        fi
    fi
done

