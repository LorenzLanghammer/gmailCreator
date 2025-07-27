import os
import subprocess
import random
import shutil
import winreg
import ctypes


fonts = [
    "BELL",
    "COOPBL",
    "CHILLER",
    "CALIST",
    "CENTURY",
    "MAIAN",
    "BRADHITC",
    "ANTIQUAB",
    "NIAGENG",
    "GOUDOS",
    "HTOWERT",
    "INFORMAN",
    "JUICE",
    "GARA",
    "ELEPHNT",
    "BASKVILL",
    "COLONNA",
    "CURLZ___",
    "CALIFB",
    "BOD_B",
    "FRSCRIPT",
    "GIL_____",
    "CENTURY",
    "IMPRISHA",
    "LFAX",
    "HARLOWSI",
    "HARNGTON"
]

FONT_BACKUP_FOLDER = r"C:\Users\stefa\Documents\client\saved_fonts"
FONT_INSTALL_FOLDER = r"C:\Windows\Fonts"
NUM_FONTS_TO_REINSTALL = 10  # Change this to reinstall more/less
fonts_to_install = random.sample(fonts, min(NUM_FONTS_TO_REINSTALL, len(fonts)))
#fonts_to_install = fonts

async def install_fonts():

    for font in fonts_to_install:
        ttf_filename = f"{font}.TTF"
        src = os.path.join(FONT_BACKUP_FOLDER, ttf_filename)
        dest = os.path.join(FONT_INSTALL_FOLDER, ttf_filename)

        if not os.path.exists(src):
            print(f"Font file not found: {src}")
            continue

        print(f"Installing {ttf_filename}")

        try:
            shutil.copyfile(src, dest)
            font_display_name = ttf_filename
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts",
                            0, winreg.KEY_SET_VALUE) as reg:
                winreg.SetValueEx(reg, font_display_name, 0, winreg.REG_SZ, ttf_filename)
        
        except Exception as e:
            print(f"Error installing {ttf_filename}: {e}")

        FR_PRIVATE = 0x10
        FR_NOT_ENUM = 0x20

        result = ctypes.windll.gdi32.AddFontResourceExW(src, 0, 0)
        if result == 0:
            print(f"Failed to load font into memory: {src}")
        else:
            print(f"Font loaded into memory: {src}")

        HWND_BROADCAST = 0xFFFF
        WM_FONTCHANGE = 0x001D
        ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_FONTCHANGE, 0, 0)



async def uninstall_fonts():
    for font in fonts_to_install:
        ttf_filename = f"{font}.TTF"
        font_path = os.path.join(FONT_INSTALL_FOLDER, ttf_filename)

        print(f"Uninstalling {ttf_filename}...")

        # 1. Unload from memory
        result = ctypes.windll.gdi32.RemoveFontResourceExW(font_path, 0, 0)
        if result == 0:
            print(f"Failed to unload font from memory: {font_path}")
        else:
            print(f"Font unloaded from memory: {font_path}")

        # 2. Delete registry key
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts",
                                0, winreg.KEY_SET_VALUE) as reg:
                try:
                    winreg.DeleteValue(reg, ttf_filename)
                    print(f"Deleted registry key for {ttf_filename}")
                except FileNotFoundError:
                    print(f"Registry key for {ttf_filename} not found.")
        except PermissionError:
            print("Permission denied: run script as administrator.")

        # 3. Delete font file
        try:
            if os.path.exists(font_path):
                os.remove(font_path)
                print(f"Deleted font file: {font_path}")
            else:
                print(f"Font file not found: {font_path}")
        except Exception as e:
            print(f"Error deleting font file: {e}")

    # 4. Notify system of font change
    HWND_BROADCAST = 0xFFFF
    WM_FONTCHANGE = 0x001D
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_FONTCHANGE, 0, 0)

        





