"""
Controls:
    LEFT / RIGHT / A / D  -> move ship
    SPACE                 -> shoot
    P                      -> pause
    ENTER                  -> restart after game over / win
    ESC                    -> quit

Run:
    pip install pygame
    python space_invaders.py
"""

import pygame
import random
import sys
import math


pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (5, 5, 15)
WHITE = (240, 240, 240)
GREEN = (60, 220, 100)
RED = (220, 60, 60)
YELLOW = (240, 220, 60)
CYAN = (60, 220, 220)
MAGENTA = (220, 60, 220)
GRAY = (90, 90, 100)
ORANGE = (240, 150, 50)

FONT_BIG = pygame.font.SysFont("consolas", 56, bold=True)
FONT_MED = pygame.font.SysFont("consolas", 32, bold=True)
FONT_SMALL = pygame.font.SysFont("consolas", 20)

ENEMY_ROWS = 5
ENEMY_COLS = 10
ENEMY_ROW_COLORS = [MAGENTA, RED, ORANGE, YELLOW, CYAN]


class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(0.5, 2.5)
        self.size = random.choice([1, 1, 2])

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self, surf):
        shade = 120 + int(self.speed * 40)
        pygame.draw.rect(surf, (shade, shade, shade), (self.x, self.y, self.size, self.size))


stars = [Star() for _ in range(120)]



