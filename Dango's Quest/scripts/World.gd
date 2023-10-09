extends Node2D

var player_spawn_location = Vector2.ZERO

func _ready():
	VisualServer.set_default_clear_color(Color.cornflower)
	get_tree().paused = true
	yield(get_tree().create_timer(1.3), "timeout") 
	get_tree().paused = false
	Events.connect("hit_checkpoint", self, "_on_hit_checkpoint")
	
func _on_hit_checkpoint(checkpoint_position):
	player_spawn_location = checkpoint_position
