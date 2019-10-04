#include "forall.py"
#include "arrows.py"
#include "workspaces.py"
#begin python

TOP_COMMANDS = {

"touchpad toggle":
    ("XF86TouchpadToggle","$exec $touchpad_toggle"),

"screen brightness controls":[
    ("XF86MonBrightnessUp","$brightness_up"),
    ("XF86MonBrightnessDown","$brightness_down")
],

"screen poweroff":
    ("XF86ScreenSaver","$exec $screen_off"),

"screenshot":
    ("Print","$exec i3-scrot"),

"display": #TODO
    ("XF86Display", "$exec xrandr --output eDP1 --mode 1920x1080 --preferred"),

"middle mouse no border":
    ("--border button2","$no_border"),

}

MOD1_COMMANDS_RSB = {

"kill":
    ("Mod1+F4","kill"),

}

MOD4_COMMANDS = {

"touchpad":[
    ("Mod4+space","$exec $touchpad_x_on"),
    ("Mod4+Shift+space","$exec $touchpad_x_off"),
],

"fullscreen":
    ("Mod4+f","fullscreen toggle"),

"split orientation":[
    ("Mod4+v","split v; $exec notify-send 'vertical'"),
    ("Mod4+h","split h; $exec notify-send 'horizontal'"),
    ("Mod4+g","split v; focus parent; layout toggle split; focus child"),
],

"reload configuration":[
    ("Mod4+control+r",'$exec "make -C ~/.i3 && i3-msg $no_border restart"'),
    ("Mod4+control+Shift+r", '$exec "make -C ~/.i3 stable && i3-msg $no_border restart"')
],

}

MOD4_COMMANDS_RSB = {

"kill":
    ("Mod4+control+w","kill"),

"cut":
    ("Mod4+control+x","move container to workspace $wx"),

"paste":
    ("Mod4+control+v",'$exec "i3-msg \'workspace --no-auto-back-and-forth $wx; move container to workspace $wx; workspace $wx\'"'),

"browse workspaces":[
    ("Mod4+Tab","workspace next"),
    ("Mod4+Shift+Tab","workspace prev"),
    ("Mod4+j","workspace prev"),
    ("Mod4+agrave","workspace next"),
    ("Mod4+Home","workspace prev"),
    ("Mod4+End","workspace next"),
    ("Mod4+ugrave","workspace back_and_forth"),
],

"focus group":[
    ("Mod4+less","focus child"),
    ("Mod4+Shift+greater","focus parent")
],

"focus all":
    ("Mod4+control+a","fullscreen disable $focus_all"),

"borders":[
    ("Mod4+x","$border $focus_one fullscreen disable"),
    ("Mod4+Shift+x","$no_border $focus_one")
],

"open emacs":
    ("Mod4+e","$exec $emacs"),

"shutdown emacs server":
    ("Mod4+control+Shift+e","$exec pkill emacs"),

"file manager":[
    ("Mod4+control+f","$exec $fm"),
    ("Mod4+control+j","$exec $fm Downloads")
],

"save layout":
    ("Mod4+control+s",'$exec "i3-save-tree > ~/.workspaces/stamp.json; emacsclient -create-frame --alternate-editor=\'\' ~/.workspaces/stamp.json"'),

}

MOD4_COMMANDS_TO_DEFLT = {

"start dmenu for applications":
    ("Mod4+Shift+exclam","$exec $dmenu"),

"start dmenu for commands":
    ("Mod4+control+e","$exec dmenu_run"),

}

MOD4_COMMANDS_TO_RIGHT = {

"application menu":
    ("Mod4+Menu","$exec morc_menu"),

"open terminal":
    ("Mod4+Return","$exec gnome-terminal"),

"resize window":[
    ("Mod4+i","resize shrink height 5 px or 5 ppt"),
    ("Mod4+p","resize  grow  height 5 px or 5 ppt"),
    ("Mod4+Prior","resize shrink height 5 px or 5 ppt"),
    ("Mod4+Next", "resize  grow  height 5 px or 5 ppt"),
    ("Mod4+Shift+i","resize shrink width  5 px or 5 ppt"),
    ("Mod4+Shift+p","resize  grow  width  5 px or 5 ppt"),
    ("Mod4+Shift+Prior","resize shrink width  5 px or 5 ppt"),
    ("Mod4+Shift+Next", "resize  grow  width  5 px or 5 ppt"),
],

"resize (precise)":[
    ("Mod4+control+i","resize shrink height 1 px or 1 ppt"),
    ("Mod4+control+p","resize  grow  height 1 px or 1 ppt"),
    ("Mod4+control+Prior","resize shrink height 1 px or 1 ppt"),
    ("Mod4+control+Next", "resize  grow  height 1 px or 1 ppt"),
    ("Mod4+control+Shift+i","resize shrink width  1 px or 1 ppt"),
    ("Mod4+control+Shift+p","resize  grow  width  1 px or 1 ppt"),
    ("Mod4+control+Shift+Prior","resize shrink width  1 px or 1 ppt"),
    ("Mod4+control+Shift+Next", "resize  grow  width  1 px or 1 ppt"),
],

"resize (scale)":[
    ("Mod4+control+minus","resize shrink height 5 px or 5 ppt; resize shrink width  5 px or 5 ppt"),
    ("Mod4+control+plus","resize  grow  height 5 px or 5 ppt; resize  grow  width  5 px or 5 ppt"),
    ("Mod4+control+Shift+minus","resize shrink height 1 px or 1 ppt; resize shrink width  1 px or 1 ppt"),
    ("Mod4+control+Shift+plus","resize  grow  height 1 px or 1 ppt; resize  grow  width  1 px or 1 ppt"),
],

}

MOD4_COMMANDS_TO_RIGHT_RSB = {}

MOD4_COMMANDS["move focused container to workspace and follow"] = []
MOD4_COMMANDS_RSB["switch workspace"] = []

def workspace_commands(X,i):
    key = X["key"]
    MOD4_COMMANDS["move focused container to workspace and follow"].append(("Mod4+control+"+key,"move container to workspace {}; workspace {}".format(i,i)))
    MOD4_COMMANDS_RSB["switch workspace"].append(("Mod4+"+key,"workspace {}".format(i)))

forall(WORKSPACES,workspace_commands)

DIRECTIONS = ["up","left","down","right"]

def arrow_commands(X,i):
    MOD4_COMMANDS[i+" move"] = []
    MOD4_COMMANDS[i+" split and move"] = []
    MOD4_COMMANDS_RSB[i+" focus"] = []
    for j in range(len(DIRECTIONS)):
        MOD4_COMMANDS[i+" move"].append(("Shift+"+X[j],"move "+DIRECTIONS[j]))
        MOD4_COMMANDS[i+" split and move"].append(("control+Shift+"+X[j],"focus {}; split v; focus {}; move {}".format(DIRECTIONS[j],DIRECTIONS[(j+2)%4],DIRECTIONS[j])))
        MOD4_COMMANDS_RSB[i+" focus"].append((""+X[j],"focus "+DIRECTIONS[j]))

forall(ARROW_SETS,arrow_commands)

#end python
