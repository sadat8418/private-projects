import pygame
import random
pygame.init()


#Creating Window
screen_width=900
screen_height=600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()
clock =pygame.time.Clock()   # smooth korar jonno

font = pygame.font.SysFont(None, 55)
#Colors
White=(191,191,191)
Black=(0,0,0)
Red=(255,0,0)
snake_list =[]
snake_length = 1
#Score printing in Screen


def text_screen(text,color,x,y):
	screen_text = font.render(text,True,color)
	gameWindow.blit(screen_text, [x,y])
#make length increase

#Game Specific Variuables
exit_game=False
game_over=False
snake_x =50
snake_y =50
snake_size = 20
fps = 50
Vx =0
Vy =0
score =0
#food_x =random.randint(0,screen_width)
food_x =random.randint(20,screen_width/2) 		#To bring the food in center position
food_y =random.randint(20,screen_height/2)

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])





 
#Creating Game Loop (to quit window flickering)

while not exit_game:
		for  event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				exit_game = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					#print("You have pressed Right arrow")
					#snake_x=snake_x +10
					Vx =  +10
					Vy=0
				if event.key == pygame.K_LEFT:
					Vx= -10
					Vy = 0

				if event.key == pygame.K_UP:
					#snake_y=snake_y -10
					Vy = -10
					Vx =0	
				if event.key == pygame.K_DOWN:
					Vy=10
					Vx=0
	
		if abs(snake_x -food_x)<19 and abs(snake_y -food_y)<19:
				score +=1
				print("Score:",score)
				#food_x =random.randint(0,screen_width)
				food_x =random.randint(20,screen_width/2) 		#To bring the food in center position
				food_y =random.randint(20,screen_height/2)
				snake_length +=5
		if len(snake_list)> snake_length:
			del snake_list[0]

		snake_x += Vx
		snake_y += Vy 	
		gameWindow.fill(White)
		text_screen("Screen:"+str(score *10) , Red,5,5)
		#pygame.draw.rect(gameWindow,Black,[snake_x,snake_y,snake_size,snake_size])
	
	
		pygame.draw.rect(gameWindow,Red,[food_x,food_y,snake_size,snake_size])
		#pygame.display.update()	

	
		
		head=[]
		head.append(snake_x)
		head.append(snake_y)
		snake_list.append(head) 
		clock.tick(fps)
		
		plot_snake(gameWindow,Black,snake_list,snake_size)
		pygame.display.update()
pygame.quit()
quit()		