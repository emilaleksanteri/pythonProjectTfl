from tkinter import *
import urllib.request
import json
import sched
import time


def getStationData(scheduler):
    scheduler.enter(60, 1, getStationData, (scheduler,))
    try:
        url = "https://api.tfl.gov.uk/Line/district/Arrivals"

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
    districtPlt1 = []
    districtPlt2 = []

    for station in asDict:
        if station["stationName"] == "Aldgate East Underground Station":
            if station["platformName"] == "Westbound - Platform 1":
                districtPlt1.append({
                    "current": station["currentLocation"],
                    "from_platform": station["platformName"],
                    "final_stop": station["towards"],
                    "expected_arrival": round(station["timeToStation"]/60)
                })

            if station["platformName"] == "Eastbound - Platform 2":
                districtPlt2.append({
                    "current": station["currentLocation"],
                    "from_platform": station["platformName"],
                    "final_stop": station["towards"],
                    "expected_arrival": round(station["timeToStation"]/60)
                })

    print(districtPlt1)


my_scheduler = sched.scheduler(time.time, time.sleep)
getStationData(my_scheduler)
my_scheduler.enter(60, 1, getStationData, (my_scheduler,))
my_scheduler.run()
