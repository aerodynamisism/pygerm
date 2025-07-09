import curses
import random
import time

DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]
AGE_LIMIT = 1
MAX_GERMS = 4

class Germ:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = random.randint(0, 3)
        self.birth = time.time()
        self.alive = True

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(0)

    height, width = stdscr.getmaxyx()
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    germs = [Germ(width // 2, height // 2)]

    while True:
        now = time.time()

        if len(germs) > MAX_GERMS:
            victim = random.choice(germs)
            victim.alive = False

        for germ in germs:
            if not germ.alive:
                continue

            age = now - germ.birth
            if age >= AGE_LIMIT:
                grid[germ.y][germ.x] = 'X'
                germ.alive = False
                continue

            cell = grid[germ.y][germ.x]
            if cell == ' ':
                grid[germ.y][germ.x] = '#'
            elif cell == '#':
                grid[germ.y][germ.x] = '.'

                for _ in range(20):
                    sx = germ.x + random.randint(-5, 5)
                    sy = germ.y + random.randint(-5, 5)
                    if 0 <= sx < width and 0 <= sy < height and grid[sy][sx] != 'X':
                        germs.append(Germ(sx, sy))
                        break
            elif cell == '.':
                grid[germ.y][germ.x] = ' '

            dir = germ.dir
            nx = germ.x + DX[dir]
            ny = germ.y + DY[dir]
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] != 'X':
                germ.x, germ.y = nx, ny
            else:
                germ.dir = (dir + random.randint(-1, 1)) % 4
            germ.dir = (germ.dir + random.randint(-1, 1)) % 4

        germs = [g for g in germs if g.alive]

        if not germs:
            grid = [[' ' for _ in range(width)] for _ in range(height)]
            germs.append(Germ(width // 2, height // 2))

        stdscr.erase()
        empty_found = False
        for y in range(height):
            for x in range(width):
                ch = grid[y][x]
                try:
                    stdscr.addch(y, x, ch)
                except curses.error:
                    pass
                if ch == ' ':
                    empty_found = True

        if not empty_found:
            stdscr.addstr(height // 2, max(0, (width - 18) // 2), " (TERMINAL INFECTED) ")
            stdscr.refresh()
            time.sleep(2)
            break

        stdscr.refresh()
        time.sleep(0.10)

if __name__ == '__main__':
    curses.wrapper(main)
