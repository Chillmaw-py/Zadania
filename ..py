import pygame
import numpy as np

width, height = (1280, 720)
win = pygame.display.set_mode((width, height))


class Shape():
    def __init__(self) -> None:
        self.points = []
        self.adding_points = True
        self.edges = []

    def add_point(self, mouse_x: int, mouse_y: int) -> None:
        self.points.append((mouse_x, mouse_y))

    # Wczytywanie narysowanej figury (powstałych krawędzi)
    def establish_shape(self) -> None:
        for point1, point2 in zip(self.points[:-1], self.points[1:]):
            self.edges.append((point1, point2))
        self.edges.append((self.points[-1], self.points[0]))

        return

    # Wyznaczanie punktów przecięcia
    def intersections(self, yr: int) -> list:
        l = []
        for (x1, y1), (x2, y2) in self.edges:
            if (yr >= y1 and yr <= y2) or (yr <= y1 and yr >= y2):
                l.append((x1 + ((yr-y1)/(y2 - y1))*(x2 - x1), yr))

        return l

    # Sprawdzanie czy punkt jest wewnątrz figury używając Ray-Castingu
    def is_inside(self, xr: int, yr: int) -> bool:
        r_crosses = 0
        l_crosses = 0
        for (x1, y1), (x2, y2) in self.edges:
            if (yr >= y1 and yr <= y2) or (yr <= y1 and yr >= y2):
                if xr < x1 + ((yr-y1)/(y2 - y1))*(x2 - x1):
                    r_crosses += 1
                else:
                    l_crosses += 1

        return r_crosses % 2 == 1 or l_crosses == 1

    def render(self, win: pygame.display, mouse_x: int, mouse_y: int) -> None:
        if self.adding_points:
            pygame.draw.lines(win, (255, 255, 255), True,
                              self.points + [(mouse_x, mouse_y)])
        else:
            pygame.draw.lines(win, (255, 255, 255), True, self.points)

        for point in self.points:
            pygame.draw.circle(win, (200, 200, 200), point, 4)

        return


class MonteCarlo():
    def __init__(self, n: int) -> None:
        self.n = n

        self.random_points = []
        self.points = []
        self.edges = []

    # Losowanie n losowych punktów
    def roll_points(self) -> np.array:
        self.random_points = np.stack((np.random.uniform(
            0, width, self.n), np.random.uniform(0, height, self.n)), axis=-1)
        return self.random_points

    # Obliczanie pola figury
    def calculate_area(self, shape: Shape) -> float:
        count = 0
        for xr, yr in self.random_points:
            if shape.is_inside(xr, yr):
                count += 1

        return count/self.n

    def render(self, win: pygame.display):
        for point in self.random_points[:100]:
            pygame.draw.circle(win, (150, 50, 25), point, 2)


# Punkt testowy
class Point():
    def __init__(self, x: int, y: int, shape: Shape) -> None:
        self.x = x
        self.y = y
        self.is_inside = shape.is_inside(x, y)
        self.intersections = shape.intersections(y)

    def render(self, win: pygame.display) -> None:
        if self.is_inside:
            pygame.draw.circle(win, (20, 255, 20), (self.x, self.y), 4)
        else:
            pygame.draw.circle(win, (255, 20, 20), (self.x, self.y), 4)

        for point in self.intersections:
            pygame.draw.circle(win, (255, 165, 0), point, 3)

        pygame.draw.line(win, (0, 0, 255), (0, self.y), (width, self.y))


print("Controls: ")
print("--Use left mouse button to add points until you are satisfied with the shape or to add test points")
print("--Use right mouse button to confirm your shape")
print("--Press 'r' to calculate the area using Monte Carlo method")
print("--Press 'e' to delete all test points")
print("Program shows first 100 points from the default 100_000 random ones")
print("Ressult is a fraction of the whole screen")

shape = Shape()
monte = MonteCarlo(100_000)

test_points = []
run = True

while run:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Kontrolki
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and shape.adding_points:
                shape.add_point(mouse_x, mouse_y)
                print(mouse_x, mouse_y)
            elif pygame.mouse.get_pressed()[0] and not shape.adding_points:
                test_points.append(Point(mouse_x, mouse_y, shape))
            else:
                shape.adding_points = False
                shape.establish_shape()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                monte.roll_points()
                print(monte.calculate_area(shape))
            elif event.key == pygame.K_e:
                test_points.clear()

    # Renderowanie
    win.fill((50, 50, 50))
    for point in test_points:
        point.render(win)
    if shape.points:
        shape.render(win, mouse_x, mouse_y)
    if not shape.adding_points:
        monte.render(win)

    pygame.display.update()