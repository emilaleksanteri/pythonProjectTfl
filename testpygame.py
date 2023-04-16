import pygame_gui
import pygame
from stopTimes import StopTimes
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel
import time

# styles reference: https://pygame-gui.readthedocs.io/en/latest/theme_guide.html

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

width = 1000
height = 800
bgColor = (255, 255, 255)

pygame.init()
pygame.display.set_caption('Transport Near Hult')
window_surface = pygame.display.set_mode((width, height))
background = pygame.Surface((width, height))
background.fill(pygame.Color(bgColor))
manager = pygame_gui.UIManager((width, height), 'theme.json')

headerImgWhite = pygame.image.load('./images/TFLOGO.png')
homeBlueTFL = pygame.image.load('./images/TFLOGOBLU.png')
skyline = pygame.image.load('./images/ldnSkyline.png')

page = "home"


def clear():
    global window_surface, background, manager
    window_surface = pygame.display.set_mode((width, height))
    background = pygame.Surface((width, height))
    background.fill(pygame.Color(bgColor))
    manager = pygame_gui.UIManager((width, height), 'theme.json')


# Header

headerPanel = UIPanel(relative_rect=pygame.Rect((0, 0), (1000, 100)),
                      manager=manager, object_id=ObjectID(class_id='@headerPanel'))

transport = UIButton(relative_rect=pygame.Rect((60, 2), (250, 40)),
                     text="TRANSPORT",
                     container=headerPanel,
                     manager=manager, object_id=ObjectID(class_id='@headerText'))

forLdn = UIButton(relative_rect=pygame.Rect((60, 30), (250, 40)),
                  text="FOR LONDON",
                  container=headerPanel,
                  manager=manager, object_id=ObjectID(class_id='@headerText'))


# busses
busRoutesLbl = UILabel(relative_rect=pygame.Rect((100, 116), (250, 80)),
                       text="Bus Routes",
                       manager=manager, object_id=ObjectID(class_id='@menuHeaderLabel'))

busRoutes = UIPanel(relative_rect=pygame.Rect((48, 173), (350, 400)),
                    manager=manager, object_id=ObjectID(class_id='@outlinePanel'))

henriquesStreetBtn = UIButton(relative_rect=pygame.Rect((20, 100), (250, 27)),
                              text="• Henriques Street (Stop P)",
                              container=busRoutes,
                              manager=manager, object_id=ObjectID(class_id='@menuItemText'))

newRoadBtn = UIButton(relative_rect=pygame.Rect((20, 150), (250, 27)),
                      text="• New Road (Stop Q)",
                      container=busRoutes,
                      manager=manager, object_id=ObjectID(class_id='@menuItemText'))


aldgateEastStationBusBtn = UIButton(relative_rect=pygame.Rect((20, 200), (280, 27)),
                                    text="• Aldgate East Station (Stop E)",
                                    container=busRoutes,
                                    manager=manager, object_id=ObjectID(class_id='@menuItemText'))

altabAliParkBtn = UIButton(relative_rect=pygame.Rect((20, 250), (250, 27)),
                           text="• Altab Ali Park (Stop D)",
                           container=busRoutes,
                           manager=manager, object_id=ObjectID(class_id='@menuItemText'))

# underground
undergrndRoutesLbl = UILabel(relative_rect=pygame.Rect((645, 116), (250, 80)),
                             text="Underground",
                             manager=manager, object_id=ObjectID(class_id='@menuHeaderLabel'))

underground = UIPanel(relative_rect=pygame.Rect((600, 173), (350, 400)),
                      manager=manager, object_id=ObjectID(class_id='@outlinePanel'))

aldgateEstUnderGrndBtn = UIButton(relative_rect=pygame.Rect((20, 100), (300, 27)),
                                  text="• Aldgate East Underground Station",
                                  container=underground,
                                  manager=manager, object_id=ObjectID(class_id='@menuItemText'))

hamSmithCityBtn = UIButton(relative_rect=pygame.Rect((35, 120), (300, 27)),
                           text="Hammersmith & City",
                           container=underground,
                           manager=manager, object_id=ObjectID(class_id='@LineNameHam'))

districtBtn = UIButton(relative_rect=pygame.Rect((35, 140), (300, 27)),
                       text="District",
                       container=underground,
                       manager=manager, object_id=ObjectID(class_id='@LineNameDist'))

aldgateUnderGrndBtn = UIButton(relative_rect=pygame.Rect((20, 200), (300, 27)),
                               text="• Aldgate Underground Station",
                               container=underground,
                               manager=manager, object_id=ObjectID(class_id='@menuItemText'))

circleyBtn = UIButton(relative_rect=pygame.Rect((35, 220), (300, 27)),
                      text="Circle",
                      container=underground,
                      manager=manager, object_id=ObjectID(class_id='@LineNameCir'))

metropolitanBtn = UIButton(relative_rect=pygame.Rect((35, 240), (300, 27)),
                           text="Metropolitan",
                           container=underground,
                           manager=manager, object_id=ObjectID(class_id='@LineNameMetro'))


