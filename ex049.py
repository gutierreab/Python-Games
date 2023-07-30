import pygame
from pygame.locals import *
from random import randint
from time import sleep
from pygame import mixer

pygame.init()
mixer.init()

tela_largura = 700
tela_altura = 500
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('JoKenPo!')

vermelho = (255, 0, 0)
preto = (0, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)

jpgPedra = pygame.image.load('pedra.jpg').convert_alpha()
jpg_pedra = pygame.transform.scale(jpgPedra, (300, 150))

jpgPapel = pygame.image.load('papel.jpg').convert_alpha()
jpg_papel = pygame.transform.scale(jpgPapel, (300, 150))

jpgTesoura = pygame.image.load('tesoura.jpg').convert_alpha()
jpg_tesoura = pygame.transform.scale(jpgTesoura, (300, 150))

mixer.music.load('jokenpo.mp3')
mixer.music.play(-1)


def Text_Objects(text, font):
    textSurface = font.render(text, True, preto)
    return textSurface, textSurface.get_rect()


def button_pedra(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(tela, preto, (x, y, w, h + 5))
        if click[0] == 1 and action is not None:
            if action == 'JO':
                pedra_result()

        tela.blit(jpg_pedra, (x, y, w, h))


def button_papel(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(tela, preto, (x, y, w, h+5))
        if click[0] == 1 and action != None:
            if action == 'KEN':
                papel_result()

    tela.blit(jpg_papel, (x, y, w, h))


def button_tesoura(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(tela, preto, (x, y, w, h + 5))
        if click[0] == 1 and action is not None:
            if action == 'PO':
                tesoura_result()

    tela.blit(jpg_tesoura, (x, y, w, h))


def tela_escolha():
    sair = False

    while not sair:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)

        button_pedra(200, 5, 300, 150, 'JO')
        button_papel(200, 175, 300, 150, 'KEN')
        button_papel(200, 340, 300, 150, 'PO')
        volt_button('Voltar', 30, 420, 100, 50, (0, 0, 200), azul, 'Voltar')

        pygame.display.update()

    pygame.quit()
    quit()


def pedra_result():
    sistema = randint(0, 2)

    sair = False

    while not sair:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Você', True, preto)
        tela.blit(palavra, (40, 60))

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Bot', True, preto)
        tela.blit(palavra, (40, 420))

        tela.blit(jpg_pedra, (200, 5))
        if sistema == 0:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('EMPATE', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(jpg_pedra, (200, 340))

        elif sistema == 1:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('PERDEU', True, vermelho)
            tela.blit(palavra, (300, 250))
            tela.blit(jpg_papel, (200, 340))

        elif sistema == 2:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('VENCEU', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(jpg_tesoura, (200, 340))

        pygame.display.update()
        sleep(2)
        tela_escolha()


def papel_result():
    sistema = randint(0, 2)

    sair = False

    while not sair:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Você:', True, preto)
        tela.blit(palavra, (40, 60))

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Bot:', True, preto)
        tela.blit(palavra, (40, 420))

        tela.blit(jpg_papel, (200, 5))

    if sistema == 0:
        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('VENCEU', True, preto)
        tela.blit(palavra, (300, 250))
        tela.blit(jpg_pedra, (200, 340))

    elif sistema == 1:
        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('EMPATE', True, preto)
        tela.blit(palavra, (300, 250))
        tela.blit(jpg_papel, (200, 340))

    elif sistema == 2:
        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('PERDEU', True, vermelho)
        tela.blit(palavra, (300, 250))
        tela.blit(jpg_tesoura, (200, 340))

    pygame.display.update()
    sleep(2)
    tela_escolha()


def tesoura_result():
    sistema = randint(0, 2)

    sair = False

    while not sair:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Você:', True, preto)
        tela.blit(palavra, (40, 60))

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Bot:', True, preto)
        tela.blit(palavra, (40, 420))

        tela.blit(jpg_tesoura, (200, 5))
        if sistema == 0:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('PERDEU', True, vermelho)
            tela.blit(palavra, (300, 250))
            tela.blit(jpg_pedra, (200, 340))

        elif sistema == 1:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('VENCEU', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(jpg_papel, (200, 340))

        elif sistema == 2:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('EMPATE', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(jpg_tesoura, (200, 340))

        pygame.display.update()
        sleep(2)
        tela_escolha()


def volt_button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(tela, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == 'Voltar':
                tela_inicio()

    else:
        pygame.draw.rect(tela, ic, (x, y, w, h))

    texto = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = Text_Objects(msg, texto)
    TextRect.center = (x + (w/2), (y + (h/2)))
    tela.blit(TextSurf, TextRect)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(tela, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == 'Jogar':
                tela_escolha()
            elif action == 'Sair':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(tela, ic, (x, y, w, h))

    texto = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, text_rect = Text_Objects(msg, texto)
    text_rect.center = (x + (w / 2), (y + h / 2))
    tela.blit(TextSurf, text_rect)


def tela_inicio():
    sair = False

    while not sair:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)

        large_text = pygame.font.Font('freesansbold.ttf', 55)
        text_surf, textrect = Text_Objects('JO KEN PO!', large_text)
        textrect.center = ((tela_largura / 2), (tela_altura / 2))
        tela.blit(text_surf, textrect)

        button('Jogar', 100, 400, 100, 50, (0, 200, 0), verde, 'Jogar')
        button('Sair', 500, 400, 100, 50, (200, 0, 0), vermelho, 'Sair')

        pygame.display.update()


tela_inicio()
pygame.quit()
quit()
