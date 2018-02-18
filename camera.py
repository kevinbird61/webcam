import cv2

class VideoCamera(object):
    def __init__(self,device_id=0):
        self.video = cv2.VideoCapture(device_id)
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def save_frame(self):
        print "snapshot!"
        success, image = self.video.read()
        cv2.imwrite("/tmp/save.png",image)
