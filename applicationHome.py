import pygame_gui
import pygame
from stopTimes import StopTimes
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIPanel, UIButton, UILabel
import time
from initialize import Initialize
from pageFunctions import Pages

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
aldgateUnderground = StopTimes("940GZZLUALD")


width = 1000
height = 800
bgColor = (255, 255, 255)

pygame.init()
pygame.display.set_caption('Transport Near Hult')
programIcon = pygame.image.load('./images/logo.ico')
pygame.display.set_icon(programIcon)
window_surface = pygame.display.set_mode((width, height))
background = pygame.Surface((width, height))
background.fill(pygame.Color(bgColor))
manager = pygame_gui.UIManager((width, height), 'theme.json')

headerImgWhite = pygame.image.load('./images/TFLOGO.png')
homeBlueTFL = pygame.image.load('./images/TFLOGOBLU.png')
skyline = pygame.image.load('./images/ldnSkyline.png')

# initialize home
home = Initialize(manager)
pages = Pages(manager)

# remake home screen


def makeHome():
    clear()
    home.generateMenu(manager)


# clear screen
def clear():
    global window_surface, background, manager
    window_surface = pygame.display.set_mode((width, height))
    background = pygame.Surface((width, height))
    background.fill(pygame.Color(bgColor))
    manager = pygame_gui.UIManager((width, height), 'theme.json')


timer = 0
clock = pygame.time.Clock()
is_running = True
while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == home.transport or event.ui_element == home.forLdn:
                makeHome()
# -------BUSES EVENTS
            if event.ui_element == home.henriquesStreetBtn:
                clear()
                pages.showTimesForStop(
                    henriquesStreet, "Henriques Street", "Stop P", manager, home, makeHome)
                timer = time.time()

            if event.ui_element == home.newRoadBtn:
                clear()
                pages.showTimesForStop(
                    newRoad, "New Road", "Stop Q", manager, home, makeHome)
                timer = time.time()

            if event.ui_element == home.aldgateEastStationBusBtn:
                clear()
                pages.showTimesForStop(
                    aldgateEastStationBus, "Aldgate East Station", "Stop E", manager, home, makeHome)
                timer = time.time()

            if event.ui_element == home.altabAliParkBtn:
                clear()
                pages.showTimesForStop(
                    altabAliPark, "Altab Ali Park", "Stop D", manager, home, makeHome)
                timer = time.time()
# -------UNDERGROUND EVENTS
            if event.ui_element == home.hamSmithCityBtn:
                clear()
                pages.showTimesUnderground(
                    aldgateEastUnderground, "Hammersmith & City", "Aldgate East Underground Station", manager, home, makeHome)
                timer = time.time()

            if event.ui_element == home.districtBtn:
                clear()
                pages.showTimesUnderground(
                    aldgateEastUnderground, "District", "Aldgate East Underground Station", manager, home, makeHome)
                timer = time.time()

            if event.ui_element == home.circleyBtn:
                clear()
                pages.showTimesUnderground(
                    aldgateUnderground, "Circle", "Aldgate Underground Station", manager, home, makeHome)
                timer = time.time()

    manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    # draw logos on screen
    headerImg = window_surface.blit(headerImgWhite, (10, 20))

    # home page icons
    if home.page == "home":
        homeImgBus = window_surface.blit(homeBlueTFL, (55, 140))
        homeImgUndr = window_surface.blit(homeBlueTFL, (600, 140))
        ldnSkylineHome = window_surface.blit(skyline, (0, 600))

    # update bus times every 60 seconds
    elif home.page == "henriques street":
        end = time.time()
        # refresh screen every minute
        if int(end - timer) % 60 == 0:
            clear()
            pages.showTimesForStop(
                henriquesStreet, "Henriques Street", "Stop P", manager, home, makeHome)

    elif home.page == "new road":
        end = time.time()
        # refresh screen every minute
        if int(end - timer) % 60 == 0:
            clear()
            pages.showTimesForStop(
                newRoad, "New Road", "Stop Q", manager, home, makeHome)

    elif home.page == "aldgate east station":
        end = time.time()
        # refresh screen every minute
        if int(end - timer) % 60 == 0:
            clear()
            pages.showTimesForStop(
                aldgateEastStationBus, "Aldgate East Station", "Stop E", manager, home, makeHome)

    elif home.page == "altab ali park":
        end = time.time()
        # refresh screen every minute
        if int(end - timer) % 60 == 0:
            clear()
            pages.showTimesForStop(
                altabAliPark, "Altab Ali Park", "Stop D", manager, home, makeHome)

    elif home.page == "hammersmith & city":
        end = time.time()

        if int(end - timer) % 60 == 0:
            clear()
            pages.showTimesUnderground(
                aldgateEastUnderground, "Hammersmith & City", "Aldgate East Underground Station", manager, home, makeHome)

    elif home.page == "district":
        end = time.time()

        if int(end - timer) % 60 == 0:
            clear()
            pages.showTimesUnderground(
                aldgateEastUnderground, "District", "Aldgate East Underground Station", manager, home, makeHome)

    elif home.page == "circle":
        end = time.time()

        if int(end - timer) % 60 == 0:
            clear()
            pages.showTimesUnderground(
                aldgateUnderground, "Circle", "Aldgate Underground Station", manager, home, makeHome)

    pygame.display.update()
