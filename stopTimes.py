import urllib.request
import json


class StopTimes:
    def __init__(self, stopId):
        self.stopId = stopId

    def getStationData(self):
        try:
            url = "https://api.tfl.gov.uk/StopPoint/" + self.stopId + "/arrivals"

            hdr = {
                # Request headers
                'Cache-Control': 'no-cache',
            }

            req = urllib.request.Request(url, headers=hdr)

            req.get_method = lambda: 'GET'
            response = urllib.request.urlopen(req)
        except Exception as e:
            print(e)

        asDict = json.loads(response.read().decode())

        stopData = []

        for line in asDict:
            if "lineName" in line and "stationName" in line and "platformName" in line and "direction" in line and "towards" in line and "destinationName" in line and "timeToStation" in line:
                dataDict = {
                    "lineName": line["lineName"],
                    "stationName": line["stationName"],
                    "platFormName": line["platformName"],
                    "direction": line['direction'],
                    "goingTowards": line["towards"],
                    "finalDestination": line["destinationName"],
                    "timeToStationMins": int(line["timeToStation"]/60)
                }

            stopData.append(dataDict)

        # returns dict list as sorted by time to arrival
        stopDataSorted = sorted(stopData, key=lambda d: d['timeToStationMins'])

        return stopDataSorted
