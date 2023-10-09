extends Area2D

onready var animatedSprite: = $AnimatedSprite

func _on_CheckPoint_body_entered(body):
	if not body is Player: return
	animatedSprite.play("Flag")
	Events.emit_signal("hit_checkpoint", position) 
