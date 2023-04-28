# import unittest
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
# if __name__ == '__main__':
#     unittest.main()


from PIL import Image
import io

# Open the corrupted file
with open('CorruptedImage', 'rb') as f:
    data = f.read()

# Check the PNG file signature
if data[:8] != b'\x89PNG\r\n\x1a\n':
    raise ValueError('File is not a valid PNG')

# Find the location of the IDAT chunk
idat_start = data.find(b'IDAT')
if idat_start == -1:
    raise ValueError('File does not contain an IDAT chunk')

# Find the length of the IDAT chunk
idat_length = int.from_bytes(data[idat_start-4:idat_start], byteorder='big')

# Read in the remaining data
with open('CorruptedImage', 'rb') as f:
    f.seek(idat_start+8)
    idat_data = f.read(idat_length)

# Construct a new PNG file with the IDAT chunk data replaced
new_data = data[:idat_start+8] + idat_data + data[idat_start+8+idat_length:]

# Attempt to open the reconstructed image
try:
    img = Image.open(io.BytesIO(new_data))
    img.show()
except Exception as e:
    print('Error opening image:', e)

# Write the reconstructed file to disk
with open('reconstructed.png', 'wb') as f:
    f.write(new_data)
