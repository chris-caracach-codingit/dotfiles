# This is my qtile config. It can be used either desktop or laptop. Just check the commented lines.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Window management keybindings
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
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
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Launchers / Killers
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # General
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


# groups = [Group(i) for i in "123456"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# WORK
# color_dark = "#04364A"
# color_middark = "#176B87"
# color_midlight = "#64CCC5"
# color_light = "#DAFFFB"
# color_lighter = "#FFFFFF"

# PERSONAL
color_dark = "#2E073F"
color_middark = "#7A1CAC"
color_midlight = "#AD49E1"
color_light = "#E49BFF"
color_lighter = "#EBD3F8"

layouts = [
    layout.Columns(border_focus_stack=[color_dark, color_dark], border_width=4),
    layout.Max(),
]

widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=12,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(highlight_method="line", active=color_light, block_highlight_text_color=color_light, this_current_screen_border=color_light, inactive=color_dark),
                widget.Sep(foreground=color_light, linewidth=2, padding=20),
                widget.Systray(),
                widget.Sep(foreground=color_light, linewidth=2, padding=20),
                widget.WindowName(foreground=color_light),
                widget.TextBox("TEMP", foreground=color_light),
                widget.ThermalSensor(foreground=color_light),
                widget.Sep(foreground=color_light, linewidth=2, padding=20),
                widget.TextBox("NET", foreground=color_light),
                widget.Net(foreground=color_light, format='{down:.0f}{down_suffix:<2} ↓↑ {up:.0f}{up_suffix:<2}', width=90),
                widget.Sep(foreground=color_light, linewidth=2, padding=20),
                widget.TextBox("RAM", foreground=color_light),
                widget.Memory(measure_mem="G", foreground=color_light),
                widget.Sep(foreground=color_light, linewidth=2, padding=20),
                widget.TextBox("CPU", foreground=color_light),
                widget.CPU(foreground=color_light, format="{load_percent}%", width=40),
                widget.Sep(foreground=color_light, linewidth=2, padding=20),
                widget.TextBox("VOL", foreground=color_light),
                widget.Volume(foreground=color_light),
                # --- LAPTOP --- #
                widget.Sep(foreground=color_light, linewidth=2, padding=20),
                widget.TextBox("BAT", foreground=color_light),
                widget.Battery(charge_char="*", format="{char} {percent:2.0%}"),
                # -------------- #
                widget.Sep(foreground=color_light, linewidth=2, padding=20),
                widget.Clock(format="%Y-%m-%d", foreground=color_light),
                widget.Clock(format="%I:%M %p", foreground=color_light),
            ],
            24,
            # border_width=[2, 2, 2, 2],  # Draw top and bottom borders
            # border_color=[color_dark, color_dark, color_dark, color_dark]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
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
    "nitrogen --restore &",
    "picom &",
]

for x in autostart:
    os.system(x)
