#Video Funcionamiento: https://youtu.be/8FVfoOUIejk 
#Nicolle Gordillo
#Joaquin Campos
#Fisica 3 Parcial 3 Problema 5

import turtle
import math
import matplotlib.pyplot as plt
import random

def calcular_area(diametro):
    radio = diametro / 2
    area = math.pi * (radio ** 2)
    return area

def calcular_resistencia(longitud, material, area): 
    resistividad = {#Según Young y Freedman (ohms*metro)
        "oro": 2.44e-8,
        "plata": 1.47e-8,
        "cobre": 1.72e-8,
        "aluminio": 2.75e-8,
        "grafito": 5.00e-6
    }
    n = {
        "oro": 5.90683e28,
        "plata": 5.86189e28,
        "cobre": 8.497e28,
        "aluminio": 6.02155e28,
        "grafito": 1.1331e29
    }
    
    resistividad_material = resistividad.get(material.lower())
    densidad_particulas_material = n.get(material.lower())
    
    resistencia = (resistividad_material * longitud) / area
    return resistencia, densidad_particulas_material

# Función para calcular la corriente
def calcular_corriente(voltaje, resistencia):
    corriente = voltaje / resistencia
    return corriente

# Función para calcular la potencia disipada
def calcular_potencia(voltaje, corriente):
    potencia = voltaje * corriente
    return potencia

# Función para calcular la velocidad de arrastre de los electrones
def calcular_velocidad_deriva(corriente, densidad_particulas,area):
    velocidad_deriva = corriente / (densidad_particulas * 1.6e-19*area) 
    return velocidad_deriva

# Función para calcular el tiempo que toma a los electrones atravesar el alambre
def calcular_tiempo(longitud, velocidad_deriva):
    tiempo = longitud / velocidad_deriva
    return tiempo


def awg_a_mm(awg):
    if(awg=="0000"):
        mm=11.684
    elif(awg=="000"):
        mm=10.4
    elif(awg=="00"):
        mm=9.266
    else:
        mm= round(float( 0.127 * 92**((36 - awg) / 39)),3)
    return mm
    

