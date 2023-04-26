from PIL import Image
import numpy as np

img = np.asarray(Image.open('color_image.jpg'))
W, H = img.shape

message = input()
message += '[END]'
message = message.encode('ascii')
message_bits = ''.join([format(i, '08b') for i in message])
img = img.flatten()

for idx, bit in enumerate(message_bits):
    val = img[idx]
    val = bin(val)
    val = val[:-1] + bit
    img[idx] = int(val, 2)

img = img.reshape(W, H)
img = Image.fromarray(img)
img.save("tree_modified.jpg")

img = np.asarray(Image.open('tree_modified.jpg'))
img = img.flatten()
msg = ""
idx = 0
while msg[-5:] != '[END]':
    bits = [bin(i)[-1] for i in img[idx:idx+8]]
    bits = ''.join(bits)
    msg += chr(int(bits, 2))
    idx += 8
    if idx > img.shape[0]:
        print("No hidden message")
        break
print(msg)