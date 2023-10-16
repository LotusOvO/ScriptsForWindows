#Requires AutoHotkey v2.0
#SingleInstance Force

^+c::{
    ProcessName := WinGetProcessName("A")
    ReturnString := ""
    windows := ComObject("Shell.Application").Windows
    If (ProcessName ~= "explorer"){
        Class := WinGetClass("A")
        flag := 0
        If (Class ~= "Progman|WorkerW"){
            Controls := WinGetControls("A")
            List := ListViewGetContent("Selected Col1", "SysListView321", "A")
            If (!List){
                ReturnString .= A_Desktop "/"
            }else{
                Loop Parse, List, "`n" {
                    If (flag == 0){
                        flag := 1   
                    } else{
                        ReturnString .= A_Space
                    }
                    tmpStr := ""
                    tmpStr .= A_Desktop "/" A_LoopField
                    If (InStr(FileExist(tmpStr), "D")){
                        tmpStr .= "/"
                    }
                    ReturnString .= tmpStr
                }
            }
        } else If (class ~= "(Cabinet|Explore)WClass"){
            for window in ComObject("Shell.Application").Windows{
                If (window.hwnd == WinGetID("A")){
                    sel := window.Document.SelectedItems
                    If (sel.Count == 0) {
                        ReturnString .= window.Document.Folder.Self.Path "/"
                    }
                    break
                }
            }
            for item in sel{
                If (flag == 0){
                    flag := 1
                } else{
                    ReturnString .= A_Space
                }
                If (InStr(FileExist(item.Path), "D")){
                    ReturnString .= item.Path "/"
                } else{
                    ReturnString .= item.Path
                }
            }
        }
        ReturnString := StrReplace(ReturnString, "\" , "/")
        if (ReturnString)
            A_Clipboard := ReturnString
    }
}
