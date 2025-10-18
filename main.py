clear()
change_hat(Hats.Wizard_Hat)

## Global Variables
pumpkinAreaSize = 6

## Imports
import pumpkinArea
import treePlanting

while True:
	pumpkinArea.pumpkinAreaProcessor(pumpkinAreaSize)
	treePlanting.treeAreaProcessor(pumpkinAreaSize)