#begin python

def BINDALL(blocks,modifier="",postfix="",prefix=""):
    string = ""
    for name in blocks:
        string += " # {}\n".format(name)
        x = blocks[name]
        if type(x) == tuple:
            string += BIND(x,modifier,postfix,prefix)
        elif type(x) == list:
            for t in blocks[name]:
                string += BIND(t,modifier,postfix,prefix)
    return string

def BIND(t,mod,post,pre):
    x,y = t
    if pre != "": pre = pre + " "
    if post != "": post = "; " + post
    if mod != "":  mod += "+"
    return "bindsym {} {}\n".format(mod+x,y+post)

#end python
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #                               SETTINGS                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # This font is widely installed, provides lots of unicode glyphs, right-to-left
 # text rendering and scalability on retina/hidpi displays (thanks to pango).
font pango:DejaVu Sans Mono 8

 # Use Mouse+Mod1 to drag floating windows to their wanted position
floating_modifier Mod1

 # no title-bars nor border
new_window pixel 0

 # no floating border
new_float pixel 0

 # go back to previous workspace if you try to go to the current one
 # (allow for fast window movement to a workspace and back)
workspace_auto_back_and_forth yes

 # focus on mouse (is a pain if you happen to have a mouse)
focus_follows_mouse no

 # I like the original snake better
focus_wrapping no

 # smart|ignore|leave_fullscreen
popup_during_fullscreen leave_fullscreen

 # smart|urgent|focus|none
focus_on_window_activation none

 # # # # # # # # # # # # # # # # # COLORS  # # # # # # # # # # # # # # # # # # # 

 # class                 border  backgr. text    ind.    child
client.focused          #4CC97E #4CC97E #ffffff #4CC97E #4CC97E
client.focused_inactive #222222 #222222 #ffffff #222222 #222222
client.unfocused        #222222 #222222 #888888 #222222 #222222
client.urgent           #222222 #900000 #ffffff #900000 #900000
client.placeholder      #000000 #222222 #ffffff #000000 #222222

client.background       #222222

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 #                              DEFINITIONS                                    #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

 # The (new) i3-dmenu-desktop which only displays applications
 # shipping a .desktop file. It is a wrapper around dmenu, so you need that
 # installed.
 # Since it's slow as **** someone made a fast one:
 # https://github.com/matteoalessiocarrara/k5-dmenu-desktop
set $dmenu i3-dmenu-desktop   # ~/k5-dmenu-desktop

 # file manager
set $fm nautilus -w

 # for brevity
set $exec exec --no-startup-id
set $exec_always exec_always --no-startup-id
set $alert notify-send --expire-time=1200
set $refresh_status_bar exec killall -USR1 i3status
set $focus_all focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent; focus parent
set $focus_one focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child ; focus child
set $no_border [tiling] border none
set $border [tiling] border pixel 5
set $alt_gr "ISO_Level3_Shift"

 # # # # # # # # # # # # # # # # KEYBINDINGS # # # # # # # # # # # # # # # # # # 

set $disable_Caps setxkbmap -option ctrl:nocaps
set  $enable_Caps setxkbmap -option
set $disable_hover_mode ~/.bin/hover.sh 0
set  $enable_hover_mode ~/.bin/hover.sh 1

 # # # # # # # # # # # # # # # FUNCTIONALITIES # # # # # # # # # # # # # # # # #

 # touchpad toggle
set $touchpad_on ~/.bin/touchpad_toggle.sh 1 & xdotool mousemove  750  350
set $touchpad_off ~/.bin/touchpad_toggle.sh 0 & xdotool mousemove 2500 1200
set $touchpad_off_2 ~/.bin/touchpad_toggle.sh 0
set $touchpad_toggle ~/.bin/touchpad_toggle.sh

 # autoscroll
set $disable_autoscroll ~/.bin/autoscroll.sh 0
set  $enable_autoscroll ~/.bin/autoscroll.sh 1

 # screenshot
set $stamp "import ~/Pictures/latest-screenshot.png; xdg-open ~/Pictures/latest-screenshot.png"

 # brightness
set $brightness_up exec "xbacklight -inc 5; notify-send 'brightness up'"
set $brightness_down exec "xbacklight -dec 5; notify-send 'brightness down'"

 # # # # # # # # # # # # # # # # WORKSPACES # # # # # # # # # # # # # # # # # # #
#begin python

WORKSPACES = [    
("1nternet", ("$w1","1")),
("2rectory", ("$w2","2")),
("3code",    ("$w3","3")),
("4terminl", ("$w4","4")),
("5team",    ("$w5","5")),
("6iscord",  ("$w6","6")),
("7atex",    ("$w7","7")),
("8volante", ("$w8","8")),
("9imp",     ("$w9","9"))]
        
CUT_WORKSPACE = \
("X",        ("$wx","x")) 


def SETALL(l):
    string=""
    for x in l:
        string += SET(x)
    return string

def SET(x):
    name,t = x
    return "set {} {}\n".format(t[0],name)

#end python

<[SETALL(WORKSPACES)]>
 # this one is for cut and paste
<[SET(CUT_WORKSPACE)]>
 # # # # # # # # # # # # # # # # LAYOUTS # # # # # # # # # # # # # # # # # # # # 

set $layout_1 i3-msg 'workspace --no-auto-back-and-forth 1nternet; split h; focus parent; focus parent; focus parent; focus parent; kill; append_layout ~/.workspaces/1nternet.json'
set $layout_2 i3-msg 'workspace --no-auto-back-and-forth 2rectory; split h; focus parent; focus parent; focus parent; focus parent; focus parent; kill; append_layout ~/.workspaces/2rectory.json'

set $fill_1 chromium --new-window --profile-directory=Default https://web.telegram.org/ https://web.whatsapp.com/ & sleep 0.75; chromium --new-window --profile-directory=Default https://mail.google.com/mail/u/0/ https://mail.google.com/mail/u/1/ https://calendar.google.com/calendar/ & sleep 0.75; chromium --new-window --profile-directory=Default https://keep.google.com/u/0/ https://getpocket.com/a/queue/list/
 # set $fill_2 nautilus -w & nautilus -w Downloads & emacs ~/memo & chromium --new-window --profile-directory=Default https://github.com/Kappanneo https://gitlab.com/kappanneo & gnome-terminal
set $fill_2 nautilus -w & nautilus -w Downloads & emacs ~/memo & chromium --new-window --profile-directory=Default https://observablehq.com/@kappanneo & gnome-terminal

 # # # # # # # # # # # # # # # # # MODES # # # # # # # # # # # # # # # # # # # # #

 # [poweroff] to disable standard poweroff: in /etc/systemd/logind.conf set HandlePowerKey=ignore
set $pow "POWER: [q]uit  [r]estart  [s]uspend  [e]xit  [esc]"

 # [space] basic mode
set $bas "BASIC: writing enabled  [super] select container  [super+space] hover mode"
set $def "default"

 # [super+space] hovering mode
set $hov "HOVER: writing disabled  [oklò] move cursor  [0] insert  [space|esc] exit mode"

 # [super] super mode
set $sup "SUPER: [wasd|oklò] select  [shift] move  [123] workspace  [space|esc] exit mode"

 # # # # # # # # # # # # # # # # SUB-MODES # # # # # # # # # # # # # # # # # # # 

 # [super+z] (start) layout
set $str "START: [1|2] layouts  [space|esc] exit mode"

 # [super+r] redshift
set $red "REDSH: [123] shift red level  [+] increase  [space|esc] exit mode"

 # [super+c] configuration
set $cnf "CONFG: [c]onfigure i3  .git[i]gnore  [a]pplications  [e]macs  [s]tatusbar  [z]sh  [g]uide  [1|2|l]ayouts  [y]aourt  [r]edshift  [space|esc] exit mode"

 # # # # # # # # # # # # # # # #ON-NEW-WINDOW # # # # # # # # # # # # # # # # # #

for_window [class="."] floating disable split toggle; mode $def $no_border; fullscreen disable; $exec $disable_hover_mode & $alert $bas

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 #                               COMMANDS                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#begin python
TOP_COMMANDS={   

"touchpad toggle":
    ("XF86TouchpadToggle","$touchpad_toggle"),

"screen brightness controls":[
    ("XF86MonBrightnessUp","$brightness_up"),
    ("XF86MonBrightnessDown","$brightness_down")
],

"screenshot":
    ("--release Shift+Print","$exec $stamp"),

"display": #TODO
    ("XF86Display", "$exec xrandr --output eDP1 --mode 1920x1080 --preferred")

}

