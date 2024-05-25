import os
from PIL import Image

ICON_FILENAME = "icon.ico"
DESKTOP_INI_FILENAME = "desktop.ini"
PNG_FILENAME = "ICON0.PNG"

def main():
    parent_folder = input("Please enter the path to the folder containing your PSP/PS3 save folders: ")

    if not os.path.isdir(parent_folder):
        print(f'The specified path "{parent_folder}" is not a directory.')
        return

    for item in os.listdir(parent_folder):
        item_path = os.path.join(parent_folder, item)
        
        if os.path.isdir(item_path):
            png_path = os.path.join(item_path, PNG_FILENAME)
            if os.path.exists(png_path):
                ico_path = os.path.join(item_path, ICON_FILENAME)
                png_to_ico(png_path, ico_path)
                set_folder_icon(item_path)
            else:
                print(f"No {PNG_FILENAME} found in {item_path}")

    print(f"Finished generating icons.")

def png_to_ico(png_path, ico_path):
    try:
        if os.path.exists(ico_path):
            os.unlink(ico_path)

        with Image.open(png_path) as img:
            if img.width < 256:
                img = img.resize((256, int(256 * img.height / img.width)), resample=Image.LANCZOS)
            img.thumbnail((256, 256), Image.LANCZOS)
            background = Image.new("RGBA", (256, 256), (0, 0, 0, 0))
            offset = (int((256 - img.size[0]) / 2), int((256 - img.size[1]) / 2))
            background.paste(img, offset)
            background.save(ico_path, format='ICO', sizes=[(256, 256)])
    except Exception as e:
        print(f"Error converting {png_path} to ICO: {e}")

def set_folder_icon(folder_path):
    try:
        desktop_ini_path = os.path.join(folder_path, DESKTOP_INI_FILENAME)
        icon_path = os.path.join(folder_path, ICON_FILENAME)
        
        if os.path.exists(desktop_ini_path):
            os.system(f'attrib -h -s "{desktop_ini_path}"')

        with open(desktop_ini_path, "w") as desktop_ini:
            desktop_ini.write("[.ShellClassInfo]\n")
            desktop_ini.write(f"IconResource={ICON_FILENAME},0\n")

        os.system(f'attrib +h +s "{desktop_ini_path}"')
        os.system(f'attrib +h "{icon_path}"')
        
        print(f'Saved "{icon_path}" and "{desktop_ini_path}".')
    except PermissionError:
        print(f'Permission denied: "{desktop_ini_path}". You may need to run the script as an administrator.')
    except Exception as e:
        print(f'Error setting folder icon to "{folder_path}": {e}')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")