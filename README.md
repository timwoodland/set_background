# Read Me

The function of this scrip is to replace the background on a machine running Windows 10. It relies on having the `screeninfo` package installed.

The scrip looks for the image file titled `background_image.jpg` which must be in the root of the directory containing this script.

The script makes use of the `ctypes`, `pathlib` and `time` modules.

The original python script (`main.py`) is read by the `set_background.bat` file, which then runs automatically using Windows Task Scheduler. Therefore, updates to `main.py` do not require updates to the `.bat` file.

The task name in Task Scheduler is Set background and runs at login + 1 minute.