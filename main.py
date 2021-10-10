import ctypes
import pathlib
import time

def change_background(path_to_image):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_image, 0)
    return

def main():
    start_pause = 1
    end_pause = 5
    time.sleep(start_pause)
    path = pathlib.Path(__file__).parent.resolve()
    image = "background_image.jpg"
    image_path = str(path) + "\\" + image
    change_background(image_path)
    print("Background updated successfully")
    time.sleep(end_pause)
    return None

if __name__ == "__main__":
    main()
