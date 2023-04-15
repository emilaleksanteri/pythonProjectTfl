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
            dataDict = {
                "lineName": line["lineName"],
                "stationName": line["stationName"],
                "platFormName": line["platformName"],
                "direction": line["direction"],
                "goingTowards": line["towards"],
                "finalDestination": line["destinationName"],
                "timeToStationMins": int(line["timeToStation"]/60)
            }
            stopData.append(dataDict)

        return stopData
