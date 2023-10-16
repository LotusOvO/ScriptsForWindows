#Requires AutoHotkey v2.0

#b::{
    CoordMode "Pixel", "Screen"
    if WinExist("ahk_exe Honeyview.exe"){
        WinClose
    }
    else{
        title := WinGetTitle("A")
        Run ".\black.png",,, &pid
        WinWait "ahk_pid " pid
        WinMove -2560, 0
        Sleep 200
        if PixelGetColor(-1280, 1430) !== "0x000000"
            Send "!{Enter}"
        WinActivate(title)
    }
}