#end python
<[BINDALL(TOP_COMMANDS)]>
 # # # # # # # # # # # # # # # MOD1-COMMANDS # # # # # # # # # # # # # # # # # #

#begin python
ALT_COMMANDS={

"kill":
    ("F4","kill"),

"browse workspaces":[
    ("Tab","workspace next"),
    ("Shift+Tab","workspace prev")
]
    
}

#end python
<[BINDALL(ALT_COMMANDS,"Mod1","$refresh_status_bar")]>
 # # # # # # # # # # # # # # # MOD4-COMMANDS # # # # # # # # # # # # # # # # # #

#begin python
SUPER_COMMANDS = {
    
"open terminal":
    ("Return","$exec gnome-terminal"),

"open emacs":
    ("e","exec emacs"),

"start dmenu for applications":[
    ("Menu","$exec $dmenu"),
    ("Shift+exclam","$exec $dmenu")
],

"fullscreen":[
    ("f","fullscreen toggle"),
    ("Shift+f",'$exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"')
],
    
"split toggle":
    ("g","split v; focus parent; layout toggle split; focus child"),

"resize window":[
    ("m",      "resize shrink height 5 px or 1 ppt"),
    ("p",      "resize  grow  height 5 px or 1 ppt"),
    ("Shift+m","resize shrink width  5 px or 1 ppt"),
    ("Shift+p","resize  grow  width  5 px or 1 ppt")
]
    
}

SUPER_CONTROL_COMMANDS = {

"open application menu":
    ("a","$exec pcmanfm -n menu://applications/"),

"kill":
    ("w","kill"),

"reload configuration":
    ("r","$no_border restart"),

"start dmenu for commands":
    ("e","$exec dmenu_run"),

"files":[
    ("f","$exec $fm"),
    ("j","$exec $fm Downloads")
],

"resize (scale)":[
    ("minus","resize shrink height 5 px or 1 ppt; resize shrink width  5 px or 1 ppt"),
    ("plus", "resize  grow  height 5 px or 1 ppt; resize  grow  width  5 px or 1 ppt")
]

}

SUPER_COMMANDS_RSB = {

"oklò change focus":[
    ("o",     "focus up"),
    ("k",     "focus left"),
    ("l",     "focus down"),
    ("ograve","focus right")
],
    
"arrows change focus":[
    ("Up",    "focus up"),
    ("Left",  "focus left"),
    ("Down",  "focus down"),
    ("Right", "focus right")
],
    
"wasd change focus":[
    ("w",     "focus up"),
    ("a",     "focus left"),
    ("s",     "focus down"),
    ("d",     "focus right")
]

}

SUPER_COMMANDS_RSB["switch workspace"] = []

for i,t in WORKSPACES+[CUT_WORKSPACE]:
    x,y = t
    SUPER_COMMANDS_RSB["switch workspace"].append(
        (y,"workspace {}".format(x))
    )
    
SUPER_CONTROL_COMMANDS["move focused container to workspace and follow"] = []

for i,t in WORKSPACES:
    x,y = t
    SUPER_CONTROL_COMMANDS["move focused container to workspace and follow"].append(
        (y,"move container to workspace {}; workspace {}".format(x,x))
    )

#end python
<[BINDALL(SUPER_COMMANDS,"Mod4")]><[BINDALL(SUPER_COMMANDS_RSB,"Mod4","$refresh_status_bar")]><[BINDALL(SUPER_CONTROL_COMMANDS,"Mod4+control")]>
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 #                                  MODES                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


#begin python

#end python

bindsym XF86PowerOff     $no_border mode $pow $exec $alert $pow; fullscreen disable

bindsym --release Super_L   $border mode $sup $exec $alert $sup & $enable_autoscroll; fullscreen disable; $focus_one

bindsym Mod4+space       $no_border mode $hov $exec $alert $hov & $enable_hover_mode & $touchpad_on

bindsym Mod4+r           $no_border mode $red $exec $alert $red
bindsym Mod4+z           $no_border mode $str $exec $alert $str
bindsym Mod4+c           $no_border mode $cnf $exec $alert $cnf

 # # # # # # # # # # # # # # # # #SUPER-MODE # # # # # # # # # # # # # # # # # # 

