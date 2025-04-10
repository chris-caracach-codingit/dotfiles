from libqtile import widget
from colors import color_light, color_dark, color_error

# Current group widget
current_group = widget.AGroupBox(
    foreground=color_light,
    padding=5
)

# Groupbox for workspace management
group_box = widget.GroupBox(
    highlight_method="line",
    active=color_light,
    block_highlight_text_color=color_light,
    this_current_screen_border=color_light,
    inactive=color_dark,
)

# Spacer and system tray
spacer = widget.Spacer()
systray = widget.Systray()

# Separator widget (reusable)
def create_separator():
    return widget.Sep(foreground=color_light, linewidth=1, padding=20)

# Temperature widgets
temp_icon = widget.TextBox("\uef2b", foreground=color_light, fontsize=26)
temp_sensor = widget.ThermalSensor(
    foreground=color_light,
    threshold=90,
    foreground_alert=color_error
)

# Network widgets
net_icon = widget.TextBox(
    "\ueb01",
    foreground=color_light,
    fontsize=26,
)
net_widget = widget.Net(
    foreground=color_light,
    format="{down:.0f}{down_suffix:<2} ↓↑ {up:.0f}{up_suffix:<2}",
    width=110,
)

# RAM widgets
ram_icon = widget.TextBox(
    "\uefc5", 
    foreground=color_light, 
    fontsize=26, 
)
ram_widget = widget.Memory(measure_mem="G", foreground=color_light)

# CPU widgets
cpu_icon = widget.TextBox("\ue28c", foreground=color_light, fontsize=26)
cpu_widget = widget.CPU(foreground=color_light, format="{load_percent}%", width=45)

# Volume widgets
volume_icon = widget.TextBox("\uf028", foreground=color_light, fontsize=26)
volume_widget = widget.PulseVolume(foreground=color_light)

# Battery widgets
battery_icon = widget.TextBox("\uf242", foreground=color_light, fontsize=30)
battery_widget = widget.Battery(
    charge_char="*",
    format="{char} {percent:2.0%}",
    foreground=color_light,
    low_foreground=color_error,
    discharge_char=""
)

# Clock widgets
date_icon = widget.TextBox("\uf073", foreground=color_light, fontsize=26)
date_widget = widget.Clock(format="%d-%m", foreground=color_light)
time_widget = widget.Clock(format="%I:%M %p", foreground=color_light)

# Keyboard widget
keyboard_icon = widget.TextBox("\uf11c", foreground=color_light, fontsize=26)

def init_widgets_list(keyboard_widget):
    """Initialize and return the widgets list with all widgets"""
    widgets = [
        spacer,
        systray,
        create_separator(),
        temp_icon,
        temp_sensor,
        create_separator(),
        net_icon,
        net_widget,
        create_separator(),
        ram_icon,
        ram_widget,
        create_separator(),
        cpu_icon,
        cpu_widget,
        create_separator(),
        volume_icon,
        volume_widget,
        create_separator(),
        battery_icon,
        battery_widget,
        create_separator(),
        date_icon,
        date_widget,
        time_widget,
        create_separator(),
        keyboard_icon,
        keyboard_widget,
    ]
    return widgets
