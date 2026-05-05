autostart = [
    "dunst &",  # Notifications
    "picom &",  # Compositor
    "nm-applet &",  # Network manager
    "setxkbmap latam &",  # Set keyboard layout to latam
    "sh ~/.config/qtile/scripts/check_monitors.sh",  # This checks the HDMI screen, comment if you're not using it
    "nitrogen --restore &",  # Restore wallpaper
]
