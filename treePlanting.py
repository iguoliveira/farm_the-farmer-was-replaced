def treeAreaProcessor(pumpkinAreaSize):
	for alturaX in range(get_world_size()):
		for cumprimentoY in range(get_world_size()):	
			if (get_pos_x() % 2 == 0 or get_pos_y() % 2 == 0) and (get_pos_x() > pumpkinAreaSize or get_pos_y() > pumpkinAreaSize):
				plant(Entities.Tree)
			move(East)
		move(North)