mode $sup {

        # # # # # # # MODES # # # # # # #

        bindsym XF86PowerOff       $no_border mode $pow $exec $alert $pow; fullscreen disable

        bindsym Escape             $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym Super_L            $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym "Alt_L"            $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym space              $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym Delete             $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym BackSpace          $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym Return             $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym Tab                $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym $alt_gr            $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode
        bindsym --border button2   $no_border mode $hov $exec $alert $hov & $touchpad_on & $enable_hover_mode

        bindsym r                  $no_border mode $red $exec $alert $red
        bindsym z                  $no_border mode $str $exec $alert $str
        bindsym c                  $no_border mode $cnf $exec $alert $cnf

        # # # # # # COMMANDS # # # # # # 

        # touchpad toggle
        bindsym XF86TouchpadToggle $exec $touchpad_toggle

        # Screen brightness controls
        bindsym XF86MonBrightnessUp exec "xbacklight -inc 5; notify-send 'brightness up'" 
        bindsym XF86MonBrightnessDown exec "xbacklight -dec 5; notify-send 'brightness down'"

        # screenshot
        bindsym --release Print $exec $stamp

        # switch workspace
        bindsym 1 workspace $w1; $refresh_status_bar
        bindsym 2 workspace $w2; $refresh_status_bar
        bindsym 3 workspace $w3; $refresh_status_bar
        bindsym 4 workspace $w4; $refresh_status_bar
        bindsym 5 workspace $w5; $refresh_status_bar
        bindsym 6 workspace $w6; $refresh_status_bar
        bindsym 7 workspace $w7; $refresh_status_bar
        bindsym 8 workspace $w8; $refresh_status_bar
        bindsym 9 workspace $w9; $refresh_status_bar
        bindsym x workspace $wx; $refresh_status_bar

        # move focused container to workspace and follow
        bindsym control+1 move container to workspace $w1; workspace $w1
        bindsym control+2 move container to workspace $w2; workspace $w2
        bindsym control+3 move container to workspace $w3; workspace $w3
        bindsym control+4 move container to workspace $w4; workspace $w4
        bindsym control+5 move container to workspace $w5; workspace $w5
        bindsym control+6 move container to workspace $w6; workspace $w6
        bindsym control+7 move container to workspace $w7; workspace $w7
        bindsym control+8 move container to workspace $w8; workspace $w8
        bindsym control+9 move container to workspace $w9; workspace $w9

        bindsym control+Tab       workspace next; $refresh_status_bar
        bindsym control+Shift+Tab workspace prev; $refresh_status_bar

        # cut
        bindsym control+x move container to workspace $wx; $refresh_status_bar

        # paste
        bindsym control+v $exec "i3-msg 'workspace --no-auto-back-and-forth $wx; move container to workspace $wx; workspace $wx'"

        # change focus
        bindsym o      focus up   ; $refresh_status_bar
        bindsym k      focus left ; $refresh_status_bar
        bindsym l      focus down ; $refresh_status_bar
        bindsym ograve focus right; $refresh_status_bar

        # alternatively, you can use the cursor keys:
        bindsym Up     focus up   ; $refresh_status_bar
        bindsym Left   focus left ; $refresh_status_bar
        bindsym Down   focus down ; $refresh_status_bar
        bindsym Right  focus right; $refresh_status_bar

        # alternative to the other alternative
        bindsym w      focus up   ; $refresh_status_bar
        bindsym a      focus left ; $refresh_status_bar
        bindsym s      focus down ; $refresh_status_bar
        bindsym d      focus right; $refresh_status_bar

        # move focused window
        bindsym Shift+o      move up
        bindsym Shift+k      move left
        bindsym Shift+l      move down
        bindsym Shift+ograve move right

        # alternatively, you can use the cursor keys:
        bindsym Shift+Up     move up
        bindsym Shift+Left   move left
        bindsym Shift+Down   move down
        bindsym Shift+Right  move right

        # alternative to the other alternative
        bindsym Shift+w      move up
        bindsym Shift+a      move left
        bindsym Shift+s      move down
        bindsym Shift+d      move right

        # fullscreen
        bindsym f fullscreen enable; mode $def $no_border $exec $alert $bas & $touchpad_off
        bindsym Shift+f $exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"

        # resize window (you can also use the mouse for that)
        bindsym m             resize shrink height 5 px or 1 ppt
        bindsym p             resize  grow  height 5 px or 1 ppt
        bindsym Shift+m       resize shrink width  5 px or 1 ppt
        bindsym Shift+p       resize  grow  width  5 px or 1 ppt
        bindsym control+minus resize shrink height 5 px or 1 ppt; resize shrink width  5 px or 1 ppt
        bindsym control+plus  resize  grow  height 5 px or 1 ppt; resize  grow  width  5 px or 1 ppt

        # split
        bindsym h split h
        bindsym v split v
        bindsym g split v; focus parent; layout toggle split; focus child

        # focus tree
        bindsym less          focus child
        bindsym Shift+greater focus parent
        bindsym control+a    $focus_all

        # kill
        bindsym control+w kill; $refresh_status_bar

        # save layout
        bindsym control+s exec "i3-save-tree > ~/.workspaces/stamp.json; emacs ~/.workspaces/stamp.json"

        # reload i3
        bindsym control+r $no_border reload

        # files
        bindsym control+f $exec $fm
        bindsym control+j $exec $fm Downloads

        # start dmenu for commands
        bindsym control+e    $no_border mode $def $exec $alert $bas & $touchpad_off; $exec dmenu_run

        # start dmenu for applications
        bindsym Menu         $no_border mode $def $exec $alert $bas & $touchpad_off; $exec $dmenu
        bindsym Shift+exclam $no_border mode $def $exec $alert $bas & $touchpad_off; $exec $dmenu

        # # # # # # UNUSED KEYS # # # # # # 

 #       bindsym Delete                        nop
        bindsym backslash                     nop
 #       bindsym 1                             nop
 #       bindsym 2                             nop
 #       bindsym 3                             nop
 #       bindsym 4                             nop
 #       bindsym 5                             nop
 #       bindsym 6                             nop
 #       bindsym 7                             nop
 #       bindsym 8                             nop
 #       bindsym 9                             nop
 #       bindsym 0                             nop
        bindsym aphostrophe                   nop
        bindsym igrave                        nop
 #       bindsym BackSpace                     nop
 #       bindsym Tab                           nop
        bindsym q                             nop
 #       bindsym w                             nop
        bindsym e                             nop
        bindsym r                             nop
        bindsym t                             nop
        bindsym y                             nop
        bindsym u                             nop
        bindsym i                             nop
 #       bindsym o                             nop
        bindsym p                             nop
        bindsym egrave                        nop
        bindsym plus                          nop
 #       bindsym Return                        nop
        bindsym Caps                          nop
 #       bindsym a                             nop
 #       bindsym s                             nop
 #       bindsym d                             nop
        bindsym f                             nop
 #       bindsym g                             nop
 #       bindsym h                             nop
        bindsym j                             nop
 #       bindsym k                             nop
 #       bindsym l                             nop
 #       bindsym ograve                        nop
        bindsym agrave                        nop
        bindsym ugrave                        nop
 #       bindsym "Shift_L"                     nop
 #       bindsym less                          nop
        bindsym z                             nop
 #       bindsym x                             nop
        bindsym c                             nop
 #       bindsym v                             nop
        bindsym b                             nop
        bindsym n                             nop
 #       bindsym m                             nop
        bindsym comma                         nop
        bindsym period                        nop
        bindsym minus                         nop
 #       bindsym "Shift_R"                     nop
 #       bindsym "Control_L"                   nop
 #       bindsym "Super_L"                     nop
 #       bindsym "Alt_L"                       nop
 #       bindsym space                         nop
 #       bindsym $alt_gr                       nop
 #       bindsym Menu                          nop
 #       bindsym "Control_R"                   nop
 #       bindsym Up                            nop
 #       bindsym Left                          nop
 #       bindsym Down                          nop
 #       bindsym Right                         nop

        # also Shift+ (since Shift is not locked)
        bindsym Shift+bar                     nop
 #       bindsym Shift+exclam                  nop
        bindsym Shift+quotedbl                nop
        bindsym Shift+sterling                nop
        bindsym Shift+dollar                  nop
        bindsym Shift+percent                 nop
        bindsym Shift+ampersand               nop
        bindsym Shift+slash                   nop
        bindsym Shift+parenleft               nop
        bindsym Shift+parenright              nop
        bindsym Shift+equal                   nop
        bindsym Shift+question                nop
        bindsym Shift+asciicircum             nop
        bindsym Shift+q                       nop
 #       bindsym Shift+w                       nop
        bindsym Shift+e                       nop
        bindsym Shift+r                       nop
        bindsym Shift+t                       nop
        bindsym Shift+y                       nop
        bindsym Shift+u                       nop
        bindsym Shift+i                       nop
        bindsym Shift+o                       nop
        bindsym Shift+p                       nop
        bindsym Shift+eacute                  nop
        bindsym Shift+asterisk                nop
 #       bindsym Shift+a                       nop
 #       bindsym Shift+s                       nop
 #       bindsym Shift+d                       nop
 #       bindsym Shift+f                       nop
        bindsym Shift+g                       nop
        bindsym Shift+h                       nop
        bindsym Shift+j                       nop
        bindsym Shift+k                       nop
        bindsym Shift+l                       nop
        bindsym Shift+ccedilla                nop
        bindsym Shift+degree                  nop
        bindsym Shift+section                 nop
 #       bindsym Shift+greater                 nop
 #       bindsym Shift+z                       nop
        bindsym Shift+x                       nop
        bindsym Shift+c                       nop
        bindsym Shift+v                       nop
        bindsym Shift+b                       nop
        bindsym Shift+n                       nop
        bindsym Shift+m                       nop
        bindsym Shift+semicolon               nop
        bindsym Shift+colon                   nop
        bindsym Shift+underscore              nop

        # also control+ (since control is not locked)
        bindsym control+Delete                nop
        bindsym control+backslash             nop
 #       bindsym control+1                     nop
 #       bindsym control+2                     nop
 #       bindsym control+3                     nop
 #       bindsym control+4                     nop
 #       bindsym control+5                     nop
 #       bindsym control+6                     nop
 #       bindsym control+7                     nop
 #       bindsym control+8                     nop
 #       bindsym control+9                     nop
 #       bindsym control+0                     nop
        bindsym control+aphostrophe           nop
        bindsym control+igrave                nop
        bindsym control+BackSpace             nop
 #       bindsym control+Tab                   nop
        bindsym control+q                     nop
 #       bindsym control+w                     nop
        bindsym control+e                     nop
 #       bindsym control+r                     nop
 #       bindsym control+t                     nop
        bindsym control+y                     nop
        bindsym control+u                     nop
        bindsym control+i                     nop
        bindsym control+o                     nop
        bindsym control+p                     nop
        bindsym control+egrave                nop
 #       bindsym control+plus                  nop
        bindsym control+Return                nop
 #       bindsym control+a                     nop
 #       bindsym control+s                     nop
        bindsym control+d                     nop
 #       bindsym control+f                     nop
        bindsym control+g                     nop
        bindsym control+h                     nop
        bindsym control+j                     nop
 #       bindsym control+k                     nop
 #       bindsym control+l                     nop
 #       bindsym control+ograve                nop
        bindsym control+agrave                nop
        bindsym control+ugrave                nop
 #       bindsym control+"Shift_L"             nop
 #       bindsym control+less                  nop
        bindsym control+z                     nop
 #       bindsym control+x                     nop
        bindsym control+c                     nop
 #       bindsym control+v                     nop
        bindsym control+b                     nop
        bindsym control+n                     nop
 #       bindsym control+m                     nop
        bindsym control+comma                 nop
        bindsym control+period                nop
 #       bindsym control+minus                 nop
 #       bindsym control+"Shift_R"             nop
 #       bindsym control+"Control_L"           nop
 #       bindsym control+"Super_L"             nop
 #       bindsym control+"Alt_L"               nop
 #       bindsym control+space                 nop
        bindsym control+$alt_gr               nop
 #       bindsym control+Menu                  nop
 #       bindsym control+"Control_R"           nop
 #       bindsym control+Up                    nop
 #       bindsym control+Left                  nop
 #       bindsym control+Down                  nop
 #       bindsym control+Right                 nop
}

 # # # # # # # # # # # # # # # # HOVER-MODE # # # # # # # # # # # # # # # # # # # 