def generateMenu():
    clear()
    generateTopBar()

    global page, busRoutesLbl, busRoutes, henriquesStreetBtn, newRoadBtn, aldgateEastStationBusBtn, altabAliParkBtn, undergrndRoutesLbl, underground, aldgateEstUnderGrndBtn, hamSmithCityBtn, districtBtn, aldgateUnderGrndBtn, circleyBtn, metropolitanBtn
    page = "home"

    busRoutesLbl = UILabel(relative_rect=pygame.Rect((100, 116), (250, 80)),
                           text="Bus Routes",
                           manager=manager, object_id=ObjectID(class_id='@menuHeaderLabel'))

    busRoutes = UIPanel(relative_rect=pygame.Rect((48, 173), (350, 400)),
                        manager=manager, object_id=ObjectID(class_id='@outlinePanel'))

    henriquesStreetBtn = UIButton(relative_rect=pygame.Rect((20, 100), (250, 27)),
                                  text="• Henriques Street (Stop P)",
                                  container=busRoutes,
                                  manager=manager, object_id=ObjectID(class_id='@menuItemText'))

    newRoadBtn = UIButton(relative_rect=pygame.Rect((20, 150), (250, 27)),
                          text="• New Road (Stop Q)",
                          container=busRoutes,
                          manager=manager, object_id=ObjectID(class_id='@menuItemText'))

    aldgateEastStationBusBtn = UIButton(relative_rect=pygame.Rect((20, 200), (280, 27)),
                                        text="• Aldgate East Station (Stop E)",
                                        container=busRoutes,
                                        manager=manager, object_id=ObjectID(class_id='@menuItemText'))

    altabAliParkBtn = UIButton(relative_rect=pygame.Rect((20, 250), (250, 27)),
                               text="• Altab Ali Park (Stop D)",
                               container=busRoutes,
                               manager=manager, object_id=ObjectID(class_id='@menuItemText'))

    undergrndRoutesLbl = UILabel(relative_rect=pygame.Rect((645, 116), (250, 80)),
                                 text="Underground",
                                 manager=manager, object_id=ObjectID(class_id='@menuHeaderLabel'))

    underground = UIPanel(relative_rect=pygame.Rect((600, 173), (350, 400)),
                          manager=manager, object_id=ObjectID(class_id='@outlinePanel'))

    aldgateEstUnderGrndBtn = UIButton(relative_rect=pygame.Rect((20, 100), (300, 27)),
                                      text="• Aldgate East Underground Station",
                                      container=underground,
                                      manager=manager, object_id=ObjectID(class_id='@menuItemText'))

    hamSmithCityBtn = UIButton(relative_rect=pygame.Rect((35, 120), (300, 27)),
                               text="Hammersmith & City",
                               container=underground,
                               manager=manager, object_id=ObjectID(class_id='@LineNameHam'))

    districtBtn = UIButton(relative_rect=pygame.Rect((35, 140), (300, 27)),
                           text="District",
                           container=underground,
                           manager=manager, object_id=ObjectID(class_id='@LineNameDist'))

    aldgateUnderGrndBtn = UIButton(relative_rect=pygame.Rect((20, 200), (300, 27)),
                                   text="• Aldgate Underground Station",
                                   container=underground,
                                   manager=manager, object_id=ObjectID(class_id='@menuItemText'))

    circleyBtn = UIButton(relative_rect=pygame.Rect((35, 220), (300, 27)),
                          text="Circle",
                          container=underground,
                          manager=manager, object_id=ObjectID(class_id='@LineNameCir'))

    metropolitanBtn = UIButton(relative_rect=pygame.Rect((35, 240), (300, 27)),
                               text="Metropolitan",
                               container=underground,
                               manager=manager, object_id=ObjectID(class_id='@LineNameMetro'))


def generateTopBar():
    global transport, headerPanel, forLdn

    headerPanel = UIPanel(relative_rect=pygame.Rect((0, 0), (1000, 100)),
                          manager=manager, object_id=ObjectID(class_id='@headerPanel'))

    transport = UIButton(relative_rect=pygame.Rect((60, 2), (250, 40)),
                         text="TRANSPORT",
                         container=headerPanel,
                         manager=manager, object_id=ObjectID(class_id='@headerText'))

    forLdn = UIButton(relative_rect=pygame.Rect((60, 30), (250, 40)),
                      text="FOR LONDON",
                      container=headerPanel,
                      manager=manager, object_id=ObjectID(class_id='@headerText'))


