import cv2

ipv4_url = 'http://255.255.255.255:8080'

cam = f"{ipv4_url}/video"
cap = cv2.VideoCapture(cam)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (600, 600))
    cv2.imshow("Camera do celular", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()