mode $hov {

        # # # # # # # # MODES # # # # # # #

        bindsym Mod4+r             $no_border mode $red $exec $alert $red & $disable_hover_mode & $touchpad_off
        bindsym Mod4+z             $no_border mode $str $exec $alert $str & $disable_hover_mode & $touchpad_off
        bindsym Mod4+c             $no_border mode $cnf $exec $alert $cnf & $disable_hover_mode & $touchpad_off

        bindsym XF86PowerOff       $no_border mode $pow $exec $alert $pow & $disable_hover_mode & $touchpad_off; fullscreen disable

        bindsym --release Super_L     $border mode $sup $exec $alert $sup & $disable_hover_mode & $touchpad_off; fullscreen disable

        bindsym Escape             $no_border mode $def $exec $alert $bas & $disable_hover_mode & $touchpad_off
        bindsym Delete             $no_border mode $def $exec $alert $bas & $disable_hover_mode & $touchpad_off
 #       bindsym space              $no_border mode $def $exec $alert $bas & $disable_hover_mode & $touchpad_off
        bindsym BackSpace          $no_border mode $def $exec $alert $bas & $disable_hover_mode & $touchpad_off
        bindsym control+BackSpace  $no_border mode $def $exec $alert $bas & $disable_hover_mode & $touchpad_off
 #       bindsym $alt_gr            $no_border mode $def $exec $alert $bas & $disable_hover_mode & $touchpad_off

        # # # # # # # COMMANDS # # # # # # 

        # touchpad toggle
bindsym XF86TouchpadToggle $exec $touchpad_toggle

 # Screen brightness controls
bindsym XF86MonBrightnessUp exec "xbacklight -inc 5; notify-send 'brightness up'" 
bindsym XF86MonBrightnessDown exec "xbacklight -dec 5; notify-send 'brightness down'"

 # screenshot
bindsym --release Print $exec $stamp

 # display #TODO
bindsym XF86Display xrandr --output eDP1 --mode 1920x1080 --preferred

 # # # # # # # # # # # # # # # MOD1-COMMANDS # # # # # # # # # # # # # # # # # #

 # a must
bindsym Mod1+F4 kill; $refresh_status_bar

 # also Alt+Tab
bindsym Mod1+Tab       workspace next; $refresh_status_bar
bindsym Mod1+Shift+Tab workspace prev; $refresh_status_bar

 # # # # # # # # # # # # # # # MOD4-COMMANDS # # # # # # # # # # # # # # # # # #

 # start a terminal
bindsym Mod4+Return $exec gnome-terminal

 # open emacs
bindsym Mod4+e $exec emacs

 # application menu
bindsym Mod4+control+a $exec pcmanfm -n menu://applications/

 # kill
bindsym Mod4+control+w kill

 # reload configuration
bindsym Mod4+control+r $no_border restart

 # start dmenu for commands
bindsym Mod4+control+e $exec dmenu_run

 # start dmenu for applications
bindsym Mod4+Menu         $exec $dmenu
bindsym Mod4+Shift+exclam $exec $dmenu

 # files
bindsym Mod4+control+f $exec $fm
bindsym Mod4+control+j $exec $fm Downloads

 # switch workspace
bindsym Mod4+1 workspace $w1; $refresh_status_bar
bindsym Mod4+2 workspace $w2; $refresh_status_bar
bindsym Mod4+3 workspace $w3; $refresh_status_bar
bindsym Mod4+4 workspace $w4; $refresh_status_bar
bindsym Mod4+5 workspace $w5; $refresh_status_bar
bindsym Mod4+6 workspace $w6; $refresh_status_bar
bindsym Mod4+7 workspace $w7; $refresh_status_bar
bindsym Mod4+8 workspace $w8; $refresh_status_bar
bindsym Mod4+9 workspace $w9; $refresh_status_bar
bindsym Mod4+x workspace $wx; $refresh_status_bar

 # move focused container to workspace and follow
bindsym Mod4+control+1 move container to workspace $w1; workspace $w1
bindsym Mod4+control+2 move container to workspace $w2; workspace $w2
bindsym Mod4+control+3 move container to workspace $w3; workspace $w3
bindsym Mod4+control+4 move container to workspace $w4; workspace $w4
bindsym Mod4+control+5 move container to workspace $w5; workspace $w5
bindsym Mod4+control+6 move container to workspace $w6; workspace $w6
bindsym Mod4+control+7 move container to workspace $w7; workspace $w7
bindsym Mod4+control+8 move container to workspace $w8; workspace $w8
bindsym Mod4+control+9 move container to workspace $w9; workspace $w9

 # change focus
bindsym Mod4+o      focus up   ; $refresh_status_bar
bindsym Mod4+k      focus left ; $refresh_status_bar
bindsym Mod4+l      focus down ; $refresh_status_bar
bindsym Mod4+ograve focus right; $refresh_status_bar

 # alternatively, you can use the cursor keys:
bindsym Mod4+Up     focus up   ; $refresh_status_bar
bindsym Mod4+Left   focus left ; $refresh_status_bar
bindsym Mod4+Down   focus down ; $refresh_status_bar
bindsym Mod4+Right  focus right; $refresh_status_bar

 # alternative to the other alternative
bindsym Mod4+w      focus up   ; $refresh_status_bar
bindsym Mod4+a      focus left ; $refresh_status_bar
bindsym Mod4+s      focus down ; $refresh_status_bar
bindsym Mod4+d      focus right; $refresh_status_bar

 # move focused window
bindsym Mod4+Shift+o      move up
bindsym Mod4+Shift+k      move left
bindsym Mod4+Shift+l      move down
bindsym Mod4+Shift+ograve move right

 # alternatively, you can use the cursor keys:
bindsym Mod4+Shift+Up     move up
bindsym Mod4+Shift+Left   move left
bindsym Mod4+Shift+Down   move down
bindsym Mod4+Shift+Right  move right

 # alternative to the other alternative
bindsym Mod4+Shift+w      move up
bindsym Mod4+Shift+a      move left
bindsym Mod4+Shift+s      move down
bindsym Mod4+Shift+d      move right

 # fullscreen
bindsym Mod4+f fullscreen toggle
bindsym Mod4+Shift+f $exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"

 # split toggle
bindsym Mod4+g split v; focus parent; layout toggle split; focus child

 # resize window (you can also use the mouse for that)
bindsym Mod4+m             resize shrink height 5 px or 1 ppt
bindsym Mod4+p             resize  grow  height 5 px or 1 ppt
bindsym Mod4+Shift+m       resize shrink width  5 px or 1 ppt
bindsym Mod4+Shift+p       resize  grow  width  5 px or 1 ppt
bindsym Mod4+control+minus resize shrink height 5 px or 1 ppt; resize shrink width  5 px or 1 ppt
bindsym Mod4+control+plus  resize  grow  height 5 px or 1 ppt; resize  grow  width  5 px or 1 ppt



        # # # # # # UNUSED KEYS # # # # # # 

 #       bindsym Delete                        nop
        bindsym backslash                     nop
        bindsym 1                             nop
        bindsym 2                             nop
        bindsym 3                             nop
        bindsym 4                             nop
        bindsym 5                             nop
        bindsym 6                             nop
        bindsym 7                             nop
        bindsym 8                             nop
        bindsym 9                             nop
        bindsym 0                             nop
        bindsym aphostrophe                   nop
        bindsym igrave                        nop
 #       bindsym BackSpace                     nop
 #       bindsym Tab                           nop
        bindsym q                             nop
        bindsym w                             nop
        bindsym e                             nop
        bindsym r                             nop
        bindsym t                             nop
        bindsym y                             nop
        bindsym u                             nop
        bindsym i                             nop
        bindsym o                             nop
        bindsym p                             nop
        bindsym egrave                        nop
        bindsym plus                          nop
 #       bindsym Return                        nop
        bindsym Caps                          nop
        bindsym a                             nop
        bindsym s                             nop
        bindsym d                             nop
        bindsym f                             nop
        bindsym g                             nop
        bindsym h                             nop
        bindsym j                             nop
        bindsym k                             nop
        bindsym l                             nop
        bindsym ograve                        nop
        bindsym agrave                        nop
        bindsym ugrave                        nop
 #       bindsym "Shift_L"                     nop
        bindsym less                          nop
        bindsym z                             nop
        bindsym x                             nop
        bindsym c                             nop
        bindsym v                             nop
        bindsym b                             nop
        bindsym n                             nop
        bindsym m                             nop
        bindsym comma                         nop
        bindsym period                        nop
        bindsym minus                         nop
 #       bindsym "Shift_R"                     nop
 #       bindsym "Control_L"                   nop
 #       bindsym "Super_L"                     nop
 #       bindsym "Alt_L"                       nop
        bindsym space                         nop
        bindsym $alt_gr                       nop
 #       bindsym Menu                          nop
 #       bindsym "Control_R"                   nop
 #       bindsym Up                            nop
 #       bindsym Left                          nop
 #       bindsym Down                          nop
 #       bindsym Right                         nop

        # also Shift+ (since Shift is not locked)
        bindsym Shift+bar                     nop
        bindsym Shift+exclam                  nop
        bindsym Shift+quotedbl                nop
        bindsym Shift+sterling                nop
        bindsym Shift+dollar                  nop
        bindsym Shift+percent                 nop
        bindsym Shift+ampersand               nop
        bindsym Shift+slash                   nop
        bindsym Shift+parenleft               nop
        bindsym Shift+parenright              nop
        bindsym Shift+equal                   nop
        bindsym Shift+question                nop
        bindsym Shift+asciicircum             nop
        bindsym Shift+q                       nop
        bindsym Shift+w                       nop
        bindsym Shift+e                       nop
        bindsym Shift+r                       nop
        bindsym Shift+t                       nop
        bindsym Shift+y                       nop
        bindsym Shift+u                       nop
        bindsym Shift+i                       nop
        bindsym Shift+o                       nop
        bindsym Shift+p                       nop
        bindsym Shift+eacute                  nop
        bindsym Shift+asterisk                nop
        bindsym Shift+a                       nop
        bindsym Shift+s                       nop
        bindsym Shift+d                       nop
        bindsym Shift+f                       nop
        bindsym Shift+g                       nop
        bindsym Shift+h                       nop
        bindsym Shift+j                       nop
        bindsym Shift+k                       nop
        bindsym Shift+l                       nop
        bindsym Shift+ccedilla                nop
        bindsym Shift+degree                  nop
        bindsym Shift+section                 nop
        bindsym Shift+greater                 nop
        bindsym Shift+z                       nop
        bindsym Shift+x                       nop
        bindsym Shift+c                       nop
        bindsym Shift+v                       nop
        bindsym Shift+b                       nop
        bindsym Shift+n                       nop
        bindsym Shift+m                       nop
        bindsym Shift+semicolon               nop
        bindsym Shift+colon                   nop
        bindsym Shift+underscore              nop
}

 # # # # # # # # # # # # # # # POWEROFF-MODE # # # # # # # # # # # # # # # # # # 

