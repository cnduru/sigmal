import sigmal
import sys

def testGenerateOffsets():
    expectedTupleSize = 3
    offsets = sigmal.generateOffsets()
    
    if expectedTupleSize != len(offsets):
        sys.exit(255)
        
testGenerateOffsets()
