
Set objShell = CreateObject("WScript.Shell")
Dim time
time = 10000
do  
    objShell.Run "video.mp4"
    WScript.Sleep time
    if time > 1000 then
        time = time - 1000
    end if
    if time = 1000 then
    do
        objShell.Run "video.mp4"
    loop
    end if
loop