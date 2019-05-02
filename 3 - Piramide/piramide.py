from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def defaultColor():
    #Magenta
    glColor3f(1,0,1)

def pyramid():
    
    #L1
    glBegin(GL_LINE_LOOP)
    defaultColor()
    glVertex3f(1,0,1)
    glVertex3f(1,0,-1)
    glVertex3f(-1,0,-1)
    glVertex3f(-1,0,1)
    glEnd()
    
    #L2
    glBegin(GL_LINE_LOOP)
    defaultColor()
    glVertex3f(0,1,0)
    glVertex3f(1,0,1)
    glVertex3f(1,0,-1)
    glEnd()

    #L3
    glBegin(GL_LINE_LOOP)
    defaultColor()
    glVertex3f(0,1,0)
    glVertex3f(1,0,-1)
    glVertex3f(-1,0,-1)
    glEnd()
    
    #L4
    glBegin(GL_LINE_LOOP)
    defaultColor()
    glVertex3f(0,1,0)
    glVertex3f(-1,0,-1)
    glVertex3f(-1,0,1)
    glEnd()

   

  

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    pyramid()
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
glutCreateWindow("Pyramid")


#chama a funcao de desenhar 
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