mode $pow {

 #       bindsym XF86PowerOff $exec poweroff
        bindsym XF86PowerOff $exec $alert $pow
        bindsym q            $exec poweroff
        bindsym r            $exec reboot
        bindsym s mode $def  $exec systemctl suspend
        bindsym e            $exec exit

        bindsym Super_L               $border mode $sup $exec $alert $sup

        bindsym Escape                        mode $def $exec $alert $alt
        bindsym "Alt_L"                       mode $def $exec $alert $alt
        bindsym Delete                        mode $def $exec $alert $alt
        bindsym space                         mode $def $exec $alert $alt
        bindsym Return                        mode $def $exec $alert $alt
        bindsym BackSpace                     mode $def $exec $alert $alt
        bindsym Tab                           mode $def $exec $alert $alt
        bindsym $alt_gr                       mode $def $exec $alert $alt

        bindsym Delete                        nop
        bindsym backslash                     nop
        bindsym 1                             nop
        bindsym 2                             nop
        bindsym 3                             nop
        bindsym 4                             nop
        bindsym 5                             nop
        bindsym 6                             nop
        bindsym 7                             nop
        bindsym 8                             nop
        bindsym 9                             nop
        bindsym 0                             nop
        bindsym aphostrophe                   nop
        bindsym igrave                        nop
        bindsym BackSpace                     nop
 #       bindsym Tab                           nop
 #       bindsym q                             nop
        bindsym w                             nop
 #       bindsym e                             nop
 #       bindsym r                             nop
        bindsym t                             nop
        bindsym y                             nop
        bindsym u                             nop
        bindsym i                             nop
        bindsym o                             nop
        bindsym p                             nop
        bindsym egrave                        nop
        bindsym plus                          nop
        bindsym Return                        nop
        bindsym Caps                          nop
        bindsym a                             nop
 #       bindsym s                             nop
        bindsym d                             nop
        bindsym f                             nop
        bindsym g                             nop
        bindsym h                             nop
        bindsym j                             nop
        bindsym k                             nop
        bindsym l                             nop
        bindsym ograve                        nop
        bindsym agrave                        nop
        bindsym ugrave                        nop
        bindsym "Shift_L"                     nop
        bindsym less                          nop
        bindsym z                             nop
        bindsym x                             nop
        bindsym c                             nop
        bindsym v                             nop
        bindsym b                             nop
        bindsym n                             nop
        bindsym m                             nop
        bindsym comma                         nop
        bindsym period                        nop
        bindsym minus                         nop
        bindsym "Shift_R"                     nop
        bindsym "Control_L"                   nop
 #       bindsym "Super_L"                     nop
 #       bindsym "Alt_L"                       nop
 #       bindsym space                         nop
 #       bindsym $alt_gr                       nop
        bindsym Menu                          nop
        bindsym "Control_R"                   nop
        bindsym Up                            nop
        bindsym Left                          nop
        bindsym Down                          nop
        bindsym Right                         nop
}

 # # # # # # # # # # # # # # # # SUB-MODES # # # # # # # # # # # # # # # # # # # #

