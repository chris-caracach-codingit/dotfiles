# This is my qtile config. It can be used either desktop or laptop. Just check the commented lines.
#
# Version 2.0.0 - 1/4/25


#|--- TODO ---|#
# - Find a way to define a name for each group and display the group name in top bar, instead of 123456789
# - Move keys to a separated file
# - Move layouts to a separated file
# - Add a way to execute this script (record screen)
# ffmpeg -f pulse -i alsa_input.pci-0000_00_1f.3.analog-stereo -f x11grab -framerate 30 -video_size 1920x1080 -i :0.0 ~/Videos/record.mkv






#|--- IMPORTS ---|#
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from colors import *
from widgets import init_widgets_list
import subprocess
import os

mod = "mod4"
terminal = guess_terminal()

#|--- KEYS ---|#
keys = [
    # Window management keybindings
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    
    # Brightness
    Key([mod], "k", lazy.spawn("brightnessctl set +10%"), desc="Increase brightness"),
    Key([mod], "l", lazy.spawn("brightnessctl set 10%-"), desc="Decrease brightness"),
    
    # Launchers / Killers
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "p", lazy.spawn("flameshot gui"), desc="Launch Flameshot"),

    # General
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = [Group(i) for i in "123456789"]

#|--- SOME GROUP SHORTCUTS ---|
keys.append(Key([mod], "c", lazy.group["1"].toscreen()))
keys.append(Key([mod], "z", lazy.group["2"].toscreen()))
keys.append(Key([mod], "a", lazy.group["4"].toscreen()))
keys.append(Key([mod], "d", lazy.group["6"].toscreen()))
keys.append(Key([mod], "x", lazy.group["7"].toscreen()))
keys.append(Key([mod], "s", lazy.group["8"].toscreen()))
keys.append(Key([mod], "m", lazy.group["9"].toscreen()))

#|--- SWITCH TO ANOTHER GROUP ---|
for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

#|--- LAYOUTS ---|
layouts = [
    layout.Columns(
        border_focus_stack=[color_dark, color_dark], 
        border_width=3,
        border_normal=color_dark,
        border_focus=color_light
        ),
    layout.Max(),
]

widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=14,
    padding=4,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                *init_widgets_list()
            ],
            30,
            border_width=[2, 2, 2, 2],
            border_color=[color_light, color_light, color_light, color_light]  
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"

autostart = [
    "picom &",
    "nm-applet &",
    "~/.config/qtile/check_monitors.sh" # This checks the HDMI screen, comment if you're not using it
    "~/.config/qtile/set_random_wallpaper.sh" # This sets a random wallpaper
]

for cmd in autostart:
    subprocess.Popen(cmd, shell=True)
