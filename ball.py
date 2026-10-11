import pygame
import threading
import random
import time


def create_ball(num_ball):
    print(f"ball {num_ball} created")
    num_jumps = random.randint(1, 10)
    for i in range(num_jumps):
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        x = random.randint(30, 770)
        y = random.randint(30, 570)
        pygame.draw.circle(screen, color, (x, y), 30)
        pygame.display.flip()



        time.sleep(2)

        pygame.draw.circle(screen, 0, (x, y), 30)
        pygame.display.flip()

    print(f"ball {num_ball} removed, jumped {num_jumps} times")


num_balls = int(input("enter number of balls to draw "))
print(num_balls)
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Circle")

screen.fill(0)

for i in range(1, num_balls+1):
    thread = threading.Thread(target=create_ball, args=(i,), daemon=True)
    thread.start()
    time.sleep(1)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()




pygame.quit()