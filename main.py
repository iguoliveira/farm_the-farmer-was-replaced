clear()
change_hat(Hats.Traffic_Cone)

## Global Variables
worldSize = get_world_size()
pumpkinAreaSize = 5
sunflowerAreaSize = 1

## Imports
import farm

while True:
	farm.farmPlantProcessor(worldSize, pumpkinAreaSize, sunflowerAreaSize)