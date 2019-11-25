import pygame
import time

Ancho=704
Alto=640
centro=[704,640]
VERDE=[0,255,0]
ROJO=[255,0,0]
BLANCO=[255,255,255]
NEGRO=[0,0,0]
AMARILLO=[255,255,000]

#DANIEL SANCHEZ SEPULVEDA


#crear una matriz en el cual cada posicion tiene una imagen
def recorteSimple (imagenArecortar, x, y):
    imagen = pygame.image.load(imagenArecortar)
    limites = imagen.get_rect()
    lx = int(limites[2] / x)
    ly = int(limites[3] / y)
    m=[]
    for i in range(0,lx):
        for j in range(0, ly):
            cuadro=imagen.subsurface(i*x,j*y,x,y)
            m.append(cuadro)
    return m

######dependiendo de la cancion que escoja llama alguna de las funciones de redraw


def redrawWindonw():
    fondo=pygame.image.load('fondojuego.png')
    pantalla.blit(fondo,[0,0])
    pygame.display.flip()
    playerList.draw(pantalla)
    pygame.display.flip()

def redrawWindonwbetoven():

    fondo=pygame.image.load('fondojuego.png')
    pantalla.blit(fondo,[0,0])
    betoven=pygame.image.load('betoven.jpg')
    pantalla.blit(betoven,[20,20])
    pygame.display.flip()
    playerList.draw(pantalla)
    pygame.display.flip()

def redrawWindonwestrellita():

    fondo=pygame.image.load('fondojuego.png')
    pantalla.blit(fondo,[0,0])
    estrellita=pygame.image.load('estrellita.jpg')
    pantalla.blit(estrellita,[20,20])
    pygame.display.flip()
    playerList.draw(pantalla)
    pygame.display.flip()

def redrawWindonwmanana():
    fondo=pygame.image.load('fondojuego.png')
    pantalla.blit(fondo,[0,0])
    manana=pygame.image.load('manana.jpg')
    pantalla.blit(manana,[20,20])
    pygame.display.flip()
    playerList.draw(pantalla)
    pygame.display.flip()

def redrawWindonwgranja():
    fondo=pygame.image.load('fondojuego.png')
    pantalla.blit(fondo,[0,0])
    granja=pygame.image.load('granja.jpg')
    pantalla.blit(granja,[20,20])
    pygame.display.flip()
    playerList.draw(pantalla)
    pygame.display.flip()



#es el pianista que toca su instrumento infinitamente

class Estatico(pygame.sprite.Sprite):
    def __init__(self, sheet):
        pygame.sprite.Sprite.__init__(self)
        self.action = 0 #Acciones que puede tomar el sprite
        self.limit = 0 #Sprite que se esta ejecutando en dicha accion
        self.lim = [2] #Limite de cada una de las filas de acciones
        self.sheet = sheet #Sabana de sprites
        self.image = self.sheet[self.action][self.limit] #Carga una imagen en base a las coordenadas de la matriz de sprites
        self.rect = self.image.get_rect()
        self.rect.x = 70 #Posicion en x
        self.rect.y = 380 #Posicion en y
        self.frame = pygame.time.Clock()




    def update(self):
        if (self.limit > self.lim[self.action]):
            self.limit = 0

        elif self.action == 0:
            self.image = self.sheet[self.action][self.limit]
            self.limit += 1
            self.frame.tick(12)






if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([Ancho,Alto])

    fin = False
    game_over=False
    #CANCIONES
    himno=['E','E','R','T','T','R','E','W','Q','Q','W','E','E','W','W','E','E','R','T','T','R','E','W','Q','Q','W','E','W','Q','Q','W','W','E','Q','W','E','R','E','Q','W','E','R','E','W','Q','W','T','E','E','R','T','T','R','E','W','Q','Q','W','E','W','Q','Q']
    estrellita=['Q','Q','T','T','Y','Y','T','R','R','E','E','W','W','Q','T','T','R','R','E','E','W','T','T','R','R','E','E','W','Q','Q','T','T','Y','Y','T','R','R','E','E','W','W','Q']
    manana=['T','E','W','Q','W','E','T','E','W','Q','W','E','W','E','T','E','T','Y','E','Y','T','W','Q','T','E','W','Q','W','E','T','E','W','Q','W','E','W','E','T','E','T','Y','E','Y','T','W','Q']
    granja=['W','T','T','T','W','E','E','W','U','U','Y','Y','T','W','T','T','T','W','E','E','W','U','U','Y','Y','T','W','W','T','T','T','W','W','T','T','T','T','T','T','T','T','T','T','T','T','T','T','T','W','T','T','T','W','E','E','W','U','U','Y','Y','T']