mode $red {

        bindsym 1 $exec redshift -P -O 2100K
        bindsym 2 $exec redshift -P -O 2300K
        bindsym 3 $exec redshift -P -O 2500K
        bindsym 4 $exec redshift -P -O 2700K
        bindsym 5 $exec redshift -P -O 3000K
        bindsym 6 $exec redshift -P -O 3500K
        bindsym 7 $exec redshift -P -O 4000K
        bindsym 8 $exec redshift -P -O 4500K
        bindsym 9 $exec redshift -P -O 5000K
        bindsym 0 $exec redshift -P -O 6500K
        bindsym plus $exec redshift -O 6400K

        bindsym XF86PowerOff       $no_border mode $pow $exec $alert $pow; fullscreen disable

        bindsym --release Super_L                       mode $sup $exec $alert $sup

        # touchpad toggle
bindsym XF86TouchpadToggle $exec $touchpad_toggle

 # Screen brightness controls
bindsym XF86MonBrightnessUp exec "xbacklight -inc 5; notify-send 'brightness up'" 
bindsym XF86MonBrightnessDown exec "xbacklight -dec 5; notify-send 'brightness down'"

 # display #TODO
bindsym XF86Display xrandr --output eDP1 --mode 1920x1080 --preferred

 # # # # # # # # # # # # # # # MOD1-COMMANDS # # # # # # # # # # # # # # # # # #

 # a must
bindsym Mod1+F4 kill; $refresh_status_bar

 # also Alt+Tab
bindsym Mod1+Tab       workspace next; $refresh_status_bar
bindsym Mod1+Shift+Tab workspace prev; $refresh_status_bar

 # # # # # # # # # # # # # # # MOD4-COMMANDS # # # # # # # # # # # # # # # # # #

 # start a terminal
bindsym Mod4+Return $exec gnome-terminal

 # open emacs
bindsym Mod4+e $exec emacs

 # application menu
bindsym Mod4+control+a $exec pcmanfm -n menu://applications/

 # kill
bindsym Mod4+control+w kill

 # reload configuration
bindsym Mod4+control+r $no_border restart

 # start dmenu for commands
bindsym Mod4+control+e $exec dmenu_run &

 # start dmenu for applications
bindsym Mod4+Menu         $exec $dmenu
bindsym Mod4+Shift+exclam $exec $dmenu

 # files
bindsym Mod4+control+f $exec $fm
bindsym Mod4+control+j $exec $fm Downloads

 # switch workspace
bindsym Mod4+1 workspace $w1; $refresh_status_bar
bindsym Mod4+2 workspace $w2; $refresh_status_bar
bindsym Mod4+3 workspace $w3; $refresh_status_bar
bindsym Mod4+4 workspace $w4; $refresh_status_bar
bindsym Mod4+5 workspace $w5; $refresh_status_bar
bindsym Mod4+6 workspace $w6; $refresh_status_bar
bindsym Mod4+7 workspace $w7; $refresh_status_bar
bindsym Mod4+8 workspace $w8; $refresh_status_bar
bindsym Mod4+9 workspace $w9; $refresh_status_bar
bindsym Mod4+x workspace $wx; $refresh_status_bar

 # move focused container to workspace and follow
bindsym Mod4+control+1 move container to workspace $w1; workspace $w1
bindsym Mod4+control+2 move container to workspace $w2; workspace $w2
bindsym Mod4+control+3 move container to workspace $w3; workspace $w3
bindsym Mod4+control+4 move container to workspace $w4; workspace $w4
bindsym Mod4+control+5 move container to workspace $w5; workspace $w5
bindsym Mod4+control+6 move container to workspace $w6; workspace $w6
bindsym Mod4+control+7 move container to workspace $w7; workspace $w7
bindsym Mod4+control+8 move container to workspace $w8; workspace $w8
bindsym Mod4+control+9 move container to workspace $w9; workspace $w9

 # change focus
bindsym Mod4+o      focus up   ; $refresh_status_bar
bindsym Mod4+k      focus left ; $refresh_status_bar
bindsym Mod4+l      focus down ; $refresh_status_bar
bindsym Mod4+ograve focus right; $refresh_status_bar

 # alternatively, you can use the cursor keys:
bindsym Mod4+Up     focus up   ; $refresh_status_bar
bindsym Mod4+Left   focus left ; $refresh_status_bar
bindsym Mod4+Down   focus down ; $refresh_status_bar
bindsym Mod4+Right  focus right; $refresh_status_bar

 # alternative to the other alternative
bindsym Mod4+w      focus up   ; $refresh_status_bar
bindsym Mod4+a      focus left ; $refresh_status_bar
bindsym Mod4+s      focus down ; $refresh_status_bar
bindsym Mod4+d      focus right; $refresh_status_bar

 # move focused window
bindsym Mod4+Shift+o      move up
bindsym Mod4+Shift+k      move left
bindsym Mod4+Shift+l      move down
bindsym Mod4+Shift+ograve move right

 # alternatively, you can use the cursor keys:
bindsym Mod4+Shift+Up     move up
bindsym Mod4+Shift+Left   move left
bindsym Mod4+Shift+Down   move down
bindsym Mod4+Shift+Right  move right

 # alternative to the other alternative
bindsym Mod4+Shift+w      move up
bindsym Mod4+Shift+a      move left
bindsym Mod4+Shift+s      move down
bindsym Mod4+Shift+d      move right

 # fullscreen
bindsym Mod4+f fullscreen toggle
bindsym Mod4+Shift+f $exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"

 # split toggle
bindsym Mod4+g split v; focus parent; layout toggle split; focus child

 # resize window (you can also use the mouse for that)
bindsym Mod4+m             resize shrink height 5 px or 1 ppt
bindsym Mod4+p             resize  grow  height 5 px or 1 ppt
bindsym Mod4+Shift+m       resize shrink width  5 px or 1 ppt
bindsym Mod4+Shift+p       resize  grow  width  5 px or 1 ppt
bindsym Mod4+control+minus resize shrink height 5 px or 1 ppt; resize shrink width  5 px or 1 ppt
bindsym Mod4+control+plus  resize  grow  height 5 px or 1 ppt; resize  grow  width  5 px or 1 ppt



        bindsym Escape             $no_border mode $def $exec $alert $alt
        bindsym "Alt_L"            $no_border mode $def $exec $alert $alt
        bindsym Delete             $no_border mode $def $exec $alert $alt
        bindsym space              $no_border mode $def $exec $alert $alt
        bindsym Return             $no_border mode $def $exec $alert $alt
        bindsym BackSpace          $no_border mode $def $exec $alert $alt
        bindsym Tab                $no_border mode $def $exec $alert $alt
        bindsym $alt_gr            $no_border mode $def $exec $alert $alt

 #       bindsym Delete                        nop
        bindsym backslash                     nop
 #       bindsym 1                             nop
 #       bindsym 2                             nop
 #       bindsym 3                             nop
 #       bindsym 4                             nop
 #       bindsym 5                             nop
 #       bindsym 6                             nop
 #       bindsym 7                             nop
 #       bindsym 8                             nop
 #       bindsym 9                             nop
 #       bindsym 0                             nop
        bindsym aphostrophe                   nop
        bindsym igrave                        nop
 #       bindsym BackSpace                     nop
 #       bindsym Tab                           nop
        bindsym q                             nop
        bindsym w                             nop
        bindsym e                             nop
        bindsym r                             nop
        bindsym t                             nop
        bindsym y                             nop
        bindsym u                             nop
        bindsym i                             nop
        bindsym o                             nop
        bindsym p                             nop
        bindsym egrave                        nop
 #       bindsym plus                          nop
 #       bindsym Return                        nop
        bindsym Caps                          nop
        bindsym a                             nop
        bindsym s                             nop
        bindsym d                             nop
        bindsym f                             nop
        bindsym g                             nop
        bindsym h                             nop
        bindsym j                             nop
        bindsym k                             nop
        bindsym l                             nop
        bindsym ograve                        nop
        bindsym agrave                        nop
        bindsym ugrave                        nop
        bindsym "Shift_L"                     nop
        bindsym less                          nop
        bindsym z                             nop
        bindsym x                             nop
        bindsym c                             nop
        bindsym v                             nop
        bindsym b                             nop
        bindsym n                             nop
        bindsym m                             nop
        bindsym comma                         nop
        bindsym period                        nop
        bindsym minus                         nop
        bindsym "Shift_R"                     nop
        bindsym "Control_L"                   nop
 #       bindsym "Super_L"                     nop
 #       bindsym "Alt_L"                       nop
 #       bindsym space                         nop
 #       bindsym $alt_gr                       nop
        bindsym Menu                          nop
        bindsym "Control_R"                   nop
        bindsym Up                            nop
        bindsym Left                          nop
        bindsym Down                          nop
        bindsym Right                         nop
}

 # start layout
