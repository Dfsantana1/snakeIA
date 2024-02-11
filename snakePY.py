import turtle
import time
import random

delay = 0.1
score = 0

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")

# Crear la cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Crear la comida de la serpiente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Funciones
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Teclado
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Bucle principal del juego
while True:
    wn.update()

    # Verificar colisión con el borde
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"

        # Esconder los segmentos
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Limpiar la lista de segmentos
        segments.clear()

        # Resetear el marcador
        score = 0

    # Verificar colisión con la comida
    if head.distance(food) < 20:
        # Mover la comida a una posición aleatoria
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x,y)

        # Añadir un segmento a la serpiente
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Aumentar el marcador
        score += 10

    # Mover los segmentos del cuerpo
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # Verificar colisión con el cuerpo de la serpiente
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Esconder los segmentos
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Limpiar la lista de segmentos
            segments.clear()

            # Resetear el marcador
            score = 0

    time.sleep(delay)

wn.mainloop()