#lista vacia con el cual dependiendo de lo que presione el jugador
#agrega un elemento correspondiente a lo que presiono con el infinitamente
#con el fin de que se compare la posicion actual de la CANCION
#con la ultima posicion de la lista vacia, si es TRUE no pasa nada
#de lo contrario game over
    void=[]
#contador que va sumando cada vez que se presione una tecla del "piano"
#que em servira apra recorre la lista de la cancion
    con=-1
    #
    fondo=pygame.image.load('fondojuego.png')
    dedo=pygame.image.load('dedo.png')



    movimiento = recorteSimple('estatico.png',135,135)

    tocador=[movimiento]

    playerList = pygame.sprite.Group()
    player = Estatico(tocador)
    playerList.add(player)


    ### menu
    op=0
    #suenen o no suenen las notas
    seguir=True
    #bandera de control del win y game over
    flag=False
    #bandera para mostrar notas y tiempo
    flagmostrar=True
    #aux de tiempo
    auxtime=1
    Fuente=pygame.font.Font(None,25)
    Mostrarnotas=pygame.font.Font(None,80)



    msj2='pulsa A para el modo libre (sin limite)'
    msj3='pulsa B para El Himno a la alegria (tienes maximo 110 segundos)'
    msj4='pulsa C para Estrellita (tienes maximo 90 segundos)'
    msj5='pulsa D para Morning-Peer Gynt (tienes maximo 85 segundos)'
    msj6='pulsa E para El Viejo McDonald  (tienes maximo 95 segundos)'
    #
    msj7='BIENVENIDO A ESTE CORTO SIMULADOR DE PIANO'
    msj0='SI VAS A TOCAR UNA CANCION EL TIEMPO COMIENZA A CORRER DESDE YA,'
    msj1='ELIJE RAPIDO, EL RELOJ APARECERA CUANDO INICIES...'

    while (not fin) and op==0:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #fin de ciclo
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    op=1
                if event.key==pygame.K_b:
                    op=2
                if event.key==pygame.K_c:
                    op=3
                if event.key==pygame.K_d:
                    op=4
                if event.key==pygame.K_e:
                    op=5

            fondo=pygame.image.load('fondojuego.png')
            pantalla.blit(fondo,[0,0])
            texto2=Fuente.render(msj2,True,BLANCO)
            texto3=Fuente.render(msj3,True,BLANCO)
            texto4=Fuente.render(msj4,True,BLANCO)
            texto5=Fuente.render(msj5,True,BLANCO)
            texto6=Fuente.render(msj6,True,BLANCO)
            #
            texto7=Fuente.render(msj7,True,AMARILLO)
            texto0=Fuente.render(msj0,True,AMARILLO)
            texto1=Fuente.render(msj1,True,AMARILLO)

            #
            pantalla.blit(texto2,[0,110])
            pantalla.blit(texto3,[0,135])
            pantalla.blit(texto4,[0,160])
            pantalla.blit(texto5,[0,185])
            pantalla.blit(texto6,[0,210])
            #
            pantalla.blit(texto7,[0,5])
            pantalla.blit(texto0,[0,40])
            pantalla.blit(texto1,[0,65])


            pygame.display.flip()



    while not fin and op==1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
