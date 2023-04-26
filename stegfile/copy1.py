from PIL import Image
import numpy as np

def encode_lsb(img, message):
    # Convert the message to binary format
    message_binary = ''.join([format(ord(c), '08b') for c in message]) + '00000000'
    message_len = len(message_binary)
    
    # Convert the image to a numpy array
    img_np = np.array(img)
    
    # Flatten the image into a 1D array
    img_flat = img_np.reshape(-1)
    
    # Create a copy of the image to be modified
    img_encoded = img_flat.copy()
    
    # Encode the message in the LSB of each pixel
    for i in range(message_len):
        if message_binary[i] == '1':
            img_encoded[i] = img_encoded[i] + 1 if img_encoded[i] % 2 == 0 else img_encoded[i]
        else:
            img_encoded[i] = img_encoded[i] - 1 if img_encoded[i] % 2 == 1 else img_encoded[i]
    
    # Reshape the encoded image back to its original shape
    img_encoded = np.reshape(img_encoded, img_np.shape)
    
    # Convert the numpy array back to an image
    img_encoded = Image.fromarray(np.uint8(img_encoded))
    
    return img_encoded

def decode_lsb(img_encoded):
    # Convert the image to a numpy array
    img_np = np.array(img_encoded)
    
    # Flatten the image into a 1D array
    img_flat = img_np.reshape(-1)
    
    # Decode the message from the LSB of each pixel
    message_binary = ''
    for i in range(len(img_flat)):
        if img_flat[i] % 2 == 1:
            message_binary += '1'
        else:
            message_binary += '0'
        if message_binary[-8:] == '00000000':
            break
    
    # Split the binary message into 8-bit chunks
    message_chunks = [message_binary[i:i+8] for i in range(0, len(message_binary), 8)]
    
    # Convert each chunk to a character
    message = ''.join([chr(int(chunk, 2)) for chunk in message_chunks])
    
    return message

# Open the original image
img = Image.open("color-image.jpg")

# Encode a message in the image
message = "Hello World!"
img_encoded = encode_lsb(img, message)

# Save the encoded image
img_encoded.save("encoded_image.png")

# Decode the message from the encoded image
img_decoded = Image.open("encoded_image.png")
decoded_message = decode_lsb(img_decoded)
print("Decoded message:", decoded_message)
