import os

def read_jpeg_headers(filename):
    with open(filename, 'rb') as file:
        # Verify JPEG start marker
        if file.read(2) != b'\xFF\xD8':
            raise ValueError("Not a valid JPEG file")

        print("JPEG Start Marker Found")

        # Read through segments
        while True:
            marker, = file.read(1)
            if marker != 0xFF:
                raise ValueError("Invalid JPEG marker")

            marker_type, = file.read(1)

            # Check for end of image marker
            if marker_type == 0xD9:
                print("End of Image Marker Found")
                break

            # Read segment length
            length = int.from_bytes(file.read(2), byteorder='big')
            data = file.read(length - 2)

            # SOF0 - Start of Frame (Baseline DCT)
            if marker_type == 0xC0:
                height = int.from_bytes(data[1:3], byteorder='big')
                width = int.from_bytes(data[3:5], byteorder='big')
                print(f"Image dimensions: {width}x{height}")
                print(f"Number of components: {data[5]}")

            # DQT - Define Quantization Table
            elif marker_type == 0xDB:
                print("Quantization Table Found")

            # DHT - Define Huffman Table
            elif marker_type == 0xC4:
                print("Huffman Table Found")

            # SOS - Start of Scan (beginning of compressed data)
            elif marker_type == 0xDA:
                print("Start of Scan Found")
                break

            else:
                print(f"Marker {hex(marker_type)} with length {length} found")

def decode_huffman_data(file, huffman_tables, num_blocks):
    bitstream = get_bitstream(file)
    decoded_blocks = []


    for _ in range(num_blocks):
                d
