import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('Flight03.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1