import utils

def treeAndCarrotProcessor(heightY, lengthX, pumpkinAreaSize):
	if heightY > pumpkinAreaSize:
		if not utils.isEven(heightY):
			if utils.isEven(lengthX):
				if get_entity_type() != Entities.Tree:
					plant(Entities.Tree)
				elif can_harvest():
					harvest()
					plant(Entities.Tree)
			else:
				if get_ground_type() != Grounds.Soil:
					till()
					plant(Entities.Carrot)
				elif can_harvest():
					harvest()
					plant(Entities.Carrot)
		else:
			if not utils.isEven(lengthX):
				if get_entity_type() != Entities.Tree:
					plant(Entities.Tree)
				elif can_harvest():
					harvest()
					plant(Entities.Tree)
			else:
				if get_ground_type() != Grounds.Soil:
					till()
					plant(Entities.Carrot)
				elif can_harvest():
					harvest()
					plant(Entities.Carrot)