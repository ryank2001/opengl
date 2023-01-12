import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math

pygame.init()
display = (1920, 1080)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
background = pygame.image.load("sterren.jpg")
screen.blit(background,(0,0))
glEnable(GL_DEPTH_TEST)

sphere = gluNewQuadric() #Create new sphere

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

def createplanet(texture, x, y, z , diameter, days, year_days):
    degrees = math.pi/180 * days / year_days *360
    
    x2 = x * math.cos(degrees)
    z = x * math.sin(degrees)
    glPushMatrix()
    glTranslatef(x2, y, z) #Move to the place
    glColor4f(0.5, 0.2, 0.2, 1) #Put color
    glBindTexture(GL_TEXTURE_2D, texture)
    glEnable(GL_TEXTURE_2D)
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    gluSphere(qobj, diameter, 10, 2000)
    gluDeleteQuadric(qobj)
    glPopMatrix()

def read_texture(filename):
    image = pygame.image.load(filename).convert_alpha()
    image_width,image_height = image.get_rect().size
    img_data = pygame.image.tostring(image,'RGBA')
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id) # This is what's missing
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,image_width,image_height,0,GL_RGBA,GL_UNSIGNED_BYTE,img_data)
    return texture_id


texture_mars = read_texture('mars.jpg')
texture_sun = read_texture('sun.png')
texture_merc = read_texture('2k_mercury.jpg')
texture_venus = read_texture('venus.jpeg')
texture_earth = read_texture('aarde.jpg')
texture_marss = read_texture('2k_mars.jpg')
texture_jupiter = read_texture('2k_jupiter.jpg')
texture_saturn = read_texture('2k_saturn.jpg')
texture_uranus = read_texture('2k_uranus.jpg')
texture_neptune = read_texture('2k_neptune.jpg')
counter = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False  

    

    # init model view matrix
    glLoadIdentity()
    
    # init the view matrix
    glPushMatrix()
    glLoadIdentity()
    keypress = pygame.key.get_pressed()
    # apply the movment 
    if keypress[pygame.K_w]:
        glTranslatef(0,0,0.1)
    if keypress[pygame.K_s]:
        glTranslatef(0,0,-0.1)
    if keypress[pygame.K_d]:
        glTranslatef(-0.1,0,0)
    if keypress[pygame.K_a]:
        glTranslatef(0.1,0,0)
    if keypress[pygame.K_q]:
        glRotatef(1,0,0,1)
    if keypress[pygame.K_e]:
        glRotatef(-1,0,0,1)
    if keypress[pygame.K_r]:
        glRotatef(1,1,0,0)
    if keypress[pygame.K_f]:
        glRotatef(-1,1,0,0)
    # multiply the current matrix by the get the new view matrix and store the final vie matrix 
    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    # apply view atrix
    glPopMatrix()
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Clear the screen

    
    createplanet(texture_sun, 0.00000001, 0, 0, 1.8, counter, 1)
    createplanet(texture_merc, 2, 0, 1, 0.05, counter, 88)
    createplanet(texture_venus, 4, 0, 0, 0.1, counter, 225)
    createplanet(texture_earth, 6, 0, 0, 0.2, counter, 365)
    createplanet(texture_marss, 8, 0, 0, 0.17, counter, 687)
    createplanet(texture_jupiter, 10, 0, 0, 0.8, counter, 4333)
    createplanet(texture_saturn, 12, 0, 0, 0.7, counter, 10759)
    createplanet(texture_uranus, 14, 0, 0, 0.4, counter, 30687)
    createplanet(texture_neptune, 16, 0, 0, 0.4, counter, 60190)
    

    

    

    

   


    screen.blit(background,(100,100))
    counter = counter +1
    pygame.display.flip() #Update the screen
    pygame.time.wait(10)

pygame.quit()

