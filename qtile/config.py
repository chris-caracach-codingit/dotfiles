# This is my qtile config. It can be used either desktop or laptop. Just check the commented lines.
#
# Version 1.2.0 - 26/12/24

#|--- IMPORTS ---|#
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from keyboard_utils import get_layout, toggle_layout
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
    
    # Aumentar brillo
    Key([mod], "k", lazy.spawn("brightnessctl set +10%"), desc="Increase brightness"),
    
    # Disminuir brillo
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

#|--- KEYBOARD WIDGET ---|
keyboard_widget = widget.TextBox(
    text=f"{get_layout()}",  
    mouse_callbacks={"Button1": lazy.function(toggle_layout)},
    foreground=color_light,
    padding=5
)

layouts = [
    layout.Columns(border_focus_stack=[color_dark, color_dark], border_width=4),
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
                *init_widgets_list(keyboard_widget)
            ],
            30,
            border_width=[0, 0, 1, 0],  
            border_color=[color_dark, color_dark, color_light, color_dark]  
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

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

autostart = [
    # "nitrogen --restore &",
    "picom &",
    "nm-applet &",
    "~/.config/qtile/check_monitors.sh" # This checks the HDMI screen, comment if you're not using it
]

for cmd in autostart:
    subprocess.Popen(cmd, shell=True)
