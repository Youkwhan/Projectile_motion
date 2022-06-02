import pygame
import math

wScreen = 1000
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))
pygame.display.set_caption("GRAVITY FALLLL")


class Ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)  # black ball
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius - 1)  # outline ball

    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)

        return (newx, newy)


def redrawWindow():
    win.fill((64, 64, 64))
    ball.draw(win)
    pygame.draw.line(win, (255, 255, 255), line[0], line[1])
    pygame.display.update()


def findAngle(pos):
    sX = ball.x
    sY = ball.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2
    # what quadrant your mouse is in the unit circle
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle


ball = Ball(300, 492, 5, (255, 255, 255))

x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False

run = True
while run:

    if shoot:  # ball in motion
        if ball.y < 500 - ball.radius:  # check if hit floor
            time += 0.025  # how fast the ball moves
            po = ball.ballPath(x, y, power, angle, time)
            ball.x = po[0]
            ball.y = po[1]
        else:
            shoot = False
            ball.y = 494

    pos = pygame.mouse.get_pos()
    line = [(ball.x, ball.y), pos]
    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = ball.x  # initial shot
                y = ball.y
                power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2) / 8
                time = 0
                angle = findAngle(pos)
pygame.quit()
