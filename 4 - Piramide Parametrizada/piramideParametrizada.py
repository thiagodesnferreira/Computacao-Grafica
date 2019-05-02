from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

#Defina numero de Lados
size = 5

def defaultColor():
    #Magenta
    glColor3f(1,0,1)
    
def pyramid(size):
    #Desenha vertices e base
    glBegin(GL_LINE_LOOP)
    defaultColor()
    for i in range(size):
        #Conecta vertice
        glVertex3f(cos(2*pi*i/size) ,0,sin(2*pi*i/size))
    glEnd()

    
    #Conecta Vertices ao Topo
    for i in range(size):
        glBegin(GL_LINE_LOOP)
        defaultColor()
        #Vertice Topo
        glVertex3f(0,1,0)
        #vertice Base
        glVertex3f(cos(2*pi*i/size) ,0,sin(2*pi*i/size))
        glVertex3f(cos(2*pi*(i+1)/size) ,0,sin(2*pi*(i+1)/size))
        glEnd()


def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    pyramid(size)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)


#Main
glutInit(sys.argv)
#Define o mode de Exibicao
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
#define tamanho da tela
glutInitWindowSize(800,600)
#Cria nome para Janela
glutCreateWindow("Multi-Pyramid")


#Chama funcao desenhar
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)

#Posiciona Camera
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-5)
glRotatef(45,1,1,1)

#Controle de velocidade
glutTimerFunc(50,timer,1)
glutMainLoop()
