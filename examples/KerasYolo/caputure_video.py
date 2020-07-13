def filenames():
    import time
    frame = 0
    while frame<600:
        yield './video/image%04d_%.6f.jpg' % (frame,time.time())
        frame += 1
    yield None
def cam_daq_3():
    import queue
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import cv2
    import time
    # Initialization of camera
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 20
    time.sleep(3)
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    rawCapture = PiRGBArray(camera, size=(640,480))
    capture_duration = 90

    print('(CAM) Camera initialized')
    print('(CAM) You may now pick up the device, capture will begin in 7 seconds')
    
    print('(CAM) Now begin capturing in {:d} seconds'.format(capture_duration))
    clock = time.time()
    run_until = clock + 90

    
    with camera:
        while True:
            if filenames() is not None:
                camera.capture_sequence(filenames(), use_video_port=True)
                return
            else:
                break
if __name__ == '__main__':
    cam_daq_3()