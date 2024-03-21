from random import randint
import pygame
import couleurs


def init(nombre):
    ''' int----->dics(str:obj)
elle retourne un dictionnaire contenant les attributs des nuages'''
    att={}
    att['vit']=1
    att['lim']=(600,150)
    l=[]
    for i in range(nombre):
        l.append([randint(0,att['lim'][0]),randint(0,att['lim'][1])])
        
    att['objs']=l
    
    return att

def dessine(att,surf):
    ''' elle recoit les attribut de nuages et la suface de l'appli
et la fonction doit dessiner tous les nuages a leurs positions '''
    for i in range (len(att['objs'])):
        pygame.draw.ellipse(surf,couleurs.BLANC,(att['objs'][i][0],att['objs'][i][1],90,35))
        pygame.draw.ellipse(surf,couleurs.BLANC,(att['objs'][i][0]+14,att['objs'][i][1]-9,60,50))

def met_a_jour(att):
    ''' elle recoit les attributs de nuages , donc la fonction
doit faire bouger les nuages en ajoutant la vit (att['vit'])'''
    for i in range (len(att['objs'])):
        att['objs'][i][0]+=att['vit']
        if att['objs'][i][0]>att['lim'][0]:
            att['objs'][i][0]=-25
    return