mode $str {

        bindsym 1 mode $def $no_border $exec $alert $bas & $touchpad_off; $exec "$layout_1; $fill_1"
        bindsym 2 mode $def $no_border $exec $alert $bas & $touchpad_off; $exec "$layout_2; $fill_2"

        bindsyl XF86PowerOff       $no_border mode $pow $exec $alert $pow; fullscreen disable

        bindsym --release Super_L                       mode $sup $exec $alert $sup

        # touchpad toggle
bindsym XF86TouchpadToggle $exec $touchpad_toggle

 # Screen brightness controls
bindsym XF86MonBrightnessUp exec "xbacklight -inc 5; notify-send 'brightness up'" 
bindsym XF86MonBrightnessDown exec "xbacklight -dec 5; notify-send 'brightness down'"

 # screenshot
bindsym --release Print $exec $stamp

 # display #TODO
bindsym XF86Display xrandr --output eDP1 --mode 1920x1080 --preferred

 # # # # # # # # # # # # # # # MOD1-COMMANDS # # # # # # # # # # # # # # # # # #

 # a must
bindsym Mod1+F4 kill; $refresh_status_bar

 # also Alt+Tab
bindsym Mod1+Tab       workspace next; $refresh_status_bar
bindsym Mod1+Shift+Tab workspace prev; $refresh_status_bar

 # # # # # # # # # # # # # # # MOD4-COMMANDS # # # # # # # # # # # # # # # # # #

 # start a terminal
bindsym Mod4+Return $exec gnome-terminal

 # open emacs
bindsym Mod4+e $exec emacs

 # application menu
bindsym Mod4+control+a $exec pcmanfm -n menu://applications/

 # kill
bindsym Mod4+control+w kill

 # reload configuration
bindsym Mod4+control+r $no_border restart

 # start dmenu for commands
bindsym Mod4+control+e $exec dmenu_run

 # start dmenu for applications
bindsym Mod4+Menu         $exec $dmenu
bindsym Mod4+Shift+exclam $exec $dmenu

 # files
bindsym Mod4+control+f $exec $fm
bindsym Mod4+control+j $exec $fm Downloads

 # switch workspace
bindsym Mod4+1 workspace $w1; $refresh_status_bar
bindsym Mod4+2 workspace $w2; $refresh_status_bar
bindsym Mod4+3 workspace $w3; $refresh_status_bar
bindsym Mod4+4 workspace $w4; $refresh_status_bar
bindsym Mod4+5 workspace $w5; $refresh_status_bar
bindsym Mod4+6 workspace $w6; $refresh_status_bar
bindsym Mod4+7 workspace $w7; $refresh_status_bar
bindsym Mod4+8 workspace $w8; $refresh_status_bar
bindsym Mod4+9 workspace $w9; $refresh_status_bar
bindsym Mod4+x workspace $wx; $refresh_status_bar

 # move focused container to workspace and follow
bindsym Mod4+control+1 move container to workspace $w1; workspace $w1
bindsym Mod4+control+2 move container to workspace $w2; workspace $w2
bindsym Mod4+control+3 move container to workspace $w3; workspace $w3
bindsym Mod4+control+4 move container to workspace $w4; workspace $w4
bindsym Mod4+control+5 move container to workspace $w5; workspace $w5
bindsym Mod4+control+6 move container to workspace $w6; workspace $w6
bindsym Mod4+control+7 move container to workspace $w7; workspace $w7
bindsym Mod4+control+8 move container to workspace $w8; workspace $w8
bindsym Mod4+control+9 move container to workspace $w9; workspace $w9

 # change focus
bindsym Mod4+o      focus up   ; $refresh_status_bar
bindsym Mod4+k      focus left ; $refresh_status_bar
bindsym Mod4+l      focus down ; $refresh_status_bar
bindsym Mod4+ograve focus right; $refresh_status_bar

 # alternatively, you can use the cursor keys:
bindsym Mod4+Up     focus up   ; $refresh_status_bar
bindsym Mod4+Left   focus left ; $refresh_status_bar
bindsym Mod4+Down   focus down ; $refresh_status_bar
bindsym Mod4+Right  focus right; $refresh_status_bar

 # alternative to the other alternative
bindsym Mod4+w      focus up   ; $refresh_status_bar
bindsym Mod4+a      focus left ; $refresh_status_bar
bindsym Mod4+s      focus down ; $refresh_status_bar
bindsym Mod4+d      focus right; $refresh_status_bar

 # move focused window
bindsym Mod4+Shift+o      move up
bindsym Mod4+Shift+k      move left
bindsym Mod4+Shift+l      move down
bindsym Mod4+Shift+ograve move right

 # alternatively, you can use the cursor keys:
bindsym Mod4+Shift+Up     move up
bindsym Mod4+Shift+Left   move left
bindsym Mod4+Shift+Down   move down
bindsym Mod4+Shift+Right  move right

 # alternative to the other alternative
bindsym Mod4+Shift+w      move up
bindsym Mod4+Shift+a      move left
bindsym Mod4+Shift+s      move down
bindsym Mod4+Shift+d      move right

 # fullscreen
bindsym Mod4+f fullscreen toggle
bindsym Mod4+Shift+f $exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"

 # split toggle
bindsym Mod4+g split v; focus parent; layout toggle split; focus child

 # resize window (you can also use the mouse for that)
bindsym Mod4+m             resize shrink height 5 px or 1 ppt
bindsym Mod4+p             resize  grow  height 5 px or 1 ppt
bindsym Mod4+Shift+m       resize shrink width  5 px or 1 ppt
bindsym Mod4+Shift+p       resize  grow  width  5 px or 1 ppt
bindsym Mod4+control+minus resize shrink height 5 px or 1 ppt; resize shrink width  5 px or 1 ppt
bindsym Mod4+control+plus  resize  grow  height 5 px or 1 ppt; resize  grow  width  5 px or 1 ppt



        bindsym Escape             $no_border mode $def $exec $alert $alt
        bindsym "Alt_L"            $no_border mode $def $exec $alert $alt
        bindsym Delete             $no_border mode $def $exec $alert $alt
        bindsym space              $no_border mode $def $exec $alert $alt
        bindsym Return             $no_border mode $def $exec $alert $alt
        bindsym BackSpace          $no_border mode $def $exec $alert $alt
        bindsym Tab                $no_border mode $def $exec $alert $alt
        bindsym $alt_gr            $no_border mode $def $exec $alert $alt


 #       bindsym Delete                        nop
        bindsym backslash                     nop
 #       bindsym 1                             nop
 #       bindsym 2                             nop
        bindsym 3                             nop
        bindsym 4                             nop
        bindsym 5                             nop
        bindsym 6                             nop
        bindsym 7                             nop
        bindsym 8                             nop
        bindsym 9                             nop
        bindsym 0                             nop
        bindsym aphostrophe                   nop
        bindsym igrave                        nop
 #       bindsym BackSpace                     nop
 #       bindsym Tab                           nop
        bindsym q                             nop
        bindsym w                             nop
        bindsym e                             nop
        bindsym r                             nop
        bindsym t                             nop
        bindsym y                             nop
        bindsym u                             nop
        bindsym i                             nop
        bindsym o                             nop
        bindsym p                             nop
        bindsym egrave                        nop
        bindsym plus                          nop
 #       bindsym Return                        nop
        bindsym Caps                          nop
        bindsym a                             nop
        bindsym s                             nop
        bindsym d                             nop
        bindsym f                             nop
        bindsym g                             nop
        bindsym h                             nop
        bindsym j                             nop
        bindsym k                             nop
        bindsym l                             nop
        bindsym ograve                        nop
        bindsym agrave                        nop
        bindsym ugrave                        nop
        bindsym "Shift_L"                     nop
        bindsym less                          nop
        bindsym z                             nop
        bindsym x                             nop
        bindsym c                             nop
        bindsym v                             nop
        bindsym b                             nop
        bindsym n                             nop
        bindsym m                             nop
        bindsym comma                         nop
        bindsym period                        nop
        bindsym minus                         nop
        bindsym "Shift_R"                     nop
        bindsym "Control_L"                   nop
 #       bindsym "Super_L"                     nop
 #       bindsym "Alt_L"                       nop
 #       bindsym space                         nop
 #       bindsym $alt_gr                       nop
        bindsym Menu                          nop
        bindsym "Control_R"                   nop
        bindsym Up                            nop
        bindsym Left                          nop
        bindsym Down                          nop
        bindsym Right                         nop
}

 # configuration files launcher
