import pygame
import nuages
import perso
import couleurs

##Tscene=dics(str:obj)

def init():
    ''' cette fonction fait l'initialisation de pygame , la fenetre de l'application , et retourne un dictionnaire de
attribut de l'animation'''
    
    pygame.init()
    
    lar,haut=600,400
    surface=pygame.display.set_mode((lar,haut))
    
    pygame.display.set_caption(' PROMENADE EN MONTAGNE ')
    
    horloge=pygame.time.Clock()
    
    scene={}
    scene['surface']=surface
    scene['nuages']=nuages.init(4)
    scene['horloge']=horloge
    scene['dim_fen']=(lar,haut)
    scene['perso']=perso.init(500,303)
    scene['continuer']=True
    
    return scene

def boucle(dc):
    ''' cette fonction elle recoit un dc de type (Tscene) elle retourne rien mais elle modifie le dictionnaire passee en parametre '''
    while dc['continuer']:
        ##trairtement de l'evenement quit
        trait_ev(dc)
     ##mettre a jour la fenetre et ajuster la vitesse de la boucle
        dc['horloge'].tick(40)##40FP
    ##mettre a jours le scenario de jeu
        met_a_jour(dc)
     ##l'appele a la fonc dessine
        dessine(dc)
    return

def trait_ev(dc):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            dc['continuer']=False


def dessine(dc):
    ''' elle dessne les objets de l'animation '''
    dc['surface'].fill(couleurs.NOIR)
    dessine_ciel(dc['surface'],dc['dim_fen'])
    dessine_soleil(dc['surface'])
     ##dessiner les nuages
    nuages.dessine(dc['nuages'],dc['surface'])
    ##dessine les montagnes 
    dessine_montagne(dc['surface'])
    dessine_sol(dc['surface'],dc['dim_fen'])
    ###les arbres
    dessine_arbre(90,300,dc['surface'])
    dessine_arbre(200,270,dc['surface'])
    dessine_arbre(370,270,dc['surface'])
    ##dessine le personnage
    if dc['perso']['img']==0:
        perso.dessine_0(dc['perso']['pos'][0],dc['perso']['pos'][1],dc['surface'])
    elif dc['perso']['img']==1:
         perso.dessine_1(dc['perso']['pos'][0],dc['perso']['pos'][1],dc['surface'])
    else:
         perso.dessine_2(dc['perso']['pos'][0],dc['perso']['pos'][1],dc['surface'])
        
    ##continuer a dessiner les autrss arbres
    dessine_arbre(90,300,dc['surface'])
    dessine_arbre(280,300,dc['surface'])
    dessine_arbre(320,340,dc['surface'])
    dessine_arbre(440,340,dc['surface'])
    ##mettre a jour l'ecran
    pygame.display.update()
def met_a_jour(dc):
    if dc['continuer']:
        nuages.met_a_jour(dc['nuages'])
        perso.met_a_jour(dc['perso'])

    
def dessine_ciel(surf,dim_fen):
    pygame.draw.rect(surf,couleurs.VIOLET,(0,0,dim_fen[0],dim_fen[1]))
    
def dessine_soleil(surf):
    '''elle recoit une surface et dessine un soleil '''
    pygame.draw.circle(surf,couleurs.JAUNE_2,(470,50),25)
    pygame.draw.circle(surf,couleurs.JAUNE,(470,50),17)

def dessine_montagne(surf):
    pygame.draw.polygon(surf,couleurs.OLIVE,([-300,400],[550,400],[200,150]))
    pygame.draw.polygon(surf,couleurs.OLIVE,([100,400],[900,400],[480,150]))
    pygame.draw.polygon(surf,couleurs.BLANC,([200,150],[140,180],[240,180]))
    pygame.draw.polygon(surf,couleurs.BLANC,([480,150],[435,180],[530,180]))
def dessine_sol(surf,dim_fen):
    pygame.draw.rect(surf,couleurs.BLANC,(0,310,dim_fen[0],dim_fen[1]))
def dessine_arbre(x,y,surf):
    ''' deessine un arbre en position (x,y) passee en parametre'''
    for i in range(4):
        pygame.draw.polygon(surf,couleurs.VERT,([x,y+25+i*13],[x+20,y],[x+35,y+25+i*13]))
    return 
    
def quitte():
    '''la fonction doit juste quitter pygame '''
    pygame.quit()

