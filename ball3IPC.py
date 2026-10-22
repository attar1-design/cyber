import multiprocessing
import random
import time
import math


def print_proc(print_q):

    #if finished_q.empty():
    while True:
        print(print_q.get())



    # print(f"ball {num_ball} removed, jumped {num_jumps} times")

def check_clolision(q, qValid, print_q):
    print("in clolision")
    positions = {}  # [num_ball] = [pos]
    while True:
        color, pos, num_ball = q.get()

        if color == 0 and num_ball in positions.keys():
            qValid.put((color, positions[num_ball]))
            del positions[num_ball]
            print_q.put(f"there are {int(len(positions) + 1)} balls")
            continue

        if positions:
            isColided = True
            while isColided:
                isColided = False
                for p in positions.values():
                    distance = math.dist(pos, p)
                    if distance < 60:
                        x = random.randint(30, 770)
                        y = random.randint(30, 570)
                        pos = [x, y]
                        isColided = True
                        break
        qValid.put((color, pos))
        if num_ball not in positions.keys():
            print_q.put(f"there are {int(len(positions) + 1)} balls")
        positions[num_ball] = pos

    print_q.put(f"clolision done! ")


def create_ball(num_ball, q, print_q):
    print_q.put(f"ball {num_ball} has been created")
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
        pos = [x, y]
        q.put((color, pos, num_ball))

        time.sleep(1)
        q.put((0, pos, num_ball))


    print_q.put(f"ball {num_ball} has been deleted")
# RADIUS = 30

if __name__ == '__main__':
    import pygame

    print_q = multiprocessing.Queue()
    q = multiprocessing.Queue()
    qValid = multiprocessing.Queue()
    printing_time_buddy = multiprocessing.Process(target=print_proc, args=(print_q,))
    printing_time_buddy.start()
    num_balls = int(input("enter number of balls to draw "))

    # events_dictionary = {}
    # for i in range(1, num_balls + 1):
    #     events_dictionary[i] = multiprocessing.Event()


    para_adoma = multiprocessing.Process(target=check_clolision, args=(q,qValid,print_q,))
    para_adoma.start()

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill(0)
    pygame.display.set_caption("Circle")


    for i in range(1, num_balls+1):
        process = multiprocessing.Process(target=create_ball, args=(i,q,print_q,))
        process.start()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        if not qValid.empty():
            color, pos = qValid.get()
            pygame.draw.circle(screen, color, pos, 30)
            pygame.display.flip()





    pygame.quit()