magics = {
    "fire": {
        "damage": 200,
        "radius": {
            1: 20,
            2: 30,
            3: 50
        }
    },
    "water": {
        "damage": 300,
        "radius": {
            1: 10,
            2: 25,
            3: 40
        }
    },
    "earth": {
        "damage": 400,
        "radius": {
            1: 25,
            2: 55,
            3: 70
        }
    },
    "air": {
        "damage": 100,
        "radius": {
            1: 18,
            2: 38,
            3: 60
        }
    }
}

def inside(x1, y1, x2, y2, xc, yc, r):
    xm = max(x1, min(xc, x2))
    ym = max(y1, min(yc, y2))
    
    return ((xm - xc) ** 2 + (ym - yc) ** 2) <= r * r

def get_response(magic, level, x1, y1, x2, y2, xc, yc):
    if inside(x1, y1, x2, y2, xc, yc, magics[magic]["radius"][level]):
        return magics[magic]["damage"]
    
    return 0

T = int(input())

for _ in range(T):
    w, h, x0, y0 = map(int, input().strip().split())
    magic, n, cx, cy = input().strip().split()
    N, cx, cy = map(int, [n, cx, cy])

    x2 = x0 + w
    y2 = y0 + h

    print(get_response(magic, N, x0, y0, x2, y2, cx, cy))
