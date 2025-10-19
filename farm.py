import utils
import movement

def farmPlantProcessor(pumpkinAreaSize):
	firstPumpkinId = 0
	worldSize = get_world_size()
	
	for heightX in range(worldSize):
		for lengthY in range(worldSize):
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
			move(East)
		move(North)