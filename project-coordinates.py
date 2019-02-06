import math

class Coor:
    def __init__(self, lat, long, alt):
        self.lat = lat
        self.long = long
        self.alt = alt
    def getValues(self):
        return [self.lat, self.long, self.alt]

def proj(droneC, dist, cameraC):
    distX = math.sin(math.radians(cameraC.lat)) * math.cos(math.radians(cameraC.long)) * dist
    distY = math.sin(math.radians(cameraC.lat)) * math.sin(math.radians(cameraC.long)) * dist
    distZ = math.cos(math.radians(cameraC.lat)) * dist
    #print "x: ",str(distX)
    #print "y: ",str(distY)
    #print "z: ",str(distZ)
    # length of a latitude degree (cm)
    LAT_DEG_LEN = 11056700
    # length of a longitude degree at the equator (cm)
    LONG_EQUATOR = 11132000
    # length of a longitude degree at current latitude (cm)
    LONG_DEG_LEN = abs(LONG_EQUATOR * math.cos(math.radians(droneC.lat)))
    #print LONG_DEG_LEN

    objC = Coor(
        droneC.lat + (distX / LAT_DEG_LEN),
        droneC.long + (distY / LONG_DEG_LEN),
        droneC.alt + distZ
    )

    #print objC.getValues()
    return objC.getValues()

def mapArea(droneC, dist, cameraC, STEP):
    map = []
    for i in range(0, 360/STEP):
        print "x"
        cameraC.long = (cameraC.long + i*10) % 360
        map.append(proj(droneC, dist, cameraC))
    return map

drone = Coor(45.0, 45.0, 20)
camera = Coor((0.0+270) % 360, (0.0+180) % 360, 0)
distance = 4000
proj(drone, distance, camera)
print mapArea(drone, distance, camera, 10)