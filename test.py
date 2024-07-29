import os
import shutil


def find_executable(app_name):
    # Common directories where executables might be located
    common_dirs = [
        os.environ["PROGRAMFILES"],
        os.environ["PROGRAMFILES(X86)"],
        os.environ["WINDIR"],
        os.path.join(os.environ["WINDIR"], "System32"),
    ]

    for directory in common_dirs:
        for root, dirs, files in os.walk(directory):
            if app_name in files:
                return os.path.join(root, app_name)
    return None


app_name = "discord.exe"  # Replace with your application executable name
app_path = find_executable(app_name)
if app_path:
    print(f"The path of {app_name} is: {app_path}")
else:
    print(f"{app_name} not found")