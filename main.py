clear()
change_hat(Hats.Wizard_Hat)

## Global Variables
pumpkinAreaSize = get_world_size() // 2
worldSize = get_world_size()

## Imports
import farm

while True:
	farm.farmPlantProcessor(worldSize, pumpkinAreaSize)