import utils
import treeAndCarrot

def farmPlantProcessor(worldSize, pumpkinAreaSize):
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
			move(East)
		move(North)