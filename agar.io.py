
import pygame, sys, random, math

def random_color():
    return (random.randint(50 ,255) ,random.randint(50 ,255) ,random.randint(50 ,255) ,190)

def distance(object1, object2):
    x = (object1.rect.centerx) - (object2.rect.centerx)
    y = (object1.rect.centery) - (object2.rect.centery)
    dist = math.sqrt( x**2 + y**2)
    return dist

def draw_grid():
    # Horizontal
    for y in range(0 ,800 ,50):
        pygame.draw.line(screen, (200 ,200 ,200 ,50), (0, y), (1400, y))
    # Vertical
    for x in range(0 ,1400 ,50):
        pygame.draw.line(screen, (200 ,200 ,200 ,50), (x, 0), (x, 800))


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()
        self.radius = 8
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, "red", (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = (random.randint(3, 1397) ,random.randint(3 ,797)))

    def relocate(self):
        self.rect.center = (random.randint(3, 797) ,random.randint(3 ,597))



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.radius = random.randint(10 ,40)
        self.test = 20
        self.speed = self.test / self.radius
        self.deltax = random.choice([-2 ,-1 ,1 ,2])
        self.deltay = random.choice([-2, -1, 1, 2])
        self.color = random_color()
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect \
            (center = (random.randint(self.radius, 1400 -self.radius) ,random.randint(self.radius ,800 -self.radius)))

    def move(self):
        if self.rect.centerx <= -200 or self.rect.centerx >= 1600:
            self.deltax *= -1
            pygame.draw.circle(self.image, random_color(), (self.radius, self.radius), self.radius)
        if self.rect.centery <= -200 or self.rect.centery >= 1000:
            self.deltay *= -1
            pygame.draw.circle(self.image, random_color(), (self.radius, self.radius), self.radius)

        self.rect.centerx += self.deltax
        self.rect.centery += self.deltay

    def collision(self, object):
        return distance(self, object) < ((self.radius + object.radius ) *.8)

    def grow(self, object):
        x = self.rect.centerx
        y = self.rect.centery
        self.radius = (self.radius + object.radius)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2) ,pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius, 0)
        self.rect = self.image.get_rect(center = (x ,y))
        self.test += 10
        self.speed = self.test / self.radius


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.radius = 25
        self.test = 20
        self.speed = self.test / self.radius
        self.color = (255 ,255 ,255 ,255)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = (40 ,40))

    def say_hello(self):
        print("Hello")

    # Move the sprite based on mouse
    def move(self, mx, my):
        print("\nMouse Location: ", (mx ,my))
        ex = self.rect.centerx
        ey = self.rect.centery
        x = (mx ) -ex
        y = (my ) -ey

        hyp = math.sqrt( x** 2 + y**2)
        if hyp==0:
            hyp =0.00000001
        deltaX = (.9 *x ) /hyp
        deltaY = (.9 *y ) /hyp

        print("Player Location:" ,self.rect.center)
        print("Delta Values: ",(deltaX, deltaY))
        self.rect.centerx += deltaX
        self.rect.centery += deltaY

    def collision(self, object):
        return distance(self, object) < ((self.radius + object.radius ) *.8)

    def grow(self, object):
        x = self.rect.centerx
        y = self.rect.centery
        self.radius = (self.radius + object.radius)
        self.image = pygame.Surface((self.radius * 2, self.radius * 2) ,pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius, 0)
        self.rect = self.image.get_rect(center = (x ,y))
        self.test += 10
        self.speed = self.test / self.radius


# Initialize Pygame and give access to all the methods in the package
pygame.init()

# Set up the screen dimensions
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Agario")

# Create clock to later control frame rate
clock = pygame.time.Clock()

enemies = pygame.sprite.Group()
for count in range(10):
    enemies.add(Enemy())

player = Player()

food = pygame.sprite.Group()
for f in range(10):
    food.add(Food())

entities = pygame.sprite.Group()
entities.add(enemies)
entities.add(player)


objects = pygame.sprite.Group()
objects.add(food)
objects.add(entities)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): # pygame.event.get()
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0 ,0 ,0))
    draw_grid()

    mx ,my = pygame.mouse.get_pos()
    player.move(mx, my)
    player.say_hello()

    for enemy in enemies:
        enemy.move()

    for object in entities:
        for other in objects:
            if object != other and object.collision(other):
                if object.radius > other.radius:
                    object.grow(other)
                    if type(other) == Food:
                        other.relocate()
                    else:
                        other.kill()
                else:
                    other.grow(object)
                    object.kill()

    objects.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()
