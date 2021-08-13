# PresensiKKNSimaster
**Automatic daily attendance for KKN in Simaster UGM website in Windows Startup**

**1. Make sure you have Python and Google Chrome Installed**

**2. Download and extract chromedriver to your C:\Program Files (x86)**

    https://sites.google.com/a/chromium.org/chromedriver/downloads
    
**3. If you haven't installed pip, install it by opening cmd and type this, otherwise skip to the next step**

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

**4. Before starting the script, run this in cmd to install some packages**

    pip install selenium
    pip install pywin32
    pip install win10toast

**5. What to change in PresensiKKN.py**

    input username and password
    os.chdir("YourFolderPath")

**6. What to change in PresensiKKN.vbs**

    CreateObject("Wscript.Shell").Run "YourFolderPath\PresensiKKN.bat", 0, True

**7. What to change in PresensiKKN.bat**

    python YourFolderPath\PresensiKKN.py

**8. Now with the scripts all ready, go to Registry Editor in your Windows and go to this path:**

    Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

**9. Right-click > New > String Value**

**10. Name it PresensiKKN and double-click on it**

**11. Change the value data to:**

    YourFilePath\PresensiKKN.vbs

**12. Click OK and Done**
