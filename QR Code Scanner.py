import cv2
from pyzbar.pyzbar import decode
import time

# Open camera
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set width
cam.set(4, 480)  # Set height

while True:
    success, frame = cam.read()
    if not success:
        break  # Exit if the frame is not captured properly

    for i in decode(frame):
        print("Type:", i.type)
        print("Data:", i.data.decode('utf-8'))
        time.sleep(2)  # Reduce sleep time for better responsiveness

    cv2.imshow("Anshu's_QR_Code_Scanner", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
