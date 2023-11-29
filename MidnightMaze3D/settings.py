import math

RES = WIDTH, HEIGHT = 1920, 1020 #1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

PLAYER_POS = 9, 5
PLAYER_ANGLE = -math.pi/2
PLAYER_SPEED = 0.004
PLAYER_SIZE_SCALE = 60
PLAYER_ROT_SPEED = 0.002
Z = 0

MOUSE_SENSITIVITY_X = 0.0001
MOUSE_SENSITIVITY_Y = 0.1
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 200
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT
MOUSE_BORDER_UP = 200
MOUSE_BORDER_DOWN = HEIGHT - MOUSE_BORDER_UP
MAX_LOOK_ANGLE = 4450

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2