import pygame
import multiprocessing
import random
import time

def check_collision():
    pass


    # print(f"ball {num_ball} removed, jumped {num_jumps} times")


def create_ball(num_ball, q):
    print(f"ball {num_ball} created")
    # num_jumps = random.randint(1, 10)
    # for i in range(num_jumps):
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

    x = random.randint(30, 770)
    y = random.randint(30, 570)
    pos = (x, y)
    q.put((color, pos))




if __name__ == '__main__':
    q = multiprocessing.Queue()
    num_balls = int(input("enter number of balls to draw "))
    print(num_balls)
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Circle")

    screen.fill(0)

    for i in range(1, num_balls+1):
        process  = multiprocessing.Process(target=create_ball, args=(i,q,))
        process .start()

        color, pos = q.get()
        pygame.draw.circle(screen, color, pos, 30)
        pygame.display.flip()
        time.sleep(1)



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip()




    pygame.quit()