class Player:
    def __init__(self):
        self.width, self.height = 50, 34
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 70
        self.speed = 6
        self.lives = 3
        self.cooldown = 0
        self.cooldown_max = 20
        self.alive = True
        self.blink_timer = 0

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        self.x = max(10, min(WIDTH - self.width - 10, self.x))
        if self.cooldown > 0:
            self.cooldown -= 1

    def shoot(self, bullets):
        if self.cooldown == 0:
            bullets.append(Bullet(self.x + self.width // 2 - 2, self.y, -9, GREEN, owner="player"))
            self.cooldown = self.cooldown_max

    def draw(self, surf):
        cx = self.x + self.width // 2
        # ship body (simple vector ship)
        points = [
            (cx, self.y),
            (self.x, self.y + self.height),
            (self.x + 10, self.y + self.height - 8),
            (self.x + self.width - 10, self.y + self.height - 8),
            (self.x + self.width, self.y + self.height),
        ]
        pygame.draw.polygon(surf, GREEN, points)
        pygame.draw.rect(surf, CYAN, (cx - 4, self.y + 10, 8, 14))



class Enemy:
    def __init__(self, x, y, row):
        self.x = x
        self.y = y
        self.width, self.height = 40, 28
        self.row = row
        self.color = ENEMY_ROW_COLORS[row % len(ENEMY_ROW_COLORS)]
        self.points = (ENEMY_ROWS - row) * 10
        self.alive = True
        self.anim = random.choice([0, 1])
        self.anim_timer = random.randint(0, 30)

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.anim_timer += 1
        if self.anim_timer >= 30:
            self.anim_timer = 0
            self.anim = 1 - self.anim

    def draw(self, surf):
        x, y, w, h = self.x, self.y, self.width, self.height
        color = self.color
        # body
        pygame.draw.rect(surf, color, (x + 6, y + 6, w - 12, h - 12))
        pygame.draw.rect(surf, color, (x, y + 12, w, 8))
        # eyes
        pygame.draw.rect(surf, BLACK, (x + 10, y + 12, 6, 6))
        pygame.draw.rect(surf, BLACK, (x + w - 16, y + 12, 6, 6))
        # legs, animated
        if self.anim == 0:
            pygame.draw.rect(surf, color, (x + 4, y + h - 4, 6, 6))
            pygame.draw.rect(surf, color, (x + w - 10, y + h - 4, 6, 6))
        else:
            pygame.draw.rect(surf, color, (x, y + h - 4, 6, 6))
            pygame.draw.rect(surf, color, (x + w - 6, y + h - 4, 6, 6))



class Bullet:
    def __init__(self, x, y, vy, color, owner):
        self.x = x
        self.y = y
        self.vy = vy
        self.color = color
        self.owner = owner
        self.width, self.height = 4, 14

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.vy

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect)

    def offscreen(self):
        return self.y < -20 or self.y > HEIGHT + 20



class Barrier:
    BLOCK = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blocks = set()
        shape = [
            "  XXXXXXXXXX  ",
            " XXXXXXXXXXXX ",
            "XXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXX",
            "XXXX      XXXX",
            "XXX        XXX",
        ]
        for row_i, row in enumerate(shape):
            for col_i, ch in enumerate(row):
                if ch == "X":
                    self.blocks.add((col_i, row_i))

    def rects(self):
        for (cx, cy) in self.blocks:
            yield pygame.Rect(self.x + cx * self.BLOCK, self.y + cy * self.BLOCK, self.BLOCK, self.BLOCK)

    def hit(self, bullet_rect):
        for (cx, cy) in list(self.blocks):
            r = pygame.Rect(self.x + cx * self.BLOCK, self.y + cy * self.BLOCK, self.BLOCK, self.BLOCK)
            if r.colliderect(bullet_rect):
                # remove a small cluster for a satisfying chip effect
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        self.blocks.discard((cx + dx, cy + dy))
                return True
        return False

    def draw(self, surf):
        for r in self.rects():
            pygame.draw.rect(surf, GREEN, r)



class UFO:
    def __init__(self):
        self.width, self.height = 50, 22
        self.x = -self.width
        self.y = 50
        self.speed = 3
        self.alive = True
        self.points = random.choice([50, 100, 150, 300])

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.alive = False

    def draw(self, surf):
        pygame.draw.ellipse(surf, MAGENTA, (self.x, self.y + 8, self.width, self.height - 8))
        pygame.draw.ellipse(surf, CYAN, (self.x + 14, self.y, self.width - 28, 14))



class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        angle = random.uniform(0, math.tau)
        speed = random.uniform(1, 4)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = random.randint(15, 30)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1

    def draw(self, surf):
        if self.life > 0:
            pygame.draw.rect(surf, self.color, (int(self.x), int(self.y), 3, 3))



class Game:
    def __init__(self):
        self.reset(full=True)

    def reset(self, full=False):
        self.player = Player()
        self.player_bullets = []
        self.enemy_bullets = []
        self.particles = []
        self.enemy_dir = 1
        self.enemy_speed = 1.0
        self.enemy_move_timer = 0
        self.enemy_shoot_timer = 0
        self.ufo = None
        self.ufo_timer = random.randint(400, 800)
        self.state = "playing"  # playing, paused, gameover, win
        self.message = ""
        if full:
            self.score = 0
            self.level = 1
            self.high_score = load_high_score()
        self.spawn_enemies()
        self.spawn_barriers()

    def spawn_enemies(self):
        self.enemies = []
        start_x, start_y = 80, 90
        gap_x, gap_y = 55, 45
        for row in range(ENEMY_ROWS):
            for col in range(ENEMY_COLS):
                x = start_x + col * gap_x
                y = start_y + row * gap_y
                self.enemies.append(Enemy(x, y, row))
        self.enemy_speed = 1.0 + (self.level - 1) * 0.35

    def spawn_barriers(self):
        self.barriers = []
        num = 4
        spacing = WIDTH // (num + 1)
        for i in range(num):
            bx = spacing * (i + 1) - 42
            by = HEIGHT - 170
            self.barriers.append(Barrier(bx, by))

    
    def update(self):
        for s in stars:
            s.update()

        if self.state != "playing":
            return

        keys = pygame.key.get_pressed()
        self.player.update(keys)

        # bullets
        for b in self.player_bullets:
            b.update()
        for b in self.enemy_bullets:
            b.update()
        self.player_bullets = [b for b in self.player_bullets if not b.offscreen()]
        self.enemy_bullets = [b for b in self.enemy_bullets if not b.offscreen()]

        # enemy movement (classic side-step-down pattern)
        self.enemy_move_timer += 1
        move_interval = max(4, int(20 - self.enemy_speed * 4))
        edge_hit = False
        alive_enemies = [e for e in self.enemies if e.alive]
        if self.enemy_move_timer >= move_interval:
            self.enemy_move_timer = 0
            for e in alive_enemies:
                e.x += 10 * self.enemy_dir
            for e in alive_enemies:
                if e.x <= 10 or e.x + e.width >= WIDTH - 10:
                    edge_hit = True
            if edge_hit:
                self.enemy_dir *= -1
                for e in alive_enemies:
                    e.y += 20
        for e in alive_enemies:
            e.update()

        # enemy reached player -> game over
        for e in alive_enemies:
            if e.y + e.height >= self.player.y:
                self.trigger_gameover("THE INVASION REACHED YOU")

        # enemy shooting
        self.enemy_shoot_timer += 1
        shoot_interval = max(20, int(55 - self.level * 3))
        if self.enemy_shoot_timer >= shoot_interval and alive_enemies:
            self.enemy_shoot_timer = 0
            shooter = random.choice(alive_enemies)
            self.enemy_bullets.append(
                Bullet(shooter.x + shooter.width // 2 - 2, shooter.y + shooter.height, 5, RED, owner="enemy")
            )

        # UFO
        if self.ufo is None:
            self.ufo_timer -= 1
            if self.ufo_timer <= 0:
                self.ufo = UFO()
        else:
            self.ufo.update()
            if not self.ufo.alive:
                self.ufo = None
                self.ufo_timer = random.randint(500, 900)

        self.handle_collisions()

        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.life > 0]

        if not alive_enemies:
            self.next_level()

    def handle_collisions(self):
        # player bullets vs enemies
        for b in self.player_bullets[:]:
            hit_something = False
            for e in self.enemies:
                if e.alive and e.rect.colliderect(b.rect):
                    e.alive = False
                    hit_something = True
                    self.score += e.points
                    self.spawn_explosion(e.x + e.width // 2, e.y + e.height // 2, e.color)
                    break
            if not hit_something and self.ufo and self.ufo.alive and self.ufo.rect.colliderect(b.rect):
                self.ufo.alive = False
                self.score += self.ufo.points
                self.spawn_explosion(self.ufo.x + 25, self.ufo.y + 11, MAGENTA)
                hit_something = True
            if not hit_something:
                for barrier in self.barriers:
                    if barrier.hit(b.rect):
                        hit_something = True
                        break
            if hit_something and b in self.player_bullets:
                self.player_bullets.remove(b)

        # enemy bullets vs player / barriers
        for b in self.enemy_bullets[:]:
            hit_something = False
            for barrier in self.barriers:
                if barrier.hit(b.rect):
                    hit_something = True
                    break
            if not hit_something and self.player.rect.colliderect(b.rect):
                hit_something = True
                self.player_hit()
            if hit_something and b in self.enemy_bullets:
                self.enemy_bullets.remove(b)

    def player_hit(self):
        self.spawn_explosion(self.player.x + self.player.width // 2, self.player.y + self.player.height // 2, GREEN)
        self.player.lives -= 1
        if self.player.lives <= 0:
            self.trigger_gameover("YOU WERE DEFEATED")
        else:
            self.player.x = WIDTH // 2 - self.player.width // 2

    def spawn_explosion(self, x, y, color):
        for _ in range(18):
            self.particles.append(Particle(x, y, color))

    def next_level(self):
        self.level += 1
        self.player_bullets.clear()
        self.enemy_bullets.clear()
        self.spawn_enemies()
        self.spawn_barriers()

    def trigger_gameover(self, message):
        if self.state == "playing":
            self.state = "gameover"
            self.message = message
            if self.score > self.high_score:
                self.high_score = self.score
                save_high_score(self.high_score)

    
    def draw(self, surf):
        surf.fill(BLACK)
        for s in stars:
            s.draw(surf)

        for barrier in self.barriers:
            barrier.draw(surf)

        for e in self.enemies:
            if e.alive:
                e.draw(surf)

        if self.ufo and self.ufo.alive:
            self.ufo.draw(surf)

        for b in self.player_bullets:
            b.draw(surf)
        for b in self.enemy_bullets:
            b.draw(surf)

        for p in self.particles:
            p.draw(surf)

        if self.player.lives > 0:
            self.player.draw(surf)

        self.draw_hud(surf)

        if self.state == "paused":
            self.draw_center_text(surf, "PAUSED", "Press P to resume")
        elif self.state == "gameover":
            self.draw_center_text(surf, "GAME OVER", self.message + "   |   Press ENTER to restart")
        elif self.state == "win_forever":
            pass

    def draw_hud(self, surf):
        score_text = FONT_SMALL.render(f"SCORE: {self.score}", True, WHITE)
        high_text = FONT_SMALL.render(f"HIGH SCORE: {self.high_score}", True, YELLOW)
        level_text = FONT_SMALL.render(f"LEVEL: {self.level}", True, CYAN)
        surf.blit(score_text, (16, 14))
        surf.blit(high_text, (WIDTH // 2 - high_text.get_width() // 2, 14))
        surf.blit(level_text, (WIDTH - level_text.get_width() - 16, 14))

        for i in range(self.player.lives):
            lx = 16 + i * 30
            ly = HEIGHT - 30
            pygame.draw.polygon(
                surf, GREEN,
                [(lx + 10, ly), (lx, ly + 18), (lx + 20, ly + 18)]
            )

    def draw_center_text(self, surf, title, subtitle):
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        surf.blit(overlay, (0, 0))
        title_surf = FONT_BIG.render(title, True, RED if "OVER" in title else YELLOW)
        sub_surf = FONT_SMALL.render(subtitle, True, WHITE)
        surf.blit(title_surf, (WIDTH // 2 - title_surf.get_width() // 2, HEIGHT // 2 - 60))
        surf.blit(sub_surf, (WIDTH // 2 - sub_surf.get_width() // 2, HEIGHT // 2 + 10))



import os

HIGH_SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "high_score.txt")


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(value):
    try:
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(value))
    except OSError:
        pass


def title_screen():
    waiting = True
    while waiting:
        screen.fill(BLACK)
        for s in stars:
            s.update()
            s.draw(screen)

        title = FONT_BIG.render("SPACE INVADERS", True, GREEN)
        prompt = FONT_MED.render("Press ENTER to start", True, WHITE)
        controls = FONT_SMALL.render("Move: LEFT/RIGHT or A/D    Shoot: SPACE    Pause: P", True, GRAY)
        hs = FONT_SMALL.render(f"High Score: {load_high_score()}", True, YELLOW)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 140))
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(controls, (WIDTH // 2 - controls.get_width() // 2, HEIGHT // 2 + 20))
        screen.blit(hs, (WIDTH // 2 - hs.get_width() // 2, HEIGHT // 2 + 60))

        # small preview enemy row
        preview_colors = ENEMY_ROW_COLORS
        for i, c in enumerate(preview_colors):
            pygame.draw.rect(screen, c, (WIDTH // 2 - 140 + i * 60, HEIGHT // 2 + 110, 30, 20))

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()



def main():
    title_screen()
    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE and game.state == "playing":
                    game.player.shoot(game.player_bullets)
                if event.key == pygame.K_p and game.state in ("playing", "paused"):
                    game.state = "paused" if game.state == "playing" else "playing"
                if event.key == pygame.K_RETURN and game.state == "gameover":
                    game.reset(full=True)

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()