import zlib
import base64

# here we open compressed data
compressed_data = open("compressed.txt", "r").read()

# here we first decode then decompress data
decompress_deta = zlib.decompress(base64.b64decode(compressed_data))

# convert byte to str for writing
decompress_deta = str(decompress_deta, "utf-8")

decompressed_file = open("decompressed.txt", "w")

decompressed_file.write(decompress_deta)
