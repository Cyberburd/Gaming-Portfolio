extends KinematicBody2D

var direction = Vector2.RIGHT
var velocity = Vector2.ZERO


func _physics_process(_delta):
		velocity = direction * 80
		move_and_slide(velocity)