mode $cnf {

        bindsym c mode $def $no_border $exec emacs ~/.i3/config & $alert $bas & $touchpad_off
        bindsym i mode $def $no_border $exec emacs ~/.gitignore
        bindsym a mode $def $no_border $exec emacs /sudo::/usr/share/applications/ & $alert $bas & $touchpad_off
        bindsym e mode $def $no_border $exec emacs ~/.emacs & $alert $bas & $touchpad_off
        bindsym s mode $def $no_border $exec emacs ~/.config/i3status/config & $alert $bas & $touchpad_off
        bindsym z mode $def $no_border $exec emacs ~/.zshrc & $alert $bas & $touchpad_off
        bindsym g mode $def $no_border $exec chromium --new-window i3wm.org/docs/userguide.html & $alert $bas & $touchpad_off
        bindsym l mode $def $no_border $exec emacs ~/.workspaces/stamp.json & $alert $bas & $touchpad_off
        bindsym 1 mode $def $no_border $exec emacs ~/.workspaces/$w1.json & $alert $bas & $touchpad_off
        bindsym 2 mode $def $no_border $exec emacs ~/.workspaces/$w2.json & $alert $bas & $touchpad_off
        bindsym y mode $def $no_border $exec emacs /sudo::/etc/yaourtrc & $alert $bas & $touchpad_off
        bindsym r mode $def $no_border $exec emacs ~/.config/redshift/redshift.conf

        bindsym XF86PowerOff       $no_border mode $pow $exec $alert $pow; fullscreen disable

        bindsym --release Super_L                       mode $sup $exec $alert $sup

        # touchpad toggle
bindsym XF86TouchpadToggle $exec $touchpad_toggle

 # Screen brightness controls
bindsym XF86MonBrightnessUp exec "xbacklight -inc 5; notify-send 'brightness up'" 
bindsym XF86MonBrightnessDown exec "xbacklight -dec 5; notify-send 'brightness down'"

 # screenshot
bindsym --release Print $exec $stamp

 # display #TODO
bindsym XF86Display xrandr --output eDP1 --mode 1920x1080 --preferred

 # # # # # # # # # # # # # # # MOD1-COMMANDS # # # # # # # # # # # # # # # # # #

 # a must
bindsym Mod1+F4 kill; $refresh_status_bar

 # also Alt+Tab
bindsym Mod1+Tab       workspace next; $refresh_status_bar
bindsym Mod1+Shift+Tab workspace prev; $refresh_status_bar

 # # # # # # # # # # # # # # # MOD4-COMMANDS # # # # # # # # # # # # # # # # # #

 # start a terminal
bindsym Mod4+Return $exec gnome-terminal

 # open emacs
bindsym Mod4+e $exec emacs

 # application menu
bindsym Mod4+control+a $exec pcmanfm -n menu://applications/

 # kill
bindsym Mod4+control+w kill

 # reload configuration
bindsym Mod4+control+r $no_border restart

 # start dmenu for commands
bindsym Mod4+control+e $exec dmenu_run

 # start dmenu for applications
bindsym Mod4+Menu         $exec $dmenu
bindsym Mod4+Shift+exclam $exec $dmenu

 # files
bindsym Mod4+control+f $exec $fm
bindsym Mod4+control+j $exec $fm Downloads

 # switch workspace
bindsym Mod4+1 workspace $w1; $refresh_status_bar
bindsym Mod4+2 workspace $w2; $refresh_status_bar
bindsym Mod4+3 workspace $w3; $refresh_status_bar
bindsym Mod4+4 workspace $w4; $refresh_status_bar
bindsym Mod4+5 workspace $w5; $refresh_status_bar
bindsym Mod4+6 workspace $w6; $refresh_status_bar
bindsym Mod4+7 workspace $w7; $refresh_status_bar
bindsym Mod4+8 workspace $w8; $refresh_status_bar
bindsym Mod4+9 workspace $w9; $refresh_status_bar
bindsym Mod4+x workspace $wx; $refresh_status_bar

 # move focused container to workspace and follow
bindsym Mod4+control+1 move container to workspace $w1; workspace $w1
bindsym Mod4+control+2 move container to workspace $w2; workspace $w2
bindsym Mod4+control+3 move container to workspace $w3; workspace $w3
bindsym Mod4+control+4 move container to workspace $w4; workspace $w4
bindsym Mod4+control+5 move container to workspace $w5; workspace $w5
bindsym Mod4+control+6 move container to workspace $w6; workspace $w6
bindsym Mod4+control+7 move container to workspace $w7; workspace $w7
bindsym Mod4+control+8 move container to workspace $w8; workspace $w8
bindsym Mod4+control+9 move container to workspace $w9; workspace $w9

 # change focus
bindsym Mod4+o      focus up   ; $refresh_status_bar
bindsym Mod4+k      focus left ; $refresh_status_bar
bindsym Mod4+l      focus down ; $refresh_status_bar
bindsym Mod4+ograve focus right; $refresh_status_bar

 # alternatively, you can use the cursor keys:
bindsym Mod4+Up     focus up   ; $refresh_status_bar
bindsym Mod4+Left   focus left ; $refresh_status_bar
bindsym Mod4+Down   focus down ; $refresh_status_bar
bindsym Mod4+Right  focus right; $refresh_status_bar

 # alternative to the other alternative
bindsym Mod4+w      focus up   ; $refresh_status_bar
bindsym Mod4+a      focus left ; $refresh_status_bar
bindsym Mod4+s      focus down ; $refresh_status_bar
bindsym Mod4+d      focus right; $refresh_status_bar

 # move focused window
bindsym Mod4+Shift+o      move up
bindsym Mod4+Shift+k      move left
bindsym Mod4+Shift+l      move down
bindsym Mod4+Shift+ograve move right

 # alternatively, you can use the cursor keys:
bindsym Mod4+Shift+Up     move up
bindsym Mod4+Shift+Left   move left
bindsym Mod4+Shift+Down   move down
bindsym Mod4+Shift+Right  move right

 # alternative to the other alternative
bindsym Mod4+Shift+w      move up
bindsym Mod4+Shift+a      move left
bindsym Mod4+Shift+s      move down
bindsym Mod4+Shift+d      move right

 # fullscreen
bindsym Mod4+f fullscreen toggle
bindsym Mod4+Shift+f $exec "sleep 0.5; xdotool key F11; i3-msg fullscreen disable"

 # split toggle
bindsym Mod4+g split v; focus parent; layout toggle split; focus child

 # resize window (you can also use the mouse for that)
bindsym Mod4+m             resize shrink height 5 px or 1 ppt
bindsym Mod4+p             resize  grow  height 5 px or 1 ppt
bindsym Mod4+Shift+m       resize shrink width  5 px or 1 ppt
bindsym Mod4+Shift+p       resize  grow  width  5 px or 1 ppt
bindsym Mod4+control+minus resize shrink height 5 px or 1 ppt; resize shrink width  5 px or 1 ppt
bindsym Mod4+control+plus  resize  grow  height 5 px or 1 ppt; resize  grow  width  5 px or 1 ppt



        bindsym Escape             $no_border mode $def $exec $alert $alt
        bindsym "Alt_L"            $no_border mode $def $exec $alert $alt
        bindsym Delete             $no_border mode $def $exec $alert $alt
        bindsym space              $no_border mode $def $exec $alert $alt
        bindsym Return             $no_border mode $def $exec $alert $alt
        bindsym BackSpace          $no_border mode $def $exec $alert $alt
        bindsym Tab                $no_border mode $def $exec $alert $alt
        bindsym $alt_gr            $no_border mode $def $exec $alert $alt

 #       bindsym Delete                        nop
        bindsym backslash                     nop
 #       bindsym 1                             nop
 #       bindsym 2                             nop
        bindsym 3                             nop
        bindsym 4                             nop
        bindsym 5                             nop
        bindsym 6                             nop
        bindsym 7                             nop
        bindsym 8                             nop
        bindsym 9                             nop
        bindsym 0                             nop
        bindsym aphostrophe                   nop
        bindsym igrave                        nop
 #       bindsym BackSpace                     nop
 #       bindsym Tab                           nop
        bindsym q                             nop
        bindsym w                             nop
 #       bindsym e                             nop
        bindsym r                             nop
        bindsym t                             nop
 #       bindsym y                             nop
        bindsym u                             nop
 #       bindsym i                             nop
        bindsym o                             nop
        bindsym p                             nop
        bindsym egrave                        nop
        bindsym plus                          nop
 #       bindsym Return                        nop
        bindsym Caps                          nop
 #       bindsym a                             nop
 #       bindsym s                             nop
        bindsym d                             nop
        bindsym f                             nop
 #       bindsym g                             nop
        bindsym h                             nop
        bindsym j                             nop
        bindsym k                             nop
 #       bindsym l                             nop
        bindsym ograve                        nop
        bindsym agrave                        nop
        bindsym ugrave                        nop
        bindsym "Shift_L"                     nop
        bindsym less                          nop
 #       bindsym z                             nop
        bindsym x                             nop
 #       bindsym c                             nop
        bindsym v                             nop
        bindsym b                             nop
        bindsym n                             nop
        bindsym m                             nop
        bindsym comma                         nop
        bindsym period                        nop
        bindsym minus                         nop
        bindsym "Shift_R"                     nop
        bindsym "Control_L"                   nop
 #       bindsym "Super_L"                     nop
 #       bindsym "Alt_L"                       nop
 #       bindsym space                         nop
 #       bindsym $alt_gr                       nop
        bindsym Menu                          nop
        bindsym "Control_R"                   nop
        bindsym Up                            nop
        bindsym Left                          nop
        bindsym Down                          nop
        bindsym Right                         nop
}

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 #                              STATUS-BAR                                     #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

 # Start i3bar to display a workspace bar (plus the system information i3status finds out, if available)
bar {
        status_command    ./.bin/my_status.sh
        position          bottom
        mode              dock
        workspace_buttons yes
        colors {
                   background #000000
                   statusline #999999
                   focused_workspace  #ffffff #000000
                   active_workspace   #ffffff #000000
                   inactive_workspace #888888 #000000
                   urgent_workspace   #ffffff #000000
               }

        # disable scrolling on status bar
 #       bindsym button4 nop # scroll wheel up
 #       bindsym button5 nop # scroll wheel down
        # mid-mouse click to lock
 #       bindsym button2 mode $def $no_border $exec $alert $bas & $touchpad_off_2 & $disable_hover_mode
    }

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 #                              APPLICATIONS                                   #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

 # code
assign [class=".*code.*"] $w3

 # android studio
assign [class="jetbrains-studio"] $w3

 # steam
assign [class="Steam"] $w5
assign [class="Wine"] $w5
for_window [title="Steam - News"] kill
for_window [title="Friends"] resize shrink width 22 px or 22 ppt; split h
for_window [title="Steam"] split h

 # discord and skype
assign [class="discord"] $w6
assign [title=".*skype.*"] $w6

 # texmaker
assign [title="Texmaker"] $w7
assign [title=".*overleaf.*"] $w7

 # gimp
assign [class="Gimp.*"] $w9

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 #                                STARTUP                                      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

 # keybinding (order matters)
$exec $disable_Caps

 # autoscroll (not always permanent, may need reaload)
$exec_always $enable_autoscroll

 # background (not always permanent)
$exec_always nitrogen --restore

 # bar applications
$exec nm-applet
$exec pamac-tray
$exec pa-applet
$exec clipit

 # background applications
$exec /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1

 # reshift oneshot mode (to set starting temperature according to time)
$exec redshift -o

 # layout
$exec $layout_2; $fill_2

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 #                                  FIN                                        #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
