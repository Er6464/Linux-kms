import subprocess
import time

TARGET = "0079:0006"
steam_opened = False

while True:
    result = subprocess.run(
        ["lsusb"],
        capture_output=True,
        text=True
    )

    if TARGET in result.stdout:
        if not steam_opened:
            print("พบจอย เปิด Steam")
            subprocess.Popen(["steam"])
            steam_opened = True
    else:
        steam_opened = False

    time.sleep(1)