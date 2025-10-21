def grassProcessor(heightY, lengthX, pumpkinAreaSize, sunflowerAreaSize):
	if heightY > sunflowerAreaSize and heightY <= pumpkinAreaSize and lengthX > pumpkinAreaSize:
		if can_harvest():
			harvest()
			plant(Entities.Grass)
		elif get_entity_type() != Entities.Grass:
			plant(Entities.Grass)