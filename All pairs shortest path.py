#ALL PAIRS SHORTEST PATH

'''The sensors are deployed in forest using drone facility. The sensors are transmitting message to base station using
point to point transmission. Derive a suitable mechanism to transmit the message assuming any one sensor as start point
and any one sensor as base location.'''
INF = 99

def path_print(path,k,i):
    '''if k == i:print(k+1,end=" ")
    elif path[k][i] == INF:print("No path from " ,k+1, " to " , i+1)
    else:
        path_print( path, k, path[k][i] )
        print(i+1,end=" ")'''
    if path[k][i]==-1:
        return ["no path exists"]
    elif k==i:
        return ["same sensor and base location. Hence,no path"]
    npath=[k+1]
    while k!=i:
        k=path[k][i]
        npath.append(k+1)
    return npath

def transmit_msg(sensors,sensor_locations):
    path=[]
    for x in range(sensors):
        path.append([])
        for y in range(sensors):
            if sensor_locations[x][y]==INF:
                path[x].append(-1)
            else:
                path[x].append(y)

    for k in range(0, sensors):             #SOURCE
        for i in range(0, sensors):         #DESTINATION
            for j in range(0, sensors):     #INTERMEDIATES
                #sensor_locations[k][i]=min(sensor_locations[k][i],sensor_locations[k][j]+sensor_locations[j][i])
                if sensor_locations[k][i]>sensor_locations[k][j]+sensor_locations[j][i]:
                    sensor_locations[k][i]=sensor_locations[k][j]+sensor_locations[j][i]
                    path[k][i]=path[k][j]
    print("The matrix below shows the shortest distance between a start point and base location.\n")

    print("o/d", end=' ')
    for i in range(0, sensors):
        print("\t{:d}".format(i+1), end=' ')
    print("\n")
    for i in range(0, sensors):
        print("{:d}\t".format(i+1), end=' ')
        for j in range(0,sensors):
            print("\t{:d}".format(sensor_locations[i][j]), end=' ')
        print()
    print("\n")
    for k in range(0, sensors):
        for i in range(0, sensors):
            print("Path from ",k+1," to " ,i+1, " is: ",*path_print(path,k,i))


sensor_locations = [
            [  0,   4,  4,  INF ],
            [  4,   0,  5,  9   ],
            [  6,   2,  0, INF],
            [INF,   INF, 3,  0]
        ]
print("\nPERFECTLY WORKING SYSTEM:")
transmit_msg(4, sensor_locations)

#consider sensor 3 as faulty. Hence,there will be no paths from sensor 3.Thus, the sensor_location matrix will change as follows:
sensor_locations[2][0]=INF
sensor_locations[2][1]=INF
sensor_locations[2][2]=INF
sensor_locations[2][3]=INF
print("\nFOR THE SYSTEM WITH FAULTY SENSOR:")
transmit_msg(4, sensor_locations)

#consider any edge,say from sensor 2 to sensor 4 as faulty. Hence,there will be no path from sensor 2 to 4.
# Thus, the sensor_location matrix will change as follows:
sensor_locations[1][3]=INF
print("\nFOR THE SYSTEM WITH FAULTY EDGE:")
transmit_msg(4, sensor_locations)
