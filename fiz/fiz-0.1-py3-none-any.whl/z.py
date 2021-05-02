from pathlib import Path
from collections import deque

ABS = Path(__file__).parent
P26 = tuple(map(lambda x: 26 ** x, range(5)))
OFF = lambda x: sum(map(lambda y: P26[y], range(x)))
A26 = lambda x, y: sum(map(lambda i, z: P26[i] * (ord(z) - 97), range(x), reversed(y)))
HYP = lambda x, y: y.join(map(lambda z: z.title(), x.split('-')))

with open(ABS / 'i.txt') as f:
    TRANSFER = f.read().splitlines()

class FizError(Exception): ...

def Fiz(s: bytes, p: str='.') -> bytes:
    w = len(s) * 8
    s = int.from_bytes(s, 'big')
    trace = deque()
    result = []

    while w:
        for i in range(len(trace), -1, -1):
            try:
                t = TRANSFER[OFF(i) + A26(i, trace)]
            except IndexError as e:
                raise FizError(
                    'index error, maybe a broken boundary conditions, or you mess the transfer table; '
                    'report this to https://github.com/20x48/fiz/issues please'
                ) from e
            v = len(t)
            if v:
                if v & 16:  v = 4
                elif v & 8: v = 3
                elif v & 4: v = 2
                elif v & 2: v = 1
                else:       v = 0
                if v:
                    if w > v:
                        w -= v
                        n = s >> w
                        s &= (1 << w) - 1
                    else:
                        n = s
                        w = 0
                    c = t[n]
                else:
                    c = t[0]
                result.append(c)
                if c == '-':
                    trace.clear()
                else:
                    if len(trace) == 4:
                        trace.popleft()
                    trace.append(c)
                break
        else:
            raise FizError('unknown error, report this to https://github.com/20x48/fiz/issues please')

    return HYP(''.join(result), p)

if __name__ == '__main__':
    for i, s in enumerate((
        b'\xC7\xD2\xD5\xDB\xC1\xF8\xA3\xAC\xB4\xFD\xCB\xFB\xC8\xD5\xA3\xAC\xD4\xD9\xCF\xE0\xB7\xEA',
        b'\xCE\xD2\xCE\xAA\xC4\xE3\x20\xB3\xAA\xD2\xBB\xC7\xFA\x20\xC8\xE7\xD3\xCE\xCB\xBF\xB5\xC4\xC6\xF8\xCF\xA2',
        b'\xCC\xE1\xB1\xCA\xD7\xDF\xB5\xA4\xC7\xE0\x20\xBA\xE1\xC6\xC3\xCB\xAE\xC4\xAB\x20\xB7\xD6\xB1\xF0\xD2\xD1\xB9\xFD\xC7\xA7\xC7\xEF\x20\xCA\xAE\xC0\xEF\xC7\xEF\xD2\xB6\xBA\xEC\x20\xD6\xB4\xB1\xCA\xBB\xAD\xCC\xC4\xCE\xAA\xBE\xFD\xC1\xF4\x20\xCA\xB1\xB9\xE2\xC8\xE7\xC1\xF7\xCB\xAE\x20\xB5\xE3\xB5\xE3\xB0\xA7\xB3\xEE\x20\xBD\xF1\xCF\xA6\xBF\xD5\xD2\xD0\xD0\xA1\xC2\xA5\x20\xBE\xB2\xBF\xB4\xBA\xD3\xB1\xDF\xBF\xDD\xC1\xF8\x20\xC8\xD4\xBF\xC9\xBC\xFB\xBE\xFD\xB7\xF1',
        b'\xD2\xFB\xB9\xFD\xD2\xBB\xD5\xB5\xD3\xEA\xBA\xF3\xCC\xEC\xC7\xE0\xB4\xC9\x20\xD2\xB2\xB2\xBB\xCB\xE3\xC0\xB4\xB3\xD9',
        b'\xB1\xCB\xCA\xB1\xC1\xB5\x20\xD4\xB8\xBA\xA3\xCA\xC4\xC9\xBD\xC3\xCB'), 1):
        print(f'--- {i} ---')
        print(f'In:  {int.from_bytes(s, "big"):X}')
        print(f'Out: {Fiz(s)}')