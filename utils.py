def isFirstPumpkin():
	return get_pos_x() == 0 and get_pos_y() == 0 and get_entity_type() == Entities.Pumpkin

def isLastPumpkin(pumpkinAreaSize):
	return get_pos_x() == pumpkinAreaSize and get_pos_y() == pumpkinAreaSize and get_entity_type() == Entities.Pumpkin
	
def isInPumpkinArea(pumpkinAreaSize):
	return get_pos_x() <= pumpkinAreaSize and get_pos_y() <= pumpkinAreaSize
	

			
			