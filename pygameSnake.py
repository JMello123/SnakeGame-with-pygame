import pygame
import os
from random import randrange
import time

_image_library= {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        '''os.sep pega o separador de caminho padrão do SO.
        Nesse caso ele é usado para substituir a '/' ou a '\\'
        pelo separador padrao do SO, no caso do windows é o \\ mesmo
        '''
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

#screen.blit(get_image('ballSprite.png'),(XY[0],XY[1],10,10))

pygame.init()

largura = 640
altura = 420

screen = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Pygame teste') # nome do programa na janela
clock = pygame.time.Clock()

def salvando_recorde(Pontuacao, Recorde_atual):
    # verificando se a pontução atingida ultrapassou o recorde
    if str(Pontuacao) > str(Recorde_atual):
        txt_recorde = open("recorde.txt", "w", encoding="UTF-8")
        Recorde_atual = txt_recorde.write(str(Pontuacao))
        txt_recorde.close()

def texto (msg, cor, tam, x, y, Fonte=None):
    font = pygame.font.SysFont(Fonte, 25)
    texto1 = font.render(msg, True, cor)
    screen.blit(texto1, [x, y])

def desenha_ball(BallXY, BallInicio):
    pygame.draw.rect(screen,(255,255,255), pygame.Rect(BallInicio[0],BallInicio[1],10,10))
    for XY in BallXY[:-1]:
        pygame.draw.rect(screen,(155,155,155), pygame.Rect(XY[0],XY[1],10,10))
    
def desenha_maca(Maca_x, Maca_y):
        pygame.draw.rect(screen,(255,0,0), pygame.Rect(Maca_x,Maca_y,10,10))

def desenha_cubo(x, y, is_Purple):
        if is_Purple: 
            color = (155,155,155)
        else: 
            color = (0,255,0)
        pygame.draw.rect(screen, color, pygame.Rect(x,y,60,60))


def jogo():
    #variáveis de controle
    exit = False
    fim_de_jogo = False
    is_purple = True
    pontuacao = 0
    sair_pelo_menu = False

    #variáveis do bola
    ball_x = randrange(0,(largura - 10),10)
    ball_y = randrange(0,(altura - 10),10)
    velocidade_x = 0
    velocidade_y = 0
    ballXY = []
    comprimento_ball = 3

    #variáveis da maca
    maca_x = randrange(0,(largura - 10),10)
    maca_y = randrange(0,(altura - 50),10)

    #variávais do cubo
    x = largura/2 #posição x inical do cubo
    y = altura/2 #posição y inical do cubo
    sentido = 0 #direção do cubo 1: direita / 0:esquerda 

    recorde = ''
    if os.path.isfile("recorde.txt"):
        txt_recorde = open("recorde.txt", "r", encoding ="UTF-8")
        recorde = txt_recorde.read()
    else:
        f = open("recorde.txt", 'w')
        recorde = "0"
        f.write(recorde)
        f.close
    
    
    while not exit:
        #print(recorde, pontuacao)
 
        #loop do menu principal
        while sair_pelo_menu == False:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    exit = True
                    sair_pelo_menu = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse_x = pygame.mouse.get_pos()[0]
                    pos_mouse_y = pygame.mouse.get_pos()[1]
                    if pos_mouse_x > 160 and pos_mouse_x < 580 and pos_mouse_y > 210 and pos_mouse_y < 260:
                        sair_pelo_menu = True
                    if pos_mouse_x > 160 and pos_mouse_x < 580 and pos_mouse_y > 280 and pos_mouse_y < 330:
                        pass
                    if pos_mouse_x > 160 and pos_mouse_x < 580 and pos_mouse_y > 350 and pos_mouse_y < 400:
                        exit = True
                        sair_pelo_menu = True
                        fim_de_jogo = False
                        pygame.quit()

            print(type(pontuacao), type(recorde), recorde)
            if sair_pelo_menu == False:
                screen.fill((0,0,0))
                texto("SNAKE GAME", (255,0,0), 150, 250, altura/5,'Arial')
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(160, 210, 320, 50))
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(160, 280, 320, 50))
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(160, 350, 320, 50))
                texto("Iniciar", (0,0,0), 100, 180, 220)
                texto("Opções", (0,0,0), 100, 180, 290)
                texto("Sair", (0,0,0), 100, 180, 360)
                pygame.display.update()


        #loop iniciado quando o jogador perde
        while fim_de_jogo:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    salvando_recorde(pontuacao,recorde)
                    exit = True
                    fim_de_jogo = False
                    pygame.quit()
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_s]:
                    salvando_recorde(pontuacao,recorde)
                    exit = True
                    fim_de_jogo = False
                    pygame.quit()
                if pressed[pygame.K_c]:
                    salvando_recorde(pontuacao,recorde)
                    jogo()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_mouse_x = pygame.mouse.get_pos()[0]
                    pos_mouse_y = pygame.mouse.get_pos()[1]
                    if pos_mouse_x > 185 and pos_mouse_x < 310 and pos_mouse_y > 280 and pos_mouse_y < 305:
                        salvando_recorde(pontuacao,recorde)
                        jogo()
                    elif pos_mouse_x > 370 and pos_mouse_x < 425 and pos_mouse_y > 280 and pos_mouse_y < 305:
                        salvando_recorde(pontuacao,recorde)
                        exit = True
                        fim_de_jogo = False
                        pygame.quit()

            print(type(pontuacao), type(recorde), recorde)

            if fim_de_jogo:
                screen.fill((0,0,0))
                if str(pontuacao) > recorde:
                    texto("NOVO RECORDE!", (255,0,0),100, 370, altura/2+30)
                texto("FIM DE JOGO", (255,0,0),100, 270, altura/3-30)
                texto("Sua pontuação foi: " + str(pontuacao), (255,255,255), 25, 235, altura/2)
                texto("O recorde é: "+ str(recorde), (255,255,255), 25, 235, altura/2+30)
        
            
            pygame.draw.rect(screen, (255,255,255), (185,280, 125,25))
            texto("Continuar(C)",(0,0,0), 25, 193 , 280)
            
            pygame.draw.rect(screen, (255,255,255), (370,280,75,25))
            texto("Sair(S)", (0,0,0),25, 380, 280)
            pygame.display.update()

            #print("fim de jogo = " + str(fim_de_jogo), "exit = " + str(exit))
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_purple = not is_purple


        #movimento para cubo
        if x < 580 and sentido == 0:
            x += 10
        else:
            sentido = 1
        
        if sentido == 1 and x > 0:
            x -= 10
        else:
            sentido = 0

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] and velocidade_y != 10 or pressed[pygame.K_UP] and velocidade_y != 10: 
            velocidade_x = 0
            velocidade_y = -10
            y -= 3
        if pressed[pygame.K_s] and velocidade_y != -10 or pressed[pygame.K_DOWN] and velocidade_y != -10: 
            velocidade_x = 0
            velocidade_y = 10
            y += 3      
        if pressed[pygame.K_a] and velocidade_x != 10 or pressed[pygame.K_LEFT] and velocidade_x != 10: 
            velocidade_x = -10
            velocidade_y = 0
            x -= 6
        if pressed[pygame.K_d] and velocidade_x != -10 or pressed[pygame.K_RIGHT] and velocidade_x != -10: 
            velocidade_x = 10
            velocidade_y = 0
            x += 6
        if pressed[pygame.K_r]:
            ball_x = largura/2
            ball_y = largura/2
            fim_de_jogo = True

        ball_x += velocidade_x
        ball_y += velocidade_y

        #fazendo a bola atravesar a tela
        if ball_x >= largura:
            ball_x = 0
        if ball_x < 0:
            ball_x = largura-10 
        if ball_y >= altura-40:
            ball_y = 0
        if ball_y < 0:
            ball_y = altura-50
        #fazendo a bola parar ao colidir com a borda da tela
        # if ball_x > largura-20:
        #     fim_de_jogo = True
        # if ball_x <= 0:
        #     fim_de_jogo = True
        # if ball_y > altura-20:
        #     fim_de_jogo = True
        # if ball_y <= 0:
        #     fim_de_jogo = True

        #colisão da bola com a maça
        if ball_x == maca_x and ball_y == maca_y:
            maca_x = randrange(0,(largura - 10),10)
            maca_y = randrange(0,(altura - 50),10)
            comprimento_ball += 1
            pontuacao += 1
        

        if not exit: #impede que o loop pinte mais um frame quando o jogo for fechado
            print(type(pontuacao), type(recorde))

            #pinta tela de preto
            screen.fill ((0,0,0))

            # adiciona a posição mais recente da bola na lista ballXY 
            ballInicio = [ball_x, ball_y]
            ballXY.append(ballInicio)

            # excluindo a posição mais antiga a cada frame de acordo com o comprimento da bola
            if len(ballXY) > comprimento_ball:
                del ballXY[0]
            
            # verifica se a bolainicio tocou no resto da cobra 
            if any(Bloco == ballInicio for Bloco in ballXY[:-3]):
                fim_de_jogo = True

            # desenha os objetos na tela
            pygame.draw.rect(screen,(255,255,255), pygame.Rect(0,altura-40,largura,40))
            texto("Pontuação: " + str(pontuacao), (0,0,0),25, 0, altura-30)
            desenha_ball(ballXY, ballInicio)
            desenha_maca(maca_x, maca_y)
            desenha_cubo(x, y, is_purple)

            #print("fim de jogo = " + str(fim_de_jogo), "exit = " + str(exit))

            pygame.display.flip()
            clock.tick(30)  
            time.sleep(0.1)

# chama a função jogo() quando o arquivo é executado
jogo() 