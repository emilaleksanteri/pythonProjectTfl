from stopTimes import StopTimes

'''
 data schema from objects:
[{
    "lineName": string
    "stationName": string
    "platFormName": string
    "direction": string
    "goingTowards": string
    "finalDestination": string
    "timeToStationMins": int
}]
'''


def main():
    # objects for all stops:

    # Henriques Street (Stop P)
    henriquesStreet = StopTimes("490009276E")
    print(henriquesStreet.getStationData())

    # New Road (Stop Q)
    newRoad = StopTimes("490010255E")
    print(newRoad.getStationData())

    # Aldgate East Station (Stop E)
    aldgateEastStationBus = StopTimes("490000004E")
    print(aldgateEastStationBus.getStationData())

    # Altab Ali Park (Stop D)
    altabAliPark = StopTimes("490006827W")
    print(altabAliPark.getStationData())

    # The underground
    aldgateEastUnderground = StopTimes("940GZZLUADE")
    print(aldgateEastUnderground.getStationData())


main()
