import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	#Initiating player
	new_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	#New AsteroidField
	new_field = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")

		#Draw the player
		#new_player.draw(screen) - replace by group
		for drawing in drawable:
			drawing.draw(screen)

		#update player position
		#new_player.update(dt) - replace by group
		for object in updatable:
			object.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(new_player):
				print("Game over!")
				sys.exit()
				
		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					shot.kill()
					asteroid.split()
				

		#Refresh the screen
		pygame.display.flip()

		#Limit to 60 fps
		dt = clock.tick(60)/1000




if __name__ == "__main__":
	main()
