import pygame_gui
import pygame
from stopTimes import StopTimes
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel

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
bgColor = (245, 247, 246)

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


def showTimesForStop(stationData, stationName):
    clear()
    generateTopBar()
    getData = stationData.getStationData()
    row = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 80), (1200, 40)),
                                       text=stationName,
                                       manager=manager)
    yPos = 120
    for data in getData:
        row = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, yPos), (1200, 40)),
                                          text='Line Name: ' +
                                          data["lineName"] + ' '
                                          + 'Platform: ' +
                                          data["platFormName"] + ' '
                                          + 'Directiom: ' +
                                          data["direction"] + ' '
                                          + 'Towards: ' +
                                          data["goingTowards"] + ' '
                                          + 'Final Destination: ' +
                                          data["finalDestination"] + ' '
                                          + 'At stop in: ' +
                                          str(data["timeToStationMins"]) +
                                          ' mins ',
                                          manager=manager)
        yPos += 40


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

    pygame.display.update()
