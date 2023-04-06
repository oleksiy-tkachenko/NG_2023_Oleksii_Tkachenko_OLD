def draw(size = 6, maxsize = 6):
    print((size * " ") + ((abs(size-maxsize)*2 * "O") + (size * " ")))
    if size > 0:
        draw(size-1, maxsize)
    print((size * " ") + ((abs(size-maxsize)*2 * "O") + (size * " ")))
draw()