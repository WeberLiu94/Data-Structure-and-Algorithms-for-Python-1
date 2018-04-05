def fun(shi,fen):
    if shi >= 12:
        shi -= 12
    angel_shi = 30 * shi + 30 * (fen / 60)
    print(angel_shi)
    angel_fen = 6 * fen
    print(angel_fen)
    angel = abs(angel_shi - angel_fen)
    if (angel > 180):
        angel = 360 - angel
    return angel

print(fun(1,45))