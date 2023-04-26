from PIL import Image
import numpy as np

img = np.asarray(Image.open("color_image.jpg"))
imgarr = img.flatten()
print(len(imgarr))

w, h = img.shape[0], img.shape[1]
print(w, h)
msg = "hello"

msg+="<-END->"
print("msg = ", msg)
msg = msg.encode('ascii')
lst = []
message_bits = ''.join([format(i,'08b') for i in msg])
for i in msg:
    lst.append(format(i, '08b'))
print("msgbits = ",lst)

print("msg_bits=", message_bits)


#for count, bit in enumerate(message_bits):
val = bin(imgarr[0])
print(imgarr[0])
print(int(val[:-1] + str(0), 2))   #base 2


'''for count, bit in enumerate(message_bits):
    val = imgarr[count]
    val = bin(val)
    val = val[:-1] + bit
    imgarr[count] = int(val, 2)'''

for count, bit in enumerate(message_bits):
    val = imgarr[count]
    val = bin(val)
    lsb = val[-1]
    if bit == '0':
        if lsb == '1':
            val = val[:-1] + '0'
    elif bit == '1':
        if lsb == '0':
            val = val[:-1] + '1'
    imgarr[count] = int(val, 2)


imgarr = np.reshape(imgarr, img.shape)
img = Image.fromarray(imgarr)

img.save("modified.jpg")

print("Encryption is done.")

print("DEcyrption -")

img = np.asarray(Image.open("color_image.jpg"))
img = img.flatten()

msg = ''
idx = 0 

while msg[-5:] != '<-END->':
    bits = [bin(i)[-1] for i in img[idx: idx+8]]
    bits = ''.join(bits)
    ascii_code = int(bits, 2)
    if ascii_code > 127:
        print("No hidden message")
        break
    msg += chr(ascii_code)
    idx += 8

'''for count, bit in enumerate(message_bits):
    val = imgarr[count]
    val = bin(val)
    lsb = val[-1]
    if lsb == '0':
        extracted_bits += '0'
    else:
        extracted_bits += '1'

msg = ''
for i in range(0, len(extracted_bits), 8):
    byte = extracted_bits[i:i+8]
    ascii_code = int(byte, 2)
    msg += chr(ascii_code)
'''
print(msg)