# Función principal
def main():
    desicion1 = int(input("Seleccione una opción del menú: \n1. Simulación de un alambre cilíndrico \n2. Simulación de un electrón de valencia cambiando de átomo \n   hasta llegar al final del cable\n"))
    if desicion1 == 1:
        print("Simulación de un alambre cilíndrico")
        longitud = float(input("Ingrese el largo del alambre (en metros): "))
        dimension = input("¿Cómo quiere ingresar el diametro? 1.mm 2.AWG ")
        diametro = float(input("Ingrese el diámetro del alambre: "))
        if dimension=="1":
            diametro=diametro/1000 #mm a m
        elif dimension=="2":
            diametro= awg_a_mm(diametro)
            print("Eso equivale a ",diametro,"mm")
            diametro=diametro/1000 #mm a m
        else:
            print("Esa opción no es válida")
            return
            
        material = input("Ingrese el material del conductor (oro (n=5.90683e28), plata (n=5.86189e28), cobre (n=8.497e28), aluminio (n=6.02155e28) o grafito (n=1.1331e29)): ")
        voltaje = float(input("Ingrese el voltaje aplicado (en voltios): "))

        area = calcular_area(diametro)  
        resistencia, densidad_particulas = calcular_resistencia(longitud, material, area)
        corriente = calcular_corriente(voltaje, resistencia)
        potencia = calcular_potencia(voltaje, corriente)
        velocidad_deriva = calcular_velocidad_deriva(corriente, densidad_particulas,area)
        tiempo = calcular_tiempo(longitud, velocidad_deriva)

        print(f"Resistencia del alambre: {resistencia:.4f} ohms")
        print(f"Corriente: {corriente:.4f} amperes")
        print(f"Potencia disipada: {potencia:.4f} watts")
        print(f"Velocidad de arrastre de los electrones: {velocidad_deriva:.4f} m/s")
        print(f"Tiempo para atravesar el alambre: {tiempo:.4f} segundos")
        velocidad_arrastre_visual = velocidad_deriva* 1000

        pantalla = turtle.Screen()
        pantalla.title("Representación gráfica de un alambre cilíndrico conectado a una batería")
        pantalla.bgcolor("white")

        # Crea un objeto Turtle
        dibujo = turtle.Turtle()
        dibujo.shape("turtle")
        dibujo.speed(2)  # Puedes ajustar la velocidad según tus preferencias

        dibujo.pensize(2)
        # Dibuja el alambre
        dibujo.penup()
        dibujo.goto(-200, -50)
        dibujo.pendown()
        dibujo.forward(400)
        dibujo.left(90)
        dibujo.forward(60)
        dibujo.left(90)
        dibujo.forward(400)
        dibujo.left(90)
        dibujo.forward(60)
        dibujo.end_fill()

        
        # Dibuja la batería (dos líneas)
        dibujo.penup()
        dibujo.goto(10, 100)
        dibujo.pendown()
        dibujo.color("gray")
        dibujo.forward(20)
        dibujo.right(180)
        dibujo.penup()
        dibujo.goto(-10, 105)
        dibujo.right(180)
        dibujo.pendown()
        dibujo.forward(30)
        
        # Dibuja los cables desde la batería al alambre
        dibujo.penup()
        dibujo.goto(-10, 90)
        dibujo.right(90)
        dibujo.pendown()
        dibujo.forward(250)
        dibujo.left(90)
        dibujo.forward(110)
        dibujo.left(90)
        dibujo.forward(59)
        
        dibujo.penup()
        dibujo.goto(10, 90)
        dibujo.pendown()
        dibujo.forward(250)
        dibujo.right(90)
        dibujo.forward(110)
        dibujo.right(90)
        dibujo.forward(59)

        # Etiquetas para la batería y el voltaje
        dibujo.penup()
        dibujo.goto(-15, 120)
        dibujo.pendown()
        dibujo.color("black")
        dibujo.write(f'{voltaje} V', font=("Arial", 12, "normal"))
        dibujo.hideturtle()
        
        # Crea un objeto Turtle para representar electrones
        electron = turtle.Turtle()
        # Configura la posición inicial de los electrones
        electron.penup()
        electron.goto(190, -35)
        electron.shape("circle")
        electron.color("blue")
        electron.speed(0)  # Establece la velocidad al máximo

        
        electron.pendown()
        
        electron2 = turtle.Turtle()
        # Configura la posición inicial de los electrones
        electron2.penup()
        electron2.goto(0, -35)
        electron2.shape("circle")
        electron2.color("blue")
        electron2.speed(0)  # Establece la velocidad al máximo

        
        electron2.pendown()
        
        electron3 = turtle.Turtle()
        # Configura la posición inicial de los electrones
        electron3.penup()
        electron3.goto(95, -5)
        electron3.shape("circle")
        electron3.color("blue")
        electron3.speed(0)  # Establece la velocidad al máximo

        
        electron3.pendown()
        
        electron4 = turtle.Turtle()
        # Configura la posición inicial de los electrones
        electron4.penup()
        electron4.goto(-95, -5)
        electron4.shape("circle")
        electron4.color("blue")
        electron4.speed(0)  # Establece la velocidad al máximo

        
        electron4.pendown()

        # Simula el movimiento de los electrones
        while True:
            electron.backward(velocidad_arrastre_visual)
            electron2.backward(velocidad_arrastre_visual)
            electron3.backward(velocidad_arrastre_visual)
            electron4.backward(velocidad_arrastre_visual)
            # Revisa si el electrón ha salido del alambre y lo devuelve al inicio
            if electron.xcor() < 0:
                electron.penup()
                electron.goto(190, -35)
                electron.pendown()
            if electron2.xcor() < -190:
                electron2.penup()
                electron2.goto(0, -35)
                electron2.pendown()
            if electron3.xcor() < 0:
                electron3.penup()
                electron3.goto(190, -5)
                electron3.pendown()
            if electron4.xcor() < -190:
                electron4.penup()
                electron4.goto(0, -5)
                electron4.pendown()
        turtle.done()
    elif desicion1 == 2:
                
        # pantalla
        wn = turtle.Screen()
        wn.title("Simulación de Electrón")
        wn.bgcolor("white")
        width, height = 600, 300
        wn.setup(width, height)

        # núcleos de los átomos
        num_atoms = 28
        nuclei = []
        i = 0
        for _ in range(num_atoms):
            nucleus = turtle.Turtle()
            nucleus.shape("circle")
            nucleus.speed(20)
            nucleus.color("red")
            nucleus.penup()
            i = i+1
            # ver de que los nucleos no esten en los bordes
            if i % 2 == 0:
                nucleus.goto(300-(i*20),35)
            else:
                nucleus.goto(300-(i*20),-35)
            nuclei.append(nucleus)

        # Dibuja el rectángulo
        rect = turtle.Turtle()
        rect.speed(20)
        rect.penup()
        rect.goto(-width//2, -height//2)
        rect.pendown()
        rect.forward(width)
        rect.left(90)
        rect.forward(height)
        rect.left(90)
        rect.forward(width)
        rect.left(90)
        rect.forward(height)
        rect.hideturtle()
        rect.speed(10)
        # Electrón
        electron = turtle.Turtle()
        electron.turtlesize(0.5)
        electron.shape("circle")
        electron.color("blue")
        electron.penup()
        electron.goto(width//2 - 10, 0)

        # Función de movimiento aleatorio
        def random_walk():
            while electron.xcor() > -width//2:
                var = electron.xcor()
                var2 = electron.ycor()
                numalea = random.randint(1,5)
                if numalea % 2 == 0:
                    electron.goto(var+20,15)
                else:
                    electron.goto(var-20,-15)
                #Verificar q no c salga del cable
                if var2 >= 35:
                    # Si se acerca a un núcleo, empujar el electrón
                    electron.goto(var, var2-20)
                elif var2 <= -35:
                    electron.goto(var, var2+20)
                # Verificar si el electrón toca algún núcleo
                for nucleus in nuclei:
                    if electron.distance(nucleus) < 20:
                        # Si se acerca a un núcleo, empujar el electrón
                        var = electron.xcor()
                        var2 = electron.ycor()
                        electron.goto(var+50, var2)
                        

                # Verificar los límites de la pantalla
                if electron.ycor() > height//2 - 10 or electron.ycor() < -height//2 + 10:
                    # Si se sale del rectángulo, invertir la dirección en y
                    electron.sety(electron.ycor() - random.choice([-10, 10]))

        # Iniciar la simulación
        while True:
            random_walk()


main()