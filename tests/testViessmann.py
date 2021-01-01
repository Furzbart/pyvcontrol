import unittest
import logging
from pyvcontrol import viControl as v

class MyTestCase(unittest.TestCase):
    def test_readsequence(self):
        vo = v.viControl()
        vo.initComm()

        vd = vo.execReadCmd('Aussentemperatur')
        print(f'Aussentemperatur: {vd.value} °C')

        vd = vo.execReadCmd('Warmwassertemperatur')
        print(f'Warmwassertemperatur: {vd.value} °C')

        vd = vo.execReadCmd('Anlagentyp')
        print(f'Anlagentyp: {vd.value}')


if __name__ == '__main__':
    logging.basicConfig(filename='testVDirekt.log', filemode='w', level=logging.DEBUG)
    unittest.main()
