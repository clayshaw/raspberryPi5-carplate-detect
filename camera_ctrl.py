from picamera2 import Picamera2
import time
import subprocess


def init_camera(retry_delay=0.5, max_retries=30):
    """
    重試式初始化 Picamera2，直到相機啟動成功為止，或達到最大重試次數。
    """
    for attempt in range(1, max_retries + 1):
        try:
            picam2 = Picamera2()
            config = picam2.create_still_configuration()
            picam2.configure(config)
            picam2.start()
            time.sleep(3)
            picam2.stop()
            print("相機初始化完成")
            return picam2
        except Exception as e:
            time.sleep(retry_delay)

    print("相機初始化失敗")
    return false



def release_camera(picam2):
    """
    停止並釋放 Picamera2 相機資源，避免 pipeline 卡住。
    """
    try:
        picam2.stop()
        del picam2  # 強制釋放記憶體與 pipeline 資源
        import gc
        gc.collect()  # 強制垃圾回收
        print("相機資源已釋放")
    except Exception as e:
        print(f"相機釋放失敗：{e}")



def take_photo_code(filename: str, picam2: Picamera2):
    if not filename.endswith(".jpg"):
        filename += ".jpg"
    
    try:
        picam2.start()
        time.sleep(0.17)
        picam2.capture_file('./photo/' + filename)
        time.sleep(0.2)
        picam2.stop()
        return True
    except Exception as e:
        print(f"拍照失敗：{e}")
        return False


"""
def take_photo_cmd(filename: str):
    
    #拍一張照片並儲存為 JPEG 檔案。若未輸入副檔名，會自動加上 .jpg。
    #:param filename: 使用者指定的照片檔名（可省略副檔名）
    
    # 自動補上 .jpg 副檔名（若沒有的話）
    if not filename.endswith(".jpg"):
        filename += ".jpg"

    try:
        subprocess.run(["rpicam-still", "-t", "20", "-o", filename], check=True)
        return True
    except subprocess.CalledProcessError:
        return False
"""


def wait_for_camera_ready(retry_delay=0.5, max_retries=20):
    """
    嘗試初始化 Picamera2，直到成功為止。
    :param retry_delay: 每次重試等待的秒數
    :param max_retries: 最多重試次數（避免無限卡死）
    """
    for attempt in range(max_retries):
        try:
            cam = Picamera2()
            cam.close()  # 初始化成功後立即關閉，代表 pipeline 通暢
            print(f"相機初始化成功（第{attempt+1}嘗試）")
            return True
        except Exception as e:
            print(f"相機未就緒，第{attempt+1}重試...")
            time.sleep(retry_delay)

    print("相機在預期時間內仍無法初始化")
    return False

