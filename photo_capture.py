from picamera2 import Picamera2
import time
import subprocess

import os



import camera_ctrl
import camera_detect


if __name__ == "__main__":
    """
    for fname in ["cmd.jpg", "code.jpg"]:
        if os.path.exists(fname):
            os.remove(fname)
            print(f"刪除舊檔案:{fname}")
    """

    for fname in ["cmd.jpg", "code.jpg"]:
        if os.path.exists(fname):
            os.remove(fname)
            print(f"\n刪除舊檔案:{fname}")

    t1 = time.time()
    picam2 = camera_ctrl.init_camera()
    t2 = time.time()
    print('\ntime elapsed: ' + str(round(t2-t1, 2)) + ' seconds')

    filename_code = "code1"
    t1 = time.time()
    result1 = camera_ctrl.take_photo_code(filename_code, picam2)
    t2 = time.time()

    filename_code = "code2"
    t3 = time.time()
    result2 = camera_ctrl.take_photo_code(filename_code, picam2)
    t4 = time.time()

    filename_code = "code3"
    t5 = time.time()
    result3 = camera_ctrl.take_photo_code(filename_code, picam2)
    t6 = time.time()
        

    if result1:
        print(f"\n拍照成功:{filename_code}")
    else:
        print("❌ 拍照失敗。")
    print('time elapsed: ' + str(round(t2-t1, 2)) + ' seconds')


    if result2:
        print(f"\n拍照成功:{filename_code}")
    else:
        print("❌ 拍照失敗。")
    print('time elapsed: ' + str(round(t4-t3, 2)) + ' seconds')


    if result3:
        print(f"\n拍照成功:{filename_code}")
    else:
        print("❌ 拍照失敗。")
    print('time elapsed: ' + str(round(t6-t5, 2)) + ' seconds')


    camera = camera_detect.is_camera_available()
    print("\n相機偵測結果:\n" + camera)