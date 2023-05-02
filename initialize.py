import pygame_gui
import pygame
from stopTimes import StopTimes
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel


class Initialize:
    def __init__(self, manager):
        self.page = "home"
        self.manager = manager
        # Header

        self.headerPanel = UIPanel(relative_rect=pygame.Rect((0, 0), (1000, 100)),
                                   manager=self.manager, object_id=ObjectID(class_id='@headerPanel'))

        self.transport = UIButton(relative_rect=pygame.Rect((60, 2), (250, 40)),
                                  text="TRANSPORT",
                                  container=self.headerPanel,
                                  manager=self.manager, object_id=ObjectID(class_id='@headerText'))

        self.forLdn = UIButton(relative_rect=pygame.Rect((60, 30), (250, 40)),
                               text="FOR LONDON",
                               container=self.headerPanel,
                               manager=self.manager, object_id=ObjectID(class_id='@headerText'))

        # -------------------BUSES
        self.busRoutesLbl = UILabel(relative_rect=pygame.Rect((100, 116), (250, 80)),
                                    text="Bus Routes",
                                    manager=self.manager, object_id=ObjectID(class_id='@menuHeaderLabel'))

        self.busRoutes = UIPanel(relative_rect=pygame.Rect((48, 173), (350, 400)),
                                 manager=self.manager, object_id=ObjectID(class_id='@outlinePanel'))

        self.henriquesStreetBtn = UIButton(relative_rect=pygame.Rect((20, 100), (250, 27)),
                                           text="Henriques Street (Stop P)",
                                           container=self.busRoutes,
                                           manager=self.manager, object_id=ObjectID(class_id='@menuItemText'))

        self.newRoadBtn = UIButton(relative_rect=pygame.Rect((20, 150), (250, 27)),
                                   text="New Road (Stop Q)",
                                   container=self.busRoutes,
                                   manager=self.manager, object_id=ObjectID(class_id='@menuItemText'))

        self.aldgateEastStationBusBtn = UIButton(relative_rect=pygame.Rect((20, 200), (280, 27)),
                                                 text="Aldgate East Station (Stop E)",
                                                 container=self.busRoutes,
                                                 manager=self.manager, object_id=ObjectID(class_id='@menuItemText'))

        self.altabAliParkBtn = UIButton(relative_rect=pygame.Rect((20, 250), (250, 27)),
                                        text="Altab Ali Park (Stop D)",
                                        container=self.busRoutes,
                                        manager=self.manager, object_id=ObjectID(class_id='@menuItemText'))

        # -------------------UNDERGROUND
        self.undergrndRoutesLbl = UILabel(relative_rect=pygame.Rect((645, 116), (250, 80)),
                                          text="Underground",
                                          manager=self.manager, object_id=ObjectID(class_id='@menuHeaderLabel'))

        self.underground = UIPanel(relative_rect=pygame.Rect((600, 173), (350, 400)),
                                   manager=self.manager, object_id=ObjectID(class_id='@outlinePanel'))

        self.aldgateEstUnderGrndBtn = UILabel(relative_rect=pygame.Rect((20, 100), (300, 30)),
                                              text="Aldgate East Underground Station",
                                              container=self.underground,
                                              manager=self.manager, object_id=ObjectID(class_id='@menuItemText'))

        self.hamSmithCityBtn = UIButton(relative_rect=pygame.Rect((35, 130), (300, 30)),
                                        text="Hammersmith & City",
                                        container=self.underground,
                                        manager=self.manager, object_id=ObjectID(class_id='@LineNameHam'))

        self.districtBtn = UIButton(relative_rect=pygame.Rect((35, 160), (300, 30)),
                                    text="District",
                                    container=self.underground,
                                    manager=self.manager, object_id=ObjectID(class_id='@LineNameDist'))

        self.aldgateUnderGrndBtn = UILabel(relative_rect=pygame.Rect((20, 200), (300, 30)),
                                           text="Aldgate Underground Station",
                                           container=self.underground,
                                           manager=self.manager, object_id=ObjectID(class_id='@menuItemText'))

        self.circleyBtn = UIButton(relative_rect=pygame.Rect((35, 230), (300, 30)),
                                   text="Circle",
                                   container=self.underground,
                                   manager=self.manager, object_id=ObjectID(class_id='@LineNameCir'))

    # make menu element on top of screen
    def generateTopBar(self, manager):

        self.headerPanel = UIPanel(relative_rect=pygame.Rect((0, 0), (1000, 100)),
                                   manager=manager, object_id=ObjectID(class_id='@headerPanel'))

        self.transport = UIButton(relative_rect=pygame.Rect((60, 2), (250, 40)),
                                  text="TRANSPORT",
                                  container=self.headerPanel,
                                  manager=manager, object_id=ObjectID(class_id='@headerText'))

        self.forLdn = UIButton(relative_rect=pygame.Rect((60, 30), (250, 40)),
                               text="FOR LONDON",
                               container=self.headerPanel,
                               manager=manager, object_id=ObjectID(class_id='@headerText'))

    def generateMenu(self, manager):
        self.generateTopBar(manager)

        self.page = "home"

        # -------------------BUSES
        self.busRoutesLbl = UILabel(relative_rect=pygame.Rect((100, 116), (250, 80)),
                                    text="Bus Routes",
                                    manager=manager, object_id=ObjectID(class_id='@menuHeaderLabel'))

        self.busRoutes = UIPanel(relative_rect=pygame.Rect((48, 173), (350, 400)),
                                 manager=manager, object_id=ObjectID(class_id='@outlinePanel'))

        self.henriquesStreetBtn = UIButton(relative_rect=pygame.Rect((20, 100), (250, 27)),
                                           text="Henriques Street (Stop P)",
                                           container=self.busRoutes,
                                           manager=manager, object_id=ObjectID(class_id='@menuItemText'))

        self.newRoadBtn = UIButton(relative_rect=pygame.Rect((20, 150), (250, 27)),
                                   text="New Road (Stop Q)",
                                   container=self.busRoutes,
                                   manager=manager, object_id=ObjectID(class_id='@menuItemText'))

        self.aldgateEastStationBusBtn = UIButton(relative_rect=pygame.Rect((20, 200), (280, 27)),
                                                 text="Aldgate East Station (Stop E)",
                                                 container=self.busRoutes,
                                                 manager=manager, object_id=ObjectID(class_id='@menuItemText'))

        self.altabAliParkBtn = UIButton(relative_rect=pygame.Rect((20, 250), (250, 27)),
                                        text="Altab Ali Park (Stop D)",
                                        container=self.busRoutes,
                                        manager=manager, object_id=ObjectID(class_id='@menuItemText'))

        # -------------------UNDERGROUND
        self.undergrndRoutesLbl = UILabel(relative_rect=pygame.Rect((645, 116), (250, 80)),
                                          text="Underground",
                                          manager=manager, object_id=ObjectID(class_id='@menuHeaderLabel'))

        self.underground = UIPanel(relative_rect=pygame.Rect((600, 173), (350, 400)),
                                   manager=manager, object_id=ObjectID(class_id='@outlinePanel'))

        self.aldgateEstUnderGrndBtn = UILabel(relative_rect=pygame.Rect((20, 100), (300, 30)),
                                              text="Aldgate East Underground Station",
                                              container=self.underground,
                                              manager=manager, object_id=ObjectID(class_id='@menuItemText'))

        self.hamSmithCityBtn = UIButton(relative_rect=pygame.Rect((35, 130), (300, 30)),
                                        text="Hammersmith & City",
                                        container=self.underground,
                                        manager=manager, object_id=ObjectID(class_id='@LineNameHam'))

        self.districtBtn = UIButton(relative_rect=pygame.Rect((35, 160), (300, 30)),
                                    text="District",
                                    container=self.underground,
                                    manager=manager, object_id=ObjectID(class_id='@LineNameDist'))

        self.aldgateUnderGrndBtn = UILabel(relative_rect=pygame.Rect((20, 200), (300, 30)),
                                           text="Aldgate Underground Station",
                                           container=self.underground,
                                           manager=manager, object_id=ObjectID(class_id='@menuItemText'))

        self.circleyBtn = UIButton(relative_rect=pygame.Rect((35, 230), (300, 30)),
                                   text="Circle",
                                   container=self.underground,
                                   manager=manager, object_id=ObjectID(class_id='@LineNameCir'))
