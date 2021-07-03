import sys
sys.path.append('../')

from util import DeviceScanner

sc = DeviceScanner.Scanner()
sc.scan("192.168.0.107",2805)