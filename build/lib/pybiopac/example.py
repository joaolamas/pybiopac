from biopac import *

b = pybiopac(ip="172.16.31.236")
b.getMPUnitType()
b.getEnabledChannels()

b.getSampRate()
b.changeUDPBroadcastEnabled(True)

b.getDataDeliveryEnabled('analog', 0)
b.getDataDeliveryEnabled('calc', 0)


b.changeDataDeliveryEnabled('analog', 0, boolean=True)
b.changeDataDeliveryEnabled('calc', 0, boolean=True)

b.getMostRecentSampleValueDeliveryEnabled('analog', 0)
b.getMostRecentSampleValueDeliveryEnabled('calc', 0)

b.changeMostRecentSampleValueDeliveryEnabled('analog', 0, boolean=True)
b.changeMostRecentSampleValueDeliveryEnabled('calc', 0, boolean=True)

a = input('waitting')

while True:
    try:
        print(b.getMostRecentSampleValue('analog', 0))
    except:
        pass
