extends KinematicBody2D
class_name Player

export (int) var run_speed = 100
export (int) var jump_speed = -300
export (int) var gravity = 1000
export (int) var friction = 100

var velocity = Vector2()
var jumping = false

func get_input():
	velocity.x = 0	
	var right = Input.is_action_pressed('ui_right')
	var left = Input.is_action_pressed('ui_left')
	var jump = Input.is_action_just_pressed('ui_up')

	if jump and is_on_floor():
		jumping = true
		$AnimatedSprite.animation = "Jump"
		SoundPlayer.play_sound(SoundPlayer.JUMP)
		velocity.y = jump_speed
	if right:
		$AnimatedSprite.animation = "Right"
		velocity.x += run_speed
	if left:
		$AnimatedSprite.animation = "Left"
		velocity.x -= run_speed

func player_dies():
	SoundPlayer.play_sound(SoundPlayer.HURT)
	$AnimatedSprite.animation = "Dead"
	get_tree().reload_current_scene()


func _physics_process(delta):
	$AnimatedSprite.animation = "Idle"
	get_input()
	velocity.y += gravity * delta
	if jumping and is_on_floor():
		jumping = false
	velocity = move_and_slide(velocity, Vector2(0, -1))
	var _input = Vector2.ZERO
	

