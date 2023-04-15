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

    # New Road (Stop Q)
    newRoad = StopTimes("490010255E")

    # Aldgate East Station (Stop E)
    aldgateEastStationBus = StopTimes("490000004E")

    # Altab Ali Park (Stop D)
    altabAliPark = StopTimes("490006827W")

    # The underground
    aldgateEastUnderground = StopTimes("940GZZLUADE")
