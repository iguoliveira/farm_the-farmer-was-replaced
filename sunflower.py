def sunflowerProcessor(heightY, lengthX, pumpkinAreaSize, sunflowerAreaSize):
	if heightY <= sunflowerAreaSize and lengthX > pumpkinAreaSize:
		if get_ground_type() != Grounds.Soil:
			till()
			plant(Entities.Sunflower)
			
		if can_harvest():
			harvest()
			plant(Entities.Sunflower)
