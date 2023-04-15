import pygame_gui
import pygame
from stopTimes import StopTimes

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

width = 1200
height = 800

pygame.init()
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((width, height))
background = pygame.Surface((width, height))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((width, height))


def clear():
    global window_surface, background, manager
    window_surface = pygame.display.set_mode((width, height))
    background = pygame.Surface((width, height))
    background.fill(pygame.Color('#000000'))
    manager = pygame_gui.UIManager((width, height))


mainBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (1200, 80)),
                                       text="Menu",
                                       manager=manager)

henriquesStreetBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 80), (1200, 80)),
                                                  text="Henriques Street (Stop P) x mins away",
                                                  manager=manager)

newRoadBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 160), (1200, 80)),
                                          text="New Road (Stop Q) x mins away",
                                          manager=manager)

aldgateEastStationBusBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 240), (1200, 80)),
                                                        text="Aldgate East Station (Stop E) x mins away",
                                                        manager=manager)


altabAliParkBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 320), (1200, 80)),
                                               text="Altab Ali Park (Stop D) x mins away",
                                               manager=manager)

aldgateEastUndergroundBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 400), (1200, 80)),
                                                         text="Aldgate East Underground x mins away",
                                                         manager=manager)


def generateMenu():
    clear()
    global mainBtn, henriquesStreetBtn, newRoadBtn, aldgateEastStationBusBtn, altabAliParkBtn, aldgateEastUndergroundBtn

    mainBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (1200, 80)),
                                           text="Menu",
                                           manager=manager)

    henriquesStreetBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 80), (1200, 80)),
                                                      text="Henriques Street (Stop P) x mins away",
                                                      manager=manager)

    newRoadBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 160), (1200, 80)),
                                              text="New Road (Stop Q) x mins away",
                                              manager=manager)

    aldgateEastStationBusBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 240), (1200, 80)),
                                                            text="Aldgate East Station (Stop E) x mins away",
                                                            manager=manager)

    altabAliParkBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 320), (1200, 80)),
                                                   text="Altab Ali Park (Stop D) x mins away",
                                                   manager=manager)

    aldgateEastUndergroundBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 400), (1200, 80)),
                                                             text="Aldgate East Underground x mins away",
                                                             manager=manager)


def generateTopBar():
    global mainBtn, henriquesStreetBtn, newRoadBtn, aldgateEastStationBusBtn, altabAliParkBtn, aldgateEastUndergroundBtn

    mainBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (200, 80)),
                                           text="Menu",
                                           manager=manager)

    henriquesStreetBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 0), (200, 80)),
                                                      text="Henriques Street",
                                                      manager=manager)

    newRoadBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 0), (200, 80)),
                                              text="New Road",
                                              manager=manager)

    aldgateEastStationBusBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 0), (200, 80)),
                                                            text="Aldgate East Station",
                                                            manager=manager)

    altabAliParkBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 0), (200, 80)),
                                                   text="Altab Ali Park",
                                                   manager=manager)

    aldgateEastUndergroundBtn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 0), (200, 80)),
                                                             text="A.E Underground",
                                                             manager=manager)


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
                                          + 'Station Name: ' +
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
            if event.ui_element == mainBtn:
                generateMenu()

            if event.ui_element == henriquesStreetBtn:
                showTimesForStop(henriquesStreet, "Henriques Street (Stop P)")

            if event.ui_element == newRoadBtn:
                showTimesForStop(newRoad, "New Road (Stop Q)")

            if event.ui_element == aldgateEastStationBusBtn:
                showTimesForStop(aldgateEastStationBus,
                                 "Aldgate East Station (Stop E)")

            if event.ui_element == altabAliParkBtn:
                showTimesForStop(altabAliPark, "Altab Ali Park (Stop D)")

            if event.ui_element == aldgateEastUndergroundBtn:
                showTimesForStop(aldgateEastUnderground,
                                 "Aldgate East Underground")

        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()
