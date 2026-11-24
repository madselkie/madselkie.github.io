
import numpy as np
from PIL import Image, ImageDraw
import math, os

W, H = 1440, 460
S = 2
FPS = 24
DUR = 8.0
N = int(FPS * DUR)
PAPER = np.array([246, 245, 241], dtype=float)
INK = np.array([20, 21, 25], dtype=float)

COLS, ROWS = 30, 6
xs = np.linspace(-0.05, 1.05, COLS)
ys = np.linspace(-0.08, 1.08, ROWS)

def field(u, v, t):
    a = 2*math.pi*t/DUR
    dx = 0.018*np.sin(2*math.pi*v + a) * np.cos(2*math.pi*u*0.5 - a)
    dy = 0.038*np.sin(2*math.pi*u + a) * np.cos(2*math.pi*v*0.5 + a)
    dy += 0.014*np.sin(2*math.pi*u*2.0 - a)
    return u+dx, v+dy

for i in range(N):
    t = i * DUR / N
    img = Image.new('RGB', (W*S, H*S), tuple(PAPER.astype(int)))
    d = ImageDraw.Draw(img)
    U, V = np.meshgrid(xs, ys)
    Xd, Yd = field(U, V, t)
    px = Xd * W * S
    py = Yd * H * S
    edge = 0.45 + 0.55*np.sin(np.pi*np.clip(V,0,1))**0.8

    for c in range(COLS):
        val = float(np.mean(edge[:, c]))
        col = tuple(int(v) for v in (PAPER + (INK-PAPER)*(0.55*val)))
        pts = [(float(px[r, c]), float(py[r, c])) for r in range(ROWS)]
        d.line(pts, fill=col, width=S, joint='curve')
    for r in range(ROWS):
        for c in range(COLS-1):
            val = float((edge[r, c] + edge[r, c+1]) / 2)
            col = tuple(int(v) for v in (PAPER + (INK-PAPER)*(0.22*val)))
            d.line([(float(px[r, c]), float(py[r, c])), (float(px[r, c+1]), float(py[r, c+1]))], fill=col, width=S)

    small = img.resize((W, H), Image.LANCZOS)
    small.save(f'/tmp/hero_{i:04d}.png')
    if i == 0:
        small.save('/home/sprite/work/madselkie/media/hero-poster.jpg', quality=80, optimize=True, progressive=True)
print('ok', N)
