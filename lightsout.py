import pew


pew.init()
screen = pew.Pix.from_iter((
    (2, 0, 0, 0, 0, 0, 2, 0),
    (0, 0, 0, 2, 0, 2, 2, 2),
    (0, 0, 0, 0, 2, 0, 2, 0),
    (0, 0, 0, 0, 2, 2, 0, 2),
    (0, 0, 0, 0, 0, 2, 0, 0),
    (0, 0, 2, 0, 0, 2, 0, 2),
    (2, 0, 2, 2, 2, 0, 2, 0),
    (2, 2, 2, 2, 0, 0, 2, 2),
))

x = 4
y = 1
blink = True

while True:
    screen.pixel(x, y, 0 if screen.pixel(x, y) < 4 else 2)

    keys = pew.keys()

    dx = 0
    dy = 0

    if keys & pew.K_UP and y > 0:
        dy = -1
    elif keys & pew.K_DOWN and y < 7:
        dy = 1
    elif keys & pew.K_LEFT and x > 0:
        dx = -1
    elif keys & pew.K_RIGHT and x < 7:
        dx = 1

    target = screen.pixel(x + dx, y + dy)

    if target in {0,2} and (keys & pew.K_X):
        screen.pixel(x, y, 0 if screen.pixel(x,y) in {2} else 2)
        screen.pixel(x+1, y, 0 if screen.pixel(x+1,y) in {2} else 2)
        screen.pixel(x-1, y, 0 if screen.pixel(x-1,y) in {2} else 2)
        screen.pixel(x, y+1, 0 if screen.pixel(x,y+1) in {2} else 2)
        screen.pixel(x, y-1, 0 if screen.pixel(x,y-1) in {2} else 2)

    x += dx
    y += dy

    count = 0
    for b in range(8):
        for a in range(8):
            if screen.pixel(a, b) == 2:
                count += 1
    if count == 0:
        break

    screen.pixel(x, y, (3 if blink else 2) +
                 (4 if screen.pixel(x, y) in {2, 7} else 0))

    blink = not blink

    pew.show(screen)

    pew.tick(1 / 6)
