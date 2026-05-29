extends MeshInstance3D

var velocidad = 5.0
var rotacion = 2.0

func _process(delta):

	# Movimiento WASD
	if Input.is_action_pressed("ui_left"):
		position.x -= velocidad * delta

	if Input.is_action_pressed("ui_right"):
		position.x += velocidad * delta

	if Input.is_action_pressed("ui_up"):
		position.z -= velocidad * delta

	if Input.is_action_pressed("ui_down"):
		position.z += velocidad * delta

	if Input.is_key_pressed(KEY_W):
		position.y += velocidad * delta

	if Input.is_key_pressed(KEY_S):
		position.y -= velocidad * delta

	# Rotación con flechas
	if Input.is_key_pressed(KEY_A):
		rotate_y(rotacion * delta)

	if Input.is_key_pressed(KEY_D):
		rotate_y(-rotacion * delta)
