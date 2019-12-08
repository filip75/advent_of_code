width = 25
height = 6
pixels_in_layer = width * height

with open("input.txt") as file:
    image = file.readline().strip()
    layers = [image[i:i + pixels_in_layer] for i in range(0, len(image), pixels_in_layer)]

    min_zeros = width * height
    result = 0
    for layer in layers:
        if layer.count('0') < min_zeros:
            min_zeros = layer.count('0')
            result = layer.count('1') * layer.count('2')
    print(result)

    final_image = ''
    for i in range(pixels_in_layer):
        for layer in layers:
            if layer[i] != '2':
                final_image += layer[i]
                break
        else:
            final_image += '2'

    for i in range(0, len(final_image), width):
        for c in (final_image[i:i + width]):
            if c == '0':
                print(' ', end='')
            else:
                print('X', end='')
        print()
