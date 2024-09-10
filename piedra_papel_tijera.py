import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 700
alto_pantalla = 600
screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Piedra, Papel o Tijera")

# Cargar imágenes
piedra_img = pygame.image.load("img/piedra.png")
papel_img = pygame.image.load("img/papel.png")
tijeras_img = pygame.image.load("img/tijeras.png")

# Escalar imágenes
img_ancho = 150
img_alto = 150
piedra_img = pygame.transform.scale(piedra_img, (img_ancho, img_alto))
papel_img = pygame.transform.scale(papel_img, (img_ancho, img_alto))
tijeras_img = pygame.transform.scale(tijeras_img, (img_ancho, img_alto))

# Definir colores suaves
NEGRO = (10, 10, 10)
BLANCO = (240, 240, 240)
ROJO = (255, 85, 85)
AZUL = (85, 150, 255)
GRIS = (50, 50, 50)

# Establecer la fuente y el tamaño
font = pygame.font.Font(None, 48)

# Inicializar variables de juego
puntos_jugador = 0
puntos_ordenador = 0
rondas_jugadas = 0

# Función para mostrar la puntuación
def mostrar_puntos():
    puntos_text = font.render(f"Jugador: {puntos_jugador}  |  Computadora: {puntos_ordenador}", True, BLANCO)
    screen.blit(puntos_text, (ancho_pantalla // 2 - puntos_text.get_width() // 2, 20))

# Función para mostrar las opciones de imagen del jugador
def mostrar_opciones_usuario():
    screen.blit(piedra_img, (100, 400))
    screen.blit(papel_img, (300, 400))
    screen.blit(tijeras_img, (500, 400))
    instruccion_text = font.render("Elige tu opción:", True, BLANCO)
    screen.blit(instruccion_text, (ancho_pantalla // 2 - instruccion_text.get_width() // 2, 350))

# Función para mostrar la elección del jugador y la computadora en el centro
def mostrar_elecciones(opcion_jugador, opcion_ordenador):
    screen.fill(GRIS)
    # Mostrar elección del jugador en el centro
    titulo_jugador = font.render("Jugador:", True, AZUL)
    screen.blit(titulo_jugador, (ancho_pantalla // 2 - 250, 150))
    screen.blit(opcion_jugador, (ancho_pantalla // 2 - 250, 200))

    # Mostrar elección de la computadora después de 1 segundo
    pygame.display.update()
    pygame.time.delay(1000)

    titulo_ordenador = font.render("Computadora:", True, ROJO)
    screen.blit(titulo_ordenador, (ancho_pantalla // 2 + 100, 150))
    screen.blit(opcion_ordenador, (ancho_pantalla // 2 + 100, 200))

    # Actualizar pantalla y pausar brevemente
    pygame.display.update()
    pygame.time.delay(1000)

# Función para determinar el resultado de la ronda
def determinar_resultado(opcion_jugador, opcion_ordenador):
    global puntos_jugador, puntos_ordenador
    if opcion_jugador == opcion_ordenador:
        return "Empate"
    elif (
        (opcion_jugador == piedra_img and opcion_ordenador == tijeras_img) or
        (opcion_jugador == papel_img and opcion_ordenador == piedra_img) or
        (opcion_jugador == tijeras_img and opcion_ordenador == papel_img)
    ):
        puntos_jugador += 1
        return "¡Ganaste esta ronda!"
    else:
        puntos_ordenador += 1
        return "La computadora gana esta ronda"

# Función principal del juego
def main():
    global puntos_jugador, puntos_ordenador, rondas_jugadas
    clock = pygame.time.Clock()
    running = True
    resultado_text = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and rondas_jugadas < 5:
                # Generar elección aleatoria para la computadora
                opcion_ordenador = random.choice([piedra_img, papel_img, tijeras_img])
                # Determinar la imagen clicada por el jugador
                x, y = event.pos
                if 100 <= x <= 250 and 400 <= y <= 550:
                    opcion_jugador = piedra_img
                elif 300 <= x <= 450 and 400 <= y <= 550:
                    opcion_jugador = papel_img
                elif 500 <= x <= 650 and 400 <= y <= 550:
                    opcion_jugador = tijeras_img
                else:
                    continue

                rondas_jugadas += 1

                # Mostrar las elecciones de ambos jugadores
                mostrar_elecciones(opcion_jugador, opcion_ordenador)

                # Determinar el resultado de la ronda
                resultado_text = determinar_resultado(opcion_jugador, opcion_ordenador)

        # Establecer fondo y mostrar puntos
        screen.fill(NEGRO)
        mostrar_puntos()
        mostrar_opciones_usuario()

        # Mostrar el resultado de la ronda
        if resultado_text:
            resultado_display = font.render(resultado_text, True, BLANCO)
            screen.blit(resultado_display, (ancho_pantalla // 2 - resultado_display.get_width() // 2, 100))

        pygame.display.update()
        clock.tick(30)

    # Pantalla final
    screen.fill(NEGRO)
    texto_final = "¡Jugador gana!" if puntos_jugador > puntos_ordenador else "¡Computadora gana!"
    final_display = font.render(texto_final, True, BLANCO)
    screen.blit(final_display, (ancho_pantalla // 2 - final_display.get_width() // 2, alto_pantalla // 2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
