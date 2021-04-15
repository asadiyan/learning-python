import zlib
import base64

# here we open our file in a read mode and save it in a object or variable
data = open("test-for-compress.txt", "r").read()

# here we conver data to byte type because for compressing we should pass it in byte type
data_bytes = bytes(data, "utf-8")

# here we pas data_byte to compress function to compressing and save it in object or variable
# the 9 up there is the level of compression which start`s from 0 to 9
compress_data = base64.b64encode(zlib.compress(data_bytes, 9))

# here we decode our compress_data because write mode just accept str file not encoded byte file 
decoded_data = compress_data.decode("utf-8")

# here we open a new file in write mode and save it in a object or variable
compression_file = open("compressed.txt", "w")

# now we write our decoded file into our compressed.txt file
compression_file.write(decoded_data)
