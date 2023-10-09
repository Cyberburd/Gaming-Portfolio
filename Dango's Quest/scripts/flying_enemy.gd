extends KinematicBody2D

var enemyMovement = 100
var enemyMovementLong = 32 * 9

onready var enemyStartPositionY = self.position.y

func _physics_process(delta):
	move_local_y(enemyMovement * delta)
	if (self.position.y < enemyStartPositionY):
		enemyMovement = - enemyMovement
	elif (self.position.y > enemyStartPositionY + enemyMovementLong):
		enemyMovement = - enemyMovement
