import pygame
import couleurs

def init(x,y):
    ''' elle recoit le couple (x,y) et cette fonction initialise
un dictionnaires des attributs de la personnage et le retourner'''
    att={}
    att['pos']=[x,y]
    att['lim']=590
    att['vit']=2
    att['img']=0
    return att

def dessine_0(x,y,surf):
    ''' cette fonction dessine l'homme_baton (avec jambes ouvertes)suivant les cordonees
(x,y) sur l'ecran '''
    pygame.draw.circle(surf,couleurs.BLANC,(x,y),5)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+8),(x-6,y+14),2)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+8),(x+6,y+14),2)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+6),(x,y+18),2)
    pygame.draw.line(surf,couleurs.BLEU,(x,y+19),(x-6,y+30),2)
    pygame.draw.line(surf,couleurs.BLEU,(x,y+19),(x+6,y+30),2)
    
def dessine_1(x,y,surf):
    ''' cette fonction dessine l'homme_baton (avec jambes semi-ouvertes)suivant les cordonees
(x,y) sur l'ecran '''
    pygame.draw.circle(surf,couleurs.BLANC,(x,y),5)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+8),(x-6,y+14),2)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+8),(x+6,y+14),2)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+6),(x,y+18),2)
    pygame.draw.line(surf,couleurs.BLEU,(x,y+19),(x-3,y+30),2)
    pygame.draw.line(surf,couleurs.BLEU,(x,y+19),(x+3,y+30),2)
    
def dessine_2(x,y,surf):
    ''' cette fonction dessine l'homme_baton (avec jambes fermees)suivant les cordonees
(x,y) sur l'ecran '''
    pygame.draw.circle(surf,couleurs.BLANC,(x,y),5)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+8),(x-6,y+14),2)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+8),(x+6,y+14),2)
    pygame.draw.line(surf,couleurs.ROUGE,(x,y+6),(x,y+18),2)
    pygame.draw.line(surf,couleurs.BLEU,(x,y+19),(x,y+30),2)
    
     

def met_a_jour(att):
    
    ''' recoit un dictionnaire de attribut de perso et met a jour ses deplacement
en ajoutant a sa position la vitesse de perso, donc cette fonction modifie
le dics att '''
    ##mettre a jour l'image du perso(l'att 'img')
    if att['img']<2:
        att['img']+=1
    else:
        att['img']=0
    
    ##mettre ajour la position de l'homme et rebondir sur le bord de l'ecran 
    att['pos'][0]+=att['vit']
    if att['pos'][0]>att['lim'] or att['pos'][0]<0:
        att['vit']*=-1
        
    return 
    
    
    
