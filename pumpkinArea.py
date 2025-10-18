def pumpkinAreaProcessor(pumpkinAreaSize):
	pumpkinId = 0
	for alturaX in range(get_world_size()):
		for cumprimentoY in range(get_world_size()):
			if get_pos_x() == 0 and get_pos_y() == 0 and get_entity_type() == Entities.Pumpkin:
				pumpkinId = measure()
			elif get_pos_x() == pumpkinAreaSize and get_pos_y() == pumpkinAreaSize and get_entity_type() == Entities.Pumpkin:
				if pumpkinId == measure():
					if can_harvest():
						harvest()
			if get_pos_x() <= pumpkinAreaSize and get_pos_y() <= pumpkinAreaSize:
				if get_ground_type() != Grounds.Soil:
					till()
				else:
					if get_entity_type() != Entities.Pumpkin:
						plant(Entities.Pumpkin)
			move(East)
		move(North)