import torch
import cv2

model = torch.hub.load('.', 'custom', 'best.pt', source='local')

model.conf = 0.5
model.max_det = 1

cam = cv2.VideoCapture(2)

while True:
    try:
        frame = cam.read()[1]
        cv2.imshow("window", frame)
        keystroke = cv2.waitKey(10)
        results = model(frame)
        results.print()

    except KeyboardInterrupt:
        cam.release()
        cv2.destroyAllWindows()
        break


