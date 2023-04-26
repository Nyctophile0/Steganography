from PIL import Image
import numpy as np

imgarr = np.asarray(Image.open("color-image.jpg"))
img1darr = imgarr.flatten()
print(img1darr)

msg = input()
msg += "<-END->"
msg = msg.encode('ascii')
message_bits = ''.join([format(i, '08b') for i in msg])

print(message_bits)