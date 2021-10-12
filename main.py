import ctypes
import pathlib
import time
from screeninfo import get_monitors

def change_background(path_to_image):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_image, 0)
    return

def monitors_check():
    monitors = 0
    for m in get_monitors():
        monitors += 1
        print(str(m))
    return monitors

def main(background_file, s_pause, e_pause):
    time.sleep(s_pause)
    path = pathlib.Path(__file__).parent.resolve()
    image = background_file
    image_path = str(path) + "\\" + image
    change_background(image_path)
    print("Background updated successfully!")
    time.sleep(e_pause)
    return None

if __name__ == "__main__":
    start_pause = 1
    end_pause = 5
    expected_monitors = 2
    num_monitors = monitors_check()
    print("\nExpected monitors: {exp}\nFound monitors: {found}".format(exp=expected_monitors, found=num_monitors))

    if num_monitors == expected_monitors:
        main("background_image.jpg", start_pause, end_pause)
    else:
        print("Background image not updated.")
        time.sleep(end_pause)
