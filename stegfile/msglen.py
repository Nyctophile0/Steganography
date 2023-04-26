# correct one

from PIL import Image
import numpy as np


class Stegnography:
    #imgarr = np.asarray(Image.open("bw_image.jpg"))
    #img1darr = imgarr.flatten()
    #print(img1darr)
    def encoding(self, image, msg):
        img = Image.open(image) #color.jpg
        img_a = np.array(img)
        img_arr = img_a.reshape(-1)
        print(img_arr)

        img_encoded = img_arr.copy()

        message =  msg     #input()
        #msg += "<-END->"
        #msgs = msg.encode('ascii')
        #message_binary = ''.join([format(i, '08b') for i in msgs])


        #print(message_binary)

        binary_message = ''.join([format(ord(c), '08b') for c in message]) + '00000000' #00000000 = <-END->
        print(binary_message)

        message_len = len(binary_message)
        print(message_len)

        for i in range(message_len):
                if binary_message[i] == '1':
                    img_encoded[i] = img_encoded[i] + 1 if img_encoded[i] % 2 == 0 else img_encoded[i]
                else:
                    img_encoded[i] = img_encoded[i] - 1 if img_encoded[i] % 2 == 1 else img_encoded[i]
            
        img_encoded = np.reshape(img_encoded, img_a.shape)

        print(img_encoded)

        target_path = "folder/"
        image_path = image

        savePath = target_path + image_path.split(".")[0] + "_enc.png"
        img_encoded = Image.fromarray(np.uint8(img_encoded))
        img_encoded.save(savePath)
        print("encoding done image is saved.")
    def decoding(self, image):
        print("Decoding -----------------------")

        img_encoded = Image.open(image)
        img_np = np.array(img_encoded)
        img_flat = img_np.reshape(-1)
        print(len(img_flat))
            # Decode the message from the LSB of each pixel
        message_binaryy = ''
        for i in range(len(img_flat)):
            if img_flat[i] % 2 == 1:
                message_binaryy += '1'
            else:
                message_binaryy += '0'
            if message_binaryy[-8:] == '00000000':
                break
            # Split the binary message into 8-bit chunks
        print(message_binaryy)
        message_chunks = [message_binaryy[i:i+8] for i in range(0, len(message_binaryy), 8)]
            
            # Convert each chunk to a character
        message = ''.join([chr(int(chunk, 2)) for chunk in message_chunks])
            
        return {"msg:", message}

obj = Stegnography()
#obj.encoding("color-image.jpg", "HEllo, this is secret.")
msg = obj.decoding("folder/color-image_enc.png")
print(msg)