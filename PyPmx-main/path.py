
import dis
from PyPmx import PmxInterface

pmx = PmxInterface()


def readCmos(addr):
    pmx.IoWrite8(0x70, addr | (1 << 7))
    return pmx.IoRead8(0x71)


def printCmosTime():
    hours = readCmos(4)
    minutes = readCmos(2)
    seconds = readCmos(0)
    print("time: %x:%x.%x" % (hours, minutes, seconds))


def printCmosDbg():
    print("dbg: %x" % (readCmos(0xe)))


printCmosTime()
printCmosDbg()
dis.dis(readCmos)