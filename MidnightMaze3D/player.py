import pygame as pg
import math
from settings import (PLAYER_POS, PLAYER_SPEED, PLAYER_ANGLE, HEIGHT, PLAYER_SIZE_SCALE, Z,
                      MOUSE_SENSITIVITY_X, MOUSE_SENSITIVITY_Y, MOUSE_MAX_REL, MOUSE_BORDER_LEFT, MOUSE_BORDER_RIGHT,
                      HALF_HEIGHT, HALF_WIDTH, MOUSE_BORDER_UP, MOUSE_BORDER_DOWN, MAX_LOOK_ANGLE)


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.lookheight = Z
        self.diag_move_corr = 1 / math.sqrt(2)
        self.compass_image = pg.image.load("assets/images/compass.jpg")
        self.compass_image.set_colorkey((255, 255, 255))

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        num_key_pressed = -1
        if keys[pg.K_w]:
            num_key_pressed += 1
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            num_key_pressed += 1
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            num_key_pressed += 1
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            num_key_pressed += 1
            dx += -speed_sin
            dy += speed_cos

        # diag move correction
        if num_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr

        self.check_wall_collision(dx, dy)

        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        # self.angle %= math.tau
        # if keys[pg.K_UP]:
        #     self.lookheight += 1 * self.game.delta_time
        # if keys[pg.K_DOWN]:
        #     self.lookheight -= 1 * self.game.delta_time
        if keys[pg.K_r]:
            self.lookheight = 0

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        if my < MOUSE_BORDER_UP or my > MOUSE_BORDER_DOWN:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        # Look left/right
        self.rel_x, self.rel_y = pg.mouse.get_rel()
        self.rel_x = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel_x))
        self.angle += self.rel_x * MOUSE_SENSITIVITY_X * self.game.delta_time

        # Look up/down
        self.rel_y = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel_y))
        self.lookheight -= self.rel_y * MOUSE_SENSITIVITY_Y * self.game.delta_time

        # Bound look up/down
        if self.lookheight <= -MAX_LOOK_ANGLE:
            self.lookheight = -MAX_LOOK_ANGLE
        if self.lookheight >= MAX_LOOK_ANGLE:
            self.lookheight = MAX_LOOK_ANGLE

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'red', (self.x * 100, self.y * 100), 15)
        pg.draw.line(self.game.screen, 'white', (self.x * 100, self.y * 100),
                (self.x * 100 + 100 * math.cos(self.angle), self.y * 100 + 100 * math.sin(self.angle)), 2)

    def compass_draw(self, surface):
        surface.blit(self.game.screen, (0, HEIGHT-self.compass_image.get_height()))

    def update(self):
        self.move()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)