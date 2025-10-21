import utils
import treeAndCarrot
import grass
import sunflower

def farmPlantProcessor(worldSize, pumpkinAreaSize, sunflowerAreaSize):
	firstPumpkinId = 0
	
	for heightY in range(worldSize):
		for lengthX in range(worldSize):
			if utils.isFirstPumpkin():
				firstPumpkinId = measure()
			 			
			elif utils.isLastPumpkin(pumpkinAreaSize):
				if firstPumpkinId == measure():
					harvest()

			if utils.isInPumpkinArea(pumpkinAreaSize):
				if get_entity_type() != Entities.Pumpkin:
					if get_ground_type() != Grounds.Soil:
						till()
					plant(Entities.Pumpkin)
			
			treeAndCarrot.treeAndCarrotProcessor(heightY, lengthX, pumpkinAreaSize)
			grass.grassProcessor(heightY, lengthX, pumpkinAreaSize, sunflowerAreaSize)
			sunflower.sunflowerProcessor(heightY, lengthX, pumpkinAreaSize, sunflowerAreaSize)
			
			move(East)
		move(North)