extends KinematicBody2D

var enemyMovement = 45
var enemyMovementLong = 32 * 9

onready var enemyStartPositionX = self.position.x

func _physics_process(delta):
	move_local_x(enemyMovement * delta)
	if (self.position.x < enemyStartPositionX):
		enemyMovement = - enemyMovement
	elif (self.position.x > enemyStartPositionX + enemyMovementLong):
		enemyMovement = - enemyMovement


