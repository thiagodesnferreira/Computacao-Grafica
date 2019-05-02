from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

#Defina numero de Lados
size = 20

def defaultColor():
    #Magenta
    glColor3f(1,0,1)
    
def multiPolygon(size):
   #Desenha Base do Poligono
    glBegin(GL_LINE_LOOP)
    defaultColor()
    for i in range(size):
        glVertex3f(cos(2*pi*i/size) ,0,sin(2*pi*i/size))
    glEnd()

    #Desenha Topo do Poligono
    glBegin(GL_LINE_LOOP)
    defaultColor()
    for i in range(size):
        glVertex3f(cos(2*pi*i/size) ,1,sin(2*pi*i/size))
    glEnd()

     #Desenha Lados do Poligono
    for i in range(size):
        glBegin(GL_LINE_LOOP)
        defaultColor()
        #Conecta Base ao Topo
        glVertex3f(cos(2*pi*i/size) ,1,sin(2*pi*i/size))
        glVertex3f(cos(2*pi*i/size) ,0,sin(2*pi*i/size))  
        glEnd()



def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    multiPolygon(size)
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
glutCreateWindow("Multi-Polygon")


#Chama funcao drawr
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)


#Posiciona Camera para ver objeto
glTranslatef(0.0,0.0,-5)
glRotatef(0.0, 0.0, 0.0, 1.0)

#Controle de tempo e rotacao
glutTimerFunc(50,timer,1)
glutMainLoop()
