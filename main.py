import pygame
from pygame.locals import *
pygame.init()
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Tic Tac Toe')

markers = []
clicked = False
pos = []
player = 1
line_width = 3
winner  = 0
game_over = False


green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
font  = pygame.font.SysFont(None,40)

def draw_grid():
    bg = (20,189,172)
    grid = (50,50,50)
    screen.fill(bg)
    for i in range(1,3):
        pygame.draw.line(screen,grid,(0,i * 100),(screen_width, i * 100),3)
        pygame.draw.line(screen,grid,(i * 100,0),( i * 100,screen_height),3)

for x in range(3):
    row = [0] * 3
    markers.append(row)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
				pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
			if y == -1:
				pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
			y_pos += 1
		x_pos += 1

def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in markers:
        if sum(x) == 3:
               winner  = 1
               game_over = True
        if sum(x) == -3:
               winner = 2
               game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 2
            game_over = True
        y_pos += 1  
            
        
    if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
         winner = 1
         game_over = True
    if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
         winner = 2
         game_over = True
         
def draw_winner(winner):
     win_text = "Player " + str(winner) +" wins"
     win_image = font.render(win_text,True,green)
     pygame.draw.rect(screen,blue,(screen_width//2 - 100,screen_height//2 - 60,200,50))
     screen.blit(win_image,(screen_width//2 - 100,screen_height//2 - 50))


run = True
while run:
    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y //100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    check_winner()
    if game_over == True:
        draw_winner(winner)


    pygame.display.update()
pygame.quit()