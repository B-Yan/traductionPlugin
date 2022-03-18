from dataclasses import dataclass

from numpy import unsignedinteger

@dataclass(init=True)
class Parameters:
    OFFSET: unsignedinteger     = 4 # []
    