import subprocess


def is_camera_available():
    """
    執行 rpicam-hello --list-cameras，只回傳第一顆相機的型號與接腳位置
    """
    result = subprocess.run(["rpicam-hello", "--list-cameras"],
                            capture_output=True, text=True, check=True)
    output = result.stdout.strip()

    # 分行找出以 "0 :" 開頭的相機資訊行
    for line in output.splitlines():
        if line.strip().startswith("0 :"):
            return line.strip()

    return "沒有偵測到相機"