#PIANO LIBRE
            if event.type == pygame.KEYDOWN:
                #DO
                if event.key == pygame.K_q:

                    C=pygame.mixer.Sound('C.wav')
                    C.play()
                    pantalla.blit(dedo,[272,576])
                    pygame.display.flip()
                    #time.sleep(0.15)


                #DO SOSTENIDO
                if event.key == pygame.K_2:
                    Csostenido=pygame.mixer.Sound('C_s.wav')
                    Csostenido.play()
                    pantalla.blit(dedo,[304,448])
                    pygame.display.flip()
                    #time.sleep(0.15)

                #RE
                if event.key == pygame.K_w:
                    D=pygame.mixer.Sound('D.wav')
                    D.play()
                    pantalla.blit(dedo,[336,576])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #RE SOSTENIDO
                if event.key == pygame.K_3:
                    Dsostenido=pygame.mixer.Sound('D_s.wav')
                    Dsostenido.play()
                    pantalla.blit(dedo,[366,448])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #MI
                if event.key == pygame.K_e:
                    E=pygame.mixer.Sound('E.wav')
                    E.play()
                    pantalla.blit(dedo,[400,576])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #FA
                if event.key == pygame.K_r:
                    F=pygame.mixer.Sound('F.wav')
                    F.play()
                    pantalla.blit(dedo,[464,576])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #FA SOSTENIDO
                if event.key == pygame.K_5:
                    Fsotenido=pygame.mixer.Sound('F_s.wav')
                    Fsotenido.play()
                    pantalla.blit(dedo,[496,448])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #SOL
                if event.key == pygame.K_t:
                    G=pygame.mixer.Sound('G.wav')
                    G.play()
                    pantalla.blit(dedo,[528,576])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #SOL SOSTENIDO
                if event.key == pygame.K_6:
                    Gsostenido=pygame.mixer.Sound('G_s.wav')
                    Gsostenido.play()
                    pantalla.blit(dedo,[560,448])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #LA
                if event.key == pygame.K_y:
                    A=pygame.mixer.Sound('A.wav')
                    A.play()
                    pantalla.blit(dedo,[592,576])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #LA SOSTENIDO
                if event.key == pygame.K_7:
                    Asostenido=pygame.mixer.Sound('Bb.wav')
                    Asostenido.play()
                    pantalla.blit(dedo,[624,448])
                    pygame.display.flip()
                    #time.sleep(0.15)
                #SI
                if event.key == pygame.K_u:
                    B=pygame.mixer.Sound('B.wav')
                    B.play()
                    pantalla.blit(dedo,[656,576])
                    pygame.display.flip()
                    #time.sleep(0.15)

        if not game_over:
            player.update()

            redrawWindonw()


