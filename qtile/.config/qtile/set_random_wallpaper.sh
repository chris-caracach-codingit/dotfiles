#!/bin/bash

WALLPAPER_DIR="$HOME/wallpapers"

RANDOM_WALLPAPER=$(find "$WALLPAPER_DIR" -type f | shuf -n 1)

nitrogen --set-zoom-fill "$RANDOM_WALLPAPER"