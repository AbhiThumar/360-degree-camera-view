def capture_n_save():
    import cv2
    import os


    def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
        cap = cv2.VideoCapture(device_num)

        if not cap.isOpened():
            return

        os.makedirs(dir_path, exist_ok=True)
        base_path = os.path.join(dir_path, basename)

        n = 0
        while True:
            ret, frame = cap.read()
            cv2.imshow(window_name, frame)
            key = cv2.waitKey(delay) & 0xFF
            if key == ord('c'): #to capture the fraame press c
                cv2.imwrite('{}{}.{}'.format(base_path, n, ext), frame)
                n += 1
            elif key == ord('q'): #to quit from window press q
                break

        cv2.destroyWindow(window_name)


    save_frame_camera_key(0,'C:/Users/fabhi/Desktop', '')

capture_n_save()
