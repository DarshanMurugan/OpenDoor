import cv2
from picamera2 import picamera2
from django.http import StreamingHttpResponse

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640,480)}))
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()

        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        _, buffer = cv2.imencode('.jpg', frame_bgr, [cv2.IMWRITE_JPEG_QUALITY, 70])

        frame_bytes = buffer.tobytes()
        yield (
            b'--frame\r\n'
            b'Conetent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'

            )
def video_stream(request):
    return StreamingHttpResponse(
        generate_frames(),
        content_type = 'multipart/x-mixed-replace; boundary=frame'
    )