def showTimesForStop(stationData, stationName, stopLetter):
    # to get back to the home screen
    global transport, page
    page = stationName.lower()
    clear()
    generateTopBar()
    getData = stationData.getStationData()
    transport = UIButton(relative_rect=pygame.Rect((50, 150), (250, 40)),
                         text="Back",
                         manager=manager, object_id=ObjectID(class_id='@backHomeText'))

    station = UILabel(relative_rect=pygame.Rect((58, 200), (250, 20)),
                      text=stationName,
                      manager=manager, object_id=ObjectID(class_id='@menuItemText'))

    stop = UILabel(relative_rect=pygame.Rect((58, 220), (250, 20)),
                   text=stopLetter,
                   manager=manager, object_id=ObjectID(class_id='@stopLetter'))

    yAxisBusses = 250
    uniqueNumbers = []
    for data in getData:
        if data["lineName"] not in uniqueNumbers:
            bus = pygame.image.load('./images/bus.png')
            uniqueNumbers.append(data["lineName"])
            busNumberContainer = UIPanel(relative_rect=pygame.Rect((58, yAxisBusses), (60, 60)),
                                         manager=manager, object_id=ObjectID(class_id='@busNumber'))

            busNumber = UILabel(relative_rect=pygame.Rect((0, 0), (30, 30)),
                                text=data["lineName"], container=busNumberContainer,
                                manager=manager, object_id=ObjectID(class_id='@busNumberTxt'))

            finalDestination = UILabel(relative_rect=pygame.Rect((130, yAxisBusses), (400, 20)),
                                       text='To ' + data["finalDestination"],
                                       manager=manager, object_id=ObjectID(class_id='@menuItemText'))

            towards = UILabel(relative_rect=pygame.Rect((130, yAxisBusses + 20), (400, 20)),
                              text='Towards ' + data["goingTowards"],
                              manager=manager, object_id=ObjectID(class_id='@menuItemText'))

            direction = UILabel(relative_rect=pygame.Rect((130, yAxisBusses + 40), (400, 20)),
                                text=data["direction"],
                                manager=manager, object_id=ObjectID(class_id='@menuItemText'))

            if data["timeToStationMins"] < 15:
                line = UIPanel(relative_rect=pygame.Rect((400, yAxisBusses + 40), (300, 5)),
                               manager=manager, object_id=ObjectID(class_id='@busNumber'))

                stopToLine = UIPanel(relative_rect=pygame.Rect((696, yAxisBusses + 25), (5, 30)),
                                     manager=manager, object_id=ObjectID(class_id='@busNumber'))

                stopLabel = UILabel(relative_rect=pygame.Rect((710, yAxisBusses + 30), (100, 20)),
                                    text='Stop',
                                    manager=manager, object_id=ObjectID(class_id='@menuItemText'))

                grid_image = pygame_gui.elements.UIImage(
                    relative_rect=pygame.Rect(
                        (700 - (data["timeToStationMins"] * 20) - 42, yAxisBusses - 5), (42, 46)),
                    image_surface=bus,
                    manager=manager,
                )

                timeToStation = UILabel(relative_rect=pygame.Rect((500, yAxisBusses + 50), (300, 20)),
                                        text=str(data["timeToStationMins"]) +
                                        ' minutes away',
                                        manager=manager, object_id=ObjectID(class_id='@menuItemText'))
            else:
                timeToStation = UILabel(relative_rect=pygame.Rect((400, yAxisBusses + 40), (300, 20)),
                                        text=str(data["timeToStationMins"]) +
                                        ' minutes away',
                                        manager=manager, object_id=ObjectID(class_id='@menuItemText'))

            yAxisBusses += 100


timer = 0
clock = pygame.time.Clock()
is_running = True
while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == transport or event.ui_element == forLdn:
                generateMenu()

            if event.ui_element == henriquesStreetBtn:
                showTimesForStop(
                    henriquesStreet, "Henriques Street", "Stop P")
                timer = time.time()

            if event.ui_element == newRoadBtn:
                showTimesForStop(
                    newRoad, "New Road", "Stop Q")
                timer = time.time()

            if event.ui_element == aldgateEastStationBusBtn:
                showTimesForStop(
                    aldgateEastStationBus, "Aldgate East Station", "Stop E")
                timer = time.time()

            if event.ui_element == altabAliParkBtn:
                showTimesForStop(
                    altabAliPark, "Altab Ali Park", "Stop D")
                timer = time.time()

        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    # draw logos on screen
    headerImg = window_surface.blit(headerImgWhite, (2, 20))

    # home page icons
    if page == "home":
        homeImgBus = window_surface.blit(homeBlueTFL, (55, 140))
        homeImgUndr = window_surface.blit(homeBlueTFL, (600, 140))
        ldnSkylineHome = window_surface.blit(skyline, (0, 600))

    elif page == "henriques street":
        end = time.time()
        # refresh screen every minute
        if int(end - timer) % 60 == 0:
            showTimesForStop(
                henriquesStreet, "Henriques Street", "Stop P")

    elif page == "new road":
        end = time.time()
        # refresh screen every minute
        if int(end - timer) % 60 == 0:
            showTimesForStop(
                newRoad, "New Road", "Stop Q")

    elif page == "aldgate east station":
        end = time.time()
        # refresh screen every minute
        if int(end - timer) % 60 == 0:
            showTimesForStop(
                aldgateEastStationBus, "Aldgate East Station", "Stop E")

    elif page == "altab ali park":
        end = time.time()
        # refresh screen every minute
        if int(end - timer) % 60 == 0:
            showTimesForStop(
                altabAliPark, "Altab Ali Park", "Stop D")

    pygame.display.update()
