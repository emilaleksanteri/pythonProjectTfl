from tkinter import *
import urllib.request
import json
import sched
import time


class StationTimes:
    def __init__(self, lineId, stationName, platformName1, platformName2):
        self.lineId = lineId
        self.stationName = stationName
        self.platformName1 = platformName1
        self.platformName2 = platformName2

    def getStationData(self):
        try:
            url = "https://api.tfl.gov.uk/Line/" + self.lineId + "/Arrivals"

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

        platform1 = []
        platform2 = []

        for station in asDict:
            if station["stationName"] == self.stationName:
                if station["platformName"] == self.platformName1:
                    platform1.append({
                        "current": station["currentLocation"],
                        "from_platform": station["platformName"],
                        "final_stop": station["towards"],
                        "expected_arrival": round(station["timeToStation"]/60)
                    })

                if station["platformName"] == self.platformName2:
                    platform2.append({
                        "current": station["currentLocation"],
                        "from_platform": station["platformName"],
                        "final_stop": station["towards"],
                        "expected_arrival": round(station["timeToStation"]/60)
                    })

        return platform1, platform2


def main():
    district = StationTimes("district", "Aldgate East Underground Station",
                            "Westbound - Platform 1", "Eastbound - Platform 2")
    plt1, plt2 = district.getStationData()
    print(plt1)


main()
