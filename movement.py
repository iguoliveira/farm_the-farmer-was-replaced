def goTo(to):
	coords = getCoordinates(to)
	directions = getDirections(coords)

	for i in range(2):
		for _ in range(abs(coords[i])):
			move(directions[i])

def getCoordinates(to):
	worldSize = get_world_size()
	worldSizeHalfed = worldSize // 2
	
	currentlyPosition = [get_pos_x(), get_pos_y()]
	positions = []
	
	for i in range(2):
		positions.append((to[i] - currentlyPosition[i] + worldSizeHalfed) % worldSize - worldSizeHalfed)
	
	return positions

def getDirections(positions):
	windRose = [[East, West], [North, South]]
	directions = []
	
	for i in range(2):
		if positions[i] > 0:
			directions.append(windRose[i][0])
		else:
			directions.append(windRose[i][1])
			
	return directions