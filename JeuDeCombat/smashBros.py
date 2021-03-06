import pygame

bleu = (14, 180, 245)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption('SMASH BROS')
pygame.key.set_repeat(30, 30)

fenetre_smash_bros = pygame.display.set_mode((720, 480))

rectangle = pygame.Rect(0, 450, 720, 480)

fenetre_smash_bros.fill(bleu)

pygame.draw.rect(fenetre_smash_bros, black, rectangle)

joueur1 = pygame.image.load("image/heros1_base.png").convert()
position_joueur1 = joueur1.get_rect()
fenetre_smash_bros.blit(joueur1,position_joueur1)


joueur2 = pygame.image.load("image/heros1_base.png").convert()
position_joueur2 = joueur2.get_rect()
position_joueur2.center= 100,100
fenetre_smash_bros.blit(joueur2, position_joueur2)


pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                position_joueur2 = position_joueur2.move(-5, 0)
            if event.key == pygame.K_d:
                position_joueur2 = position_joueur2.move(5, 0)
            if event.key == pygame.K_w:
                position_joueur2 = position_joueur2.move(0, -5)
            if event.key == pygame.K_s:
                position_joueur2 = position_joueur2.move(0, 5)
            if event.key == pygame.K_LEFT:
                position_joueur1 = position_joueur1.move(-5, 0)
            if event.key == pygame.K_RIGHT:
                position_joueur1 = position_joueur1.move(5, 0)
            if event.key == pygame.K_UP:
                position_joueur1 = position_joueur1.move(0, -5)
            if event.key == pygame.K_DOWN:
                position_joueur1 = position_joueur1.move(0, 5)

    fenetre_smash_bros.fill(bleu)
    pygame.draw.rect(fenetre_smash_bros, black, rectangle)
    fenetre_smash_bros.blit(joueur1, position_joueur1)
    fenetre_smash_bros.blit(joueur2, position_joueur2)
    pygame.display.flip()
