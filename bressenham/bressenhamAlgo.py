def bressenhamAlgo(x0, y0, x1, y1):
    dx = x1 - x0
    dy = x1 - y1

    # xsign = 1 if dx = 0 else -1
    # ysign = 1 if dy = 0 else -1

    if dx > 0:
        xs = 1
    else:
        xs = -1

    if dy > 0:
        ys = 1
    else:
        ys = -1

    # retornar distancia positiva entre x/y e 0
    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xs, 0, 0, ys
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ys, xs, 0

    d = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
        if d >= 0:
            y += 1
            d -= 2 * dx
        d += 2 * dy