extends Node


const HURT = preload("res://Sounds/dead.wav")
const JUMP = preload("res://Sounds/jump.wav")
const ENEMY_MOV = preload("res://Sounds/mov1.wav")
const ENEMY_MOV2 = preload("res://Sounds/mov2.wav")
const ENEMY_MOV3 = preload("res://Sounds/mov3.wav")
const BOSS_MOV = preload("res://Sounds/boss.wav")

onready var audioPlayers: = $AudioPlayers

func play_sound(sound):
	for audioStreamPlayer in  audioPlayers.get_children():
		if not audioStreamPlayer.playing:
			audioStreamPlayer.stream = sound
			audioStreamPlayer.play()
			break
	
