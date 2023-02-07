# Remote Control Emulator
Emulator remote control AIWA RC-CAS01 via COM-port

## Assembling
The build requires PyQt5 and PyInstaller

*Build command in pyinstaller:* pyinstaller --add-data .\css\style.css;css --add-data .\resources\Icon.ico;resources --add-data ".\resources\Remote Controller.jpg";resources --icon=.\resources\Icon.ico --noconsole main.py

## COM-Port selection
![image](https://user-images.githubusercontent.com/109802024/217218945-a33f8e43-619c-47e5-845a-618032b53af1.png)

## Pressing buttons
![image](https://user-images.githubusercontent.com/109802024/217219002-4808ceff-da52-4035-8d27-6cbb33a0a200.png)
