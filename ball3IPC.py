import multiprocessing
import random
import time
import math






    # print(f"ball {num_ball} removed, jumped {num_jumps} times")

def check_clolision(q, qValid):
    print("in clolision")
    positions = []
    while True:
        color, pos = q.get()
        isColided = False
        if positions and color != 0:
            for p in positions:
                distance = math.dist(pos, p)
                if not distance > 60:
                    # create a new pos
                    isColided = True


        if isColided == False:
            qValid.put((color, pos))
            if not color == 0:
                positions.append(pos)
            else:
                for p in positions:
                    if pos == p:
                        positions.remove(pos)



def create_ball(num_ball, q):
    print(f"ball {num_ball} created")

    # num_jumps = random.randint(1, 10)
    # for i in range(num_jumps):
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

    times = random.randint(1, 10)
    for i in range(times):


        x = random.randint(30, 770)
        y = random.randint(30, 570)
        pos = (x, y)
        q.put((color, pos))
        time.sleep(1)
        q.put((0, pos))


# RADIUS = 30

if __name__ == '__main__':
    import pygame
    q = multiprocessing.Queue()
    qValid = multiprocessing.Queue()
    num_balls = int(input("enter number of balls to draw "))
    print(num_balls)
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Circle")

    screen.fill(0)

    para_adoma = multiprocessing.Process(target=check_clolision, args=(q,qValid,))
    para_adoma.start()

    for i in range(1, num_balls+1):
        process  = multiprocessing.Process(target=create_ball, args=(i,q,))
        process .start()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        color, pos = qValid.get()

        pygame.draw.circle(screen, color, pos, 30)
        pygame.display.flip()





    pygame.quit()