import asyncio
from gekko import GEKKO
import websockets

print('Hi from GekkoGui!')

class GekkoGui(object):
    '''A GUI for GEKKO'''
    def test(self):
        return('Running from', __file__)


def test1():
    print('It Worked!')