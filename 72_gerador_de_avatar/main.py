import pagan

input = "Python"

img = pagan.Avatar(input, pagan.SHA384)
img.show()


img.save(path='imgs/', filename=f'{input}.png')
img.change(str(input), pagan.SHA384)
