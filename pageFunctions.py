import pygame_gui
import pygame
from stopTimes import StopTimes
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel

# underground times


class Pages:
    def __init__(self, manager):
        self.manager = manager

    def showTimesUnderground(self, stationData, lineName, stationName, manager, home, makeHome):
        self.manager = manager
        home.generateTopBar(manager)
        home.page = lineName.lower()

        lineNameStyle = "@busstopheading"  # default
        panel = "@cirPanel"

        if lineName == "Hammersmith & City":
            panel = "@hamPanel"

        elif lineName == "District":
            panel = "@distPanel"

        elif lineName == "Circle":
            panel = "@cirPanel"

        getData = stationData.getStationData()

        # in case of an error, return to home page
        if getData == 'error':
            makeHome()

        home.transport = UIButton(relative_rect=pygame.Rect((50, 100), (250, 40)),
                                  text="←",
                                  manager=self.manager, object_id=ObjectID(class_id='@backHomeText'))

        self.station = UILabel(relative_rect=pygame.Rect((58, 150), (400, 40)),
                               text=stationName,
                               manager=self.manager, object_id=ObjectID(class_id='@busstopheading'))

        self.undergroundPanel = UIPanel(relative_rect=pygame.Rect((58, 200), (800, 60)),
                                        manager=self.manager, object_id=ObjectID(class_id=panel))

        self.panelTxt = UILabel(relative_rect=pygame.Rect((100, 210), (400, 40)),
                                text=lineName,
                                manager=self.manager, object_id=ObjectID(class_id="@busstopheading"))

        yAxis = 300
        uniquePlatforms = []
        for data in getData:
            # if requests are too fast, this might error, in case of an error, go home
            try:
                if data["lineName"] == lineName:
                    if data["platFormName"] not in uniquePlatforms:

                        # if 1 minute away the minutes text to minute
                        timeText = 'At platform in ' + \
                            str(data["timeToStationMins"]) + ' minutes'
                        if data["timeToStationMins"] == 1:
                            timeText = 'At platform in ' + \
                                str(data["timeToStationMins"]) + ' minute'

                        uniquePlatforms.append(data["platFormName"])
                        self.platForm = UILabel(relative_rect=pygame.Rect((100, yAxis), (400, 20)),
                                                text=data["platFormName"],
                                                manager=self.manager, object_id=ObjectID(class_id='@busstopheading'))

                        self.nextTrain = UILabel(relative_rect=pygame.Rect((450, yAxis - 30), (400, 20)),
                                                 text=data["currentlyAt"],
                                                 manager=self.manager, object_id=ObjectID(class_id='@busfinaldesttext'))

                        self.finalDestination = UILabel(relative_rect=pygame.Rect((450, yAxis), (500, 20)),
                                                        text='To ' +
                                                        data["finalDestination"],
                                                        manager=self.manager, object_id=ObjectID(class_id='@busfinaldesttext'))

                        self.arrivesIn = UILabel(relative_rect=pygame.Rect((450, yAxis + 30), (400, 20)),
                                                 text=timeText,
                                                 manager=self.manager, object_id=ObjectID(class_id='@busfinaldesttext'))

                        self.line = UIPanel(relative_rect=pygame.Rect((58, yAxis + 60), (800, 2)),
                                            manager=self.manager, object_id=ObjectID(class_id='@underGroundLine'))

                        yAxis += 100
            except:
                makeHome()

    # bus time view

    def showTimesForStop(self, stationData, stationName, stopLetter, manager, home, makeHome):
        # to get back to the home screen
        self.manager = manager
        home.page = stationName.lower()
        home.generateTopBar(manager)
        getData = stationData.getStationData()

        # in case of an error, return to home page
        if getData == 'error':
            makeHome()

        home.transport = UIButton(relative_rect=pygame.Rect((50, 150), (250, 40)),
                                  text="←",
                                  manager=self.manager, object_id=ObjectID(class_id='@backHomeText'))

        self.station = UILabel(relative_rect=pygame.Rect((58, 200), (250, 40)),
                               text=stationName,
                               manager=self.manager, object_id=ObjectID(class_id='@busstopheading'))

        self.stop = UILabel(relative_rect=pygame.Rect((58, 240), (250, 40)),
                            text=stopLetter,
                            manager=self.manager, object_id=ObjectID(class_id='@stopLetter'))

        yAxisBusses = 300
        uniqueNumbers = []
        for data in getData:
            # guard against frequent requests, same reason as for underground
            try:
                if data["lineName"] not in uniqueNumbers:
                    bus = pygame.image.load('./images/bus.png')
                    uniqueNumbers.append(data["lineName"])
                    self.busNumberContainer = UIPanel(relative_rect=pygame.Rect((58, yAxisBusses), (60, 60)),
                                                      manager=self.manager, object_id=ObjectID(class_id='@busNumber'))

                    self.busNumber = UILabel(relative_rect=pygame.Rect((0, 0), (30, 30)),
                                             text=data["lineName"], container=self.busNumberContainer,
                                             manager=self.manager, object_id=ObjectID(class_id='@busNumberTxt'))

                    self.finalDestination = UILabel(relative_rect=pygame.Rect((130, yAxisBusses), (400, 20)),
                                                    text='To ' +
                                                    data["finalDestination"],
                                                    manager=self.manager, object_id=ObjectID(class_id='@busfinaldesttext'))

                    self.towards = UILabel(relative_rect=pygame.Rect((130, yAxisBusses + 20), (400, 20)),
                                           text='Towards ' +
                                           data["goingTowards"],
                                           manager=self.manager, object_id=ObjectID(class_id='@busdestinationtext'))

                    self.direction = UILabel(relative_rect=pygame.Rect((130, yAxisBusses + 40), (400, 20)),
                                             text=data["direction"],
                                             manager=self.manager, object_id=ObjectID(class_id='@busdirectiontext'))

                    if data["timeToStationMins"] < 15:
                        self.line = UIPanel(relative_rect=pygame.Rect((500, yAxisBusses + 40), (300, 5)),
                                            manager=self.manager, object_id=ObjectID(class_id='@busNumber'))

                        self.stopToLine = UIPanel(relative_rect=pygame.Rect((796, yAxisBusses + 25), (5, 30)),
                                                  manager=self.manager, object_id=ObjectID(class_id='@busNumber'))

                        self.stopLabel = UILabel(relative_rect=pygame.Rect((810, yAxisBusses + 30), (100, 20)),
                                                 text='Stop',
                                                 manager=self.manager, object_id=ObjectID(class_id='@menuItemText'))

                        self.grid_image = pygame_gui.elements.UIImage(
                            relative_rect=pygame.Rect(
                                (800 - (data["timeToStationMins"] * 20) - 42, yAxisBusses - 5), (42, 46)),
                            image_surface=bus,
                            manager=self.manager,
                        )

                        self.timeToStation = UILabel(relative_rect=pygame.Rect((600, yAxisBusses + 50), (300, 20)),
                                                     text=str(data["timeToStationMins"]) +
                                                     ' minutes away',
                                                     manager=self.manager, object_id=ObjectID(class_id='@busdirectiontext'))
                    else:
                        self.timeToStation = UILabel(relative_rect=pygame.Rect((560, yAxisBusses + 20), (300, 40)),
                                                     text=str(data["timeToStationMins"]) +
                                                     ' minutes away',
                                                     manager=self.manager, object_id=ObjectID(class_id='@busstopheading'))

                    yAxisBusses += 100
            except:
                makeHome()