#opcion 2


    while not fin and op==2 :
        Tiempo=pygame.time.get_ticks()/1000



        #MANEJO DEL TIEMPO
        if flagmostrar==True:

            mostrarcronometro=Mostrarnotas.render(str(Tiempo), True, BLANCO)
            pantalla.blit(mostrarcronometro,(640,0))
            pygame.display.flip()
        if Tiempo==110 and flagmostrar==True:
            game_over=True
            Tiempo=0
            auxtime=0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN and seguir==True:

                #DO
                if event.key == pygame.K_q:
                    C=pygame.mixer.Sound('C.wav')
                    C.play()
                    pantalla.blit(dedo,[272,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('Q')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #DO SOSTENIDO
                if event.key == pygame.K_2:
                    Csostenido=pygame.mixer.Sound('C_s.wav')
                    Csostenido.play()
                    pantalla.blit(dedo,[304,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('2')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True

                #RE
                if event.key == pygame.K_w:
                    D=pygame.mixer.Sound('D.wav')
                    D.play()
                    pantalla.blit(dedo,[336,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('W')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #RE SOSTENIDO
                if event.key == pygame.K_3:
                    Dsostenido=pygame.mixer.Sound('D_s.wav')
                    Dsostenido.play()
                    pantalla.blit(dedo,[366,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('3')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #MI
                if event.key == pygame.K_e:
                    E=pygame.mixer.Sound('E.wav')
                    E.play()
                    pantalla.blit(dedo,[400,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('E')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #FA
                if event.key == pygame.K_r:
                    F=pygame.mixer.Sound('F.wav')
                    F.play()
                    pantalla.blit(dedo,[464,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('R')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #FA SOSTENIDO
                if event.key == pygame.K_5:
                    Fsotenido=pygame.mixer.Sound('F_s.wav')
                    Fsotenido.play()
                    pantalla.blit(dedo,[496,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('5')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SOL
                if event.key == pygame.K_t:
                    G=pygame.mixer.Sound('G.wav')
                    G.play()
                    pantalla.blit(dedo,[528,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('T')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SOL SOSTENIDO
                if event.key == pygame.K_6:
                    Gsostenido=pygame.mixer.Sound('G_s.wav')
                    Gsostenido.play()
                    pantalla.blit(dedo,[560,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('6')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #LA
                if event.key == pygame.K_y:
                    A=pygame.mixer.Sound('A.wav')
                    A.play()
                    pantalla.blit(dedo,[592,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('Y')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #LA SOSTENIDO
                if event.key == pygame.K_7:
                    Asostenido=pygame.mixer.Sound('Bb.wav')
                    Asostenido.play()
                    pantalla.blit(dedo,[624,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('7')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SI
                if event.key == pygame.K_u:
                    B=pygame.mixer.Sound('B.wav')
                    B.play()
                    pantalla.blit(dedo,[656,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('U')
                    if himno[con]==void[-1]:
                        pass
                    else:
                        game_over=True


        #MOSTRAR NOTAS
        if con==-1 and flagmostrar==True:
            #puntuacion
            combo=Fuente.render("Puntuacion: "+str(con+1)+"/62", True,BLANCO)
            pantalla.blit(combo,(380,15))

            sutiempo=Fuente.render("TIEMPO: ", True,BLANCO)
            pantalla.blit(sutiempo,(560,15))
            pulse=Fuente.render("PULSE ESTO:", True, BLANCO)
            pantalla.blit(pulse,(400,165))
            #importante
            mostrar=Mostrarnotas.render(str(himno[0]), True, VERDE)
            pantalla.blit(mostrar,(530,150))
            pygame.display.flip()
        elif con>=0 and con<=60 and flagmostrar==True:
            #puntuacion
            combo=Fuente.render("Puntuacion: "+str(con+1)+"/62", True,BLANCO)
            pantalla.blit(combo,(380,15))

            sutiempo=Fuente.render("TIEMPO: ", True,BLANCO)
            pantalla.blit(sutiempo,(560,15))
            pulse=Fuente.render("PULSE ESTO:", True, BLANCO)
            pantalla.blit(pulse,(400,165))
            #importante
            mostrar=Mostrarnotas.render(str(himno[con+1]), True, VERDE)
            pantalla.blit(mostrar,(530,150))
            pygame.display.flip()



        if game_over==False and flag==False:
            player.update()
            redrawWindonwbetoven()


        if game_over==True and flag==False:
           perder=pygame.image.load('perder.png')
           pantalla.blit(perder,[0,0])
           pygame.display.flip()
           buu=pygame.mixer.Sound('buu.ogg')
           buu.play()
           seguir=False
           flagmostrar=False
           Tiempo=0

        if len(void)==62 and void[-1]=='Q':
            flag=True
            victoria=pygame.image.load('ganar.png')
            pantalla.blit(victoria,[0,0])
            pygame.display.flip()
            aplausos=pygame.mixer.Sound('aplausos.ogg')
            aplausos.play()
            seguir=False
            flagmostrar=False
            Tiempo=0
            auxtime=0
    ##########ESTRELLITA#############
    while not fin and op==3 :
        Tiempo=pygame.time.get_ticks()/1000


        #MANEJO DEL TIEMPO
        if flagmostrar==True:

            mostrarcronometro=Mostrarnotas.render(str(Tiempo), True, BLANCO)
            pantalla.blit(mostrarcronometro,(640,0))
            pygame.display.flip()
        if Tiempo==90 and flagmostrar==True:
            game_over=True
            Tiempo=0
            auxtime=0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN and seguir==True:

                #DO
                if event.key == pygame.K_q:
                    C=pygame.mixer.Sound('C.wav')
                    C.play()
                    pantalla.blit(dedo,[272,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('Q')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #DO SOSTENIDO
                if event.key == pygame.K_2:
                    Csostenido=pygame.mixer.Sound('C_s.wav')
                    Csostenido.play()
                    pantalla.blit(dedo,[304,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('2')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True

                #RE
                if event.key == pygame.K_w:
                    D=pygame.mixer.Sound('D.wav')
                    D.play()
                    pantalla.blit(dedo,[336,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('W')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #RE SOSTENIDO
                if event.key == pygame.K_3:
                    Dsostenido=pygame.mixer.Sound('D_s.wav')
                    Dsostenido.play()
                    pantalla.blit(dedo,[366,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('3')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #MI
                if event.key == pygame.K_e:
                    E=pygame.mixer.Sound('E.wav')
                    E.play()
                    pantalla.blit(dedo,[400,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('E')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #FA
                if event.key == pygame.K_r:
                    F=pygame.mixer.Sound('F.wav')
                    F.play()
                    pantalla.blit(dedo,[464,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('R')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #FA SOSTENIDO
                if event.key == pygame.K_5:
                    Fsotenido=pygame.mixer.Sound('F_s.wav')
                    Fsotenido.play()
                    pantalla.blit(dedo,[496,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('5')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SOL
                if event.key == pygame.K_t:
                    G=pygame.mixer.Sound('G.wav')
                    G.play()
                    pantalla.blit(dedo,[528,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('T')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SOL SOSTENIDO
                if event.key == pygame.K_6:
                    Gsostenido=pygame.mixer.Sound('G_s.wav')
                    Gsostenido.play()
                    pantalla.blit(dedo,[560,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('6')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #LA
                if event.key == pygame.K_y:
                    A=pygame.mixer.Sound('A.wav')
                    A.play()
                    pantalla.blit(dedo,[592,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('Y')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #LA SOSTENIDO
                if event.key == pygame.K_7:
                    Asostenido=pygame.mixer.Sound('Bb.wav')
                    Asostenido.play()
                    pantalla.blit(dedo,[624,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('7')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SI
                if event.key == pygame.K_u:
                    B=pygame.mixer.Sound('B.wav')
                    B.play()
                    pantalla.blit(dedo,[656,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('U')
                    if estrellita[con]==void[-1]:
                        pass
                    else:
                        game_over=True


        #MOSTRAR NOTAS
        if con==-1 and flagmostrar==True:
            #puntuacion
            combo=Fuente.render("Puntuacion: "+str(con+1)+"/42", True,BLANCO)
            pantalla.blit(combo,(380,15))

            sutiempo=Fuente.render("TIEMPO: ", True,BLANCO)
            pantalla.blit(sutiempo,(560,15))
            pulse=Fuente.render("PULSE ESTO:", True, BLANCO)
            pantalla.blit(pulse,(400,165))
            #importante
            mostrar=Mostrarnotas.render(str(estrellita[0]), True, VERDE)
            pantalla.blit(mostrar,(530,150))
            pygame.display.flip()
        elif con>=0 and con<=40 and flagmostrar==True:
            #puntuacion
            combo=Fuente.render("Puntuacion: "+str(con+1)+"/42", True,BLANCO)
            pantalla.blit(combo,(380,15))

            sutiempo=Fuente.render("TIEMPO: ", True,BLANCO)
            pantalla.blit(sutiempo,(560,15))
            pulse=Fuente.render("PULSE ESTO:", True, BLANCO)
            pantalla.blit(pulse,(400,165))
            #importante
            mostrar=Mostrarnotas.render(str(estrellita[con+1]), True, VERDE)
            pantalla.blit(mostrar,(530,150))
            pygame.display.flip()



        if game_over==False and flag==False:
            player.update()
            redrawWindonwestrellita()


        if game_over==True and flag==False:
           perder=pygame.image.load('perder.png')
           pantalla.blit(perder,[0,0])
           pygame.display.flip()
           buu=pygame.mixer.Sound('buu.ogg')
           buu.play()
           seguir=False
           flagmostrar=False
           Tiempo=0

        if len(void)==42 and void[-1]=='Q':
            flag=True
            victoria=pygame.image.load('ganar.png')
            pantalla.blit(victoria,[0,0])
            pygame.display.flip()
            aplausos=pygame.mixer.Sound('aplausos.ogg')
            aplausos.play()
            seguir=False
            flagmostrar=False
            Tiempo=0
            auxtime=0

    #####manana
    while not fin and op==4 :
        Tiempo=pygame.time.get_ticks()/1000


        #MANEJO DEL TIEMPO
        if flagmostrar==True:

            mostrarcronometro=Mostrarnotas.render(str(Tiempo), True, BLANCO)
            pantalla.blit(mostrarcronometro,(640,0))
            pygame.display.flip()
        if Tiempo==90 and flagmostrar==True:
            game_over=True
            Tiempo=0
            auxtime=0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN and seguir==True:

                #DO
                if event.key == pygame.K_q:
                    C=pygame.mixer.Sound('C.wav')
                    C.play()
                    pantalla.blit(dedo,[272,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('Q')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #DO SOSTENIDO
                if event.key == pygame.K_2:
                    Csostenido=pygame.mixer.Sound('C_s.wav')
                    Csostenido.play()
                    pantalla.blit(dedo,[304,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('2')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True

                #RE
                if event.key == pygame.K_w:
                    D=pygame.mixer.Sound('D.wav')
                    D.play()
                    pantalla.blit(dedo,[336,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('W')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #RE SOSTENIDO
                if event.key == pygame.K_3:
                    Dsostenido=pygame.mixer.Sound('D_s.wav')
                    Dsostenido.play()
                    pantalla.blit(dedo,[366,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('3')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #MI
                if event.key == pygame.K_e:
                    E=pygame.mixer.Sound('E.wav')
                    E.play()
                    pantalla.blit(dedo,[400,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('E')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #FA
                if event.key == pygame.K_r:
                    F=pygame.mixer.Sound('F.wav')
                    F.play()
                    pantalla.blit(dedo,[464,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('R')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #FA SOSTENIDO
                if event.key == pygame.K_5:
                    Fsotenido=pygame.mixer.Sound('F_s.wav')
                    Fsotenido.play()
                    pantalla.blit(dedo,[496,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('5')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SOL
                if event.key == pygame.K_t:
                    G=pygame.mixer.Sound('G.wav')
                    G.play()
                    pantalla.blit(dedo,[528,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('T')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SOL SOSTENIDO
                if event.key == pygame.K_6:
                    Gsostenido=pygame.mixer.Sound('G_s.wav')
                    Gsostenido.play()
                    pantalla.blit(dedo,[560,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('6')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #LA
                if event.key == pygame.K_y:
                    A=pygame.mixer.Sound('A.wav')
                    A.play()
                    pantalla.blit(dedo,[592,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('Y')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #LA SOSTENIDO
                if event.key == pygame.K_7:
                    Asostenido=pygame.mixer.Sound('Bb.wav')
                    Asostenido.play()
                    pantalla.blit(dedo,[624,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('7')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SI
                if event.key == pygame.K_u:
                    B=pygame.mixer.Sound('B.wav')
                    B.play()
                    pantalla.blit(dedo,[656,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('U')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True


        #MOSTRAR NOTAS
        if con==-1 and flagmostrar==True:
            #puntuacion
            combo=Fuente.render("Puntuacion: "+str(con+1)+"/46", True,BLANCO)
            pantalla.blit(combo,(380,15))

            sutiempo=Fuente.render("TIEMPO: ", True,BLANCO)
            pantalla.blit(sutiempo,(560,15))
            pulse=Fuente.render("PULSE ESTO:", True, BLANCO)
            pantalla.blit(pulse,(400,165))
            #importante
            mostrar=Mostrarnotas.render(str(granja[0]), True, VERDE)
            pantalla.blit(mostrar,(530,150))
            pygame.display.flip()
        elif con>=0 and con<=44 and flagmostrar==True:
            #puntuacion
            combo=Fuente.render("Puntuacion: "+str(con+1)+"/46", True,BLANCO)
            pantalla.blit(combo,(380,15))

            sutiempo=Fuente.render("TIEMPO: ", True,BLANCO)
            pantalla.blit(sutiempo,(560,15))
            pulse=Fuente.render("PULSE ESTO:", True, BLANCO)
            pantalla.blit(pulse,(400,165))
            #importante
            mostrar=Mostrarnotas.render(str(granja[con+1]), True, VERDE)
            pantalla.blit(mostrar,(530,150))
            pygame.display.flip()



        if game_over==False and flag==False:
            player.update()
            redrawWindonwgranja()


        if game_over==True and flag==False:
           perder=pygame.image.load('perder.png')
           pantalla.blit(perder,[0,0])
           pygame.display.flip()
           buu=pygame.mixer.Sound('buu.ogg')
           buu.play()
           seguir=False
           flagmostrar=False
           Tiempo=0

        if len(void)==46 and void[-1]=='Q':
            flag=True
            victoria=pygame.image.load('ganar.png')
            pantalla.blit(victoria,[0,0])
            pygame.display.flip()
            aplausos=pygame.mixer.Sound('aplausos.ogg')
            aplausos.play()
            seguir=False
            flagmostrar=False
            Tiempo=0
            auxtime=0

    #########granja
    while not fin and op==5 :
        Tiempo=pygame.time.get_ticks()/1000


        #MANEJO DEL TIEMPO
        if flagmostrar==True:

            mostrarcronometro=Mostrarnotas.render(str(Tiempo), True, BLANCO)
            pantalla.blit(mostrarcronometro,(640,0))
            pygame.display.flip()
        if Tiempo==95 and flagmostrar==True:
            game_over=True
            Tiempo=0
            auxtime=0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN and seguir==True:

                #DO
                if event.key == pygame.K_q:
                    C=pygame.mixer.Sound('C.wav')
                    C.play()
                    pantalla.blit(dedo,[272,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('Q')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #DO SOSTENIDO
                if event.key == pygame.K_2:
                    Csostenido=pygame.mixer.Sound('C_s.wav')
                    Csostenido.play()
                    pantalla.blit(dedo,[304,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('2')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True

                #RE
                if event.key == pygame.K_w:
                    D=pygame.mixer.Sound('D.wav')
                    D.play()
                    pantalla.blit(dedo,[336,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('W')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #RE SOSTENIDO
                if event.key == pygame.K_3:
                    Dsostenido=pygame.mixer.Sound('D_s.wav')
                    Dsostenido.play()
                    pantalla.blit(dedo,[366,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('3')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #MI
                if event.key == pygame.K_e:
                    E=pygame.mixer.Sound('E.wav')
                    E.play()
                    pantalla.blit(dedo,[400,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('E')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #FA
                if event.key == pygame.K_r:
                    F=pygame.mixer.Sound('F.wav')
                    F.play()
                    pantalla.blit(dedo,[464,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('R')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #FA SOSTENIDO
                if event.key == pygame.K_5:
                    Fsotenido=pygame.mixer.Sound('F_s.wav')
                    Fsotenido.play()
                    pantalla.blit(dedo,[496,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('5')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SOL
                if event.key == pygame.K_t:
                    G=pygame.mixer.Sound('G.wav')
                    G.play()
                    pantalla.blit(dedo,[528,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('T')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SOL SOSTENIDO
                if event.key == pygame.K_6:
                    Gsostenido=pygame.mixer.Sound('G_s.wav')
                    Gsostenido.play()
                    pantalla.blit(dedo,[560,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('6')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #LA
                if event.key == pygame.K_y:
                    A=pygame.mixer.Sound('A.wav')
                    A.play()
                    pantalla.blit(dedo,[592,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('Y')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #LA SOSTENIDO
                if event.key == pygame.K_7:
                    Asostenido=pygame.mixer.Sound('Bb.wav')
                    Asostenido.play()
                    pantalla.blit(dedo,[624,448])
                    pygame.display.flip()
                    con=con+1
                    void.append('7')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True
                #SI
                if event.key == pygame.K_u:
                    B=pygame.mixer.Sound('B.wav')
                    B.play()
                    pantalla.blit(dedo,[656,576])
                    pygame.display.flip()
                    con=con+1
                    void.append('U')
                    if granja[con]==void[-1]:
                        pass
                    else:
                        game_over=True


        #MOSTRAR NOTAS
        if con==-1 and flagmostrar==True:
            #puntuacion
            combo=Fuente.render("Puntuacion: "+str(con+1)+"/61", True,BLANCO)
            pantalla.blit(combo,(380,15))

            sutiempo=Fuente.render("TIEMPO: ", True,BLANCO)
            pantalla.blit(sutiempo,(560,15))
            pulse=Fuente.render("PULSE ESTO:", True, BLANCO)
            pantalla.blit(pulse,(400,165))
            #importante
            mostrar=Mostrarnotas.render(str(granja[0]), True, VERDE)
            pantalla.blit(mostrar,(530,150))
            pygame.display.flip()
        elif con>=0 and con<=59 and flagmostrar==True:
            #puntuacion
            combo=Fuente.render("Puntuacion: "+str(con+1)+"/61", True,BLANCO)
            pantalla.blit(combo,(380,15))

            sutiempo=Fuente.render("TIEMPO: ", True,BLANCO)
            pantalla.blit(sutiempo,(560,15))
            pulse=Fuente.render("PULSE ESTO:", True, BLANCO)
            pantalla.blit(pulse,(400,165))
            #importante
            mostrar=Mostrarnotas.render(str(granja[con+1]), True, VERDE)
            pantalla.blit(mostrar,(530,150))
            pygame.display.flip()



        if game_over==False and flag==False:
            player.update()
            redrawWindonwgranja()


        if game_over==True and flag==False:
           perder=pygame.image.load('perder.png')
           pantalla.blit(perder,[0,0])
           pygame.display.flip()
           buu=pygame.mixer.Sound('buu.ogg')
           buu.play()
           seguir=False
           flagmostrar=False
           Tiempo=0

        if len(void)==61 and void[-1]=='T':
            flag=True
            victoria=pygame.image.load('ganar.png')
            pantalla.blit(victoria,[0,0])
            pygame.display.flip()
            aplausos=pygame.mixer.Sound('aplausos.ogg')
            aplausos.play()
            seguir=False
            flagmostrar=False
            Tiempo=0
            auxtime=0
