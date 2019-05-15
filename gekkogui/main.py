import asyncio
from gekko import GEKKO
import websockets

class GekkoGui(object):
    '''A GUI for GEKKO'''

    def __init__(self, path, constants, parameters, variables, intermediates):
        self.path = path
        self.constants = constants
        self.parameters = parameters
        self.variables = variables
        self.intermediates = intermediates

    def display(self):
        print('Display for Gekko model found at {}'.format(self.path))
        print('Constants: {}'.format(self.constants))

    def update(self):
        print('GekkoGui update not implmented')

