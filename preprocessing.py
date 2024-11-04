def read_pgm(filename):
    with open(filename, 'r') as file:
        # Check the file format
        format_type = file.readline().strip()
        assert format_type == 'P2', "Not an ASCII PGM file"


        # Skip comments
        line = file.readline().strip()
        while line.startswith('#'):
            line = file.readline().strip()


        # Read image dimensions 
        width, height = map(int, line.split())


        # Read the maximum pixel value (usually 255)
        max_value = int(file.readline().strip())
        assert max_value == 255, "This reader only supports 8-bit PGM images"

        # Read pixel data
        pixels = []
        for line in file:
            pixels.extend(map(int, line.split()))

        # Reshape pixel list into 2D array
        image = pixels[i * width:(i+1) * width for i in range(height)]
        return image
