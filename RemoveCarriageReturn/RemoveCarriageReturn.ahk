#Requires AutoHotkey v2.0


^!c::{
    Send "^c"
    A_Clipboard := StrReplace(A_Clipboard, "-`r`n")
    A_Clipboard := StrReplace(A_Clipboard, "`r`n", A_Space)
}