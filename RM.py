# -*- coding: utf-8 -*-
"""

"""
####NOTE THAT THE GAME HAS TO BE SET NOT TO USE RAW MOUSE INPUT

#Imports*****************
import win32api
import win32con
import time

#Inputs*****************
rounds_per_minute = 620.0   #Weapon RPM
scalar = 0.25               #Scales the recoil vectors. Test that it seems good in-game.

#Recoil vectors dependent on weapon spread shots (symthick.com)
#Recoil for SCAR-H with Heavy barrel+Ergo/Vertical grip
recoil = [137,79,75,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74]

#Initiate variables*****************
a=0
count = 0
recoil_return = []

#General calculations*****************
time_between_shots = (1./((rounds_per_minute+2.)/60.))  #Used for frequency of mouse movements. Slightly higher than actual weapon rpm so that it will always move BEFORE the shot is made, not after (numerics)

for i in range(1,len(recoil)+1):
   recoil_return.append(sum(recoil[0:i]))

recoil = [scalar*x for x in recoil]                     #Scales the recoil to something that works in-game
recoil_return = [scalar*x for x in recoil_return]       #Scales the recoil to something that works in-game
recoil = [int(x) for x in recoil]                       #Makes the displacements to integers
recoil_return = [int(x) for x in recoil_return]         #Makes the displacements to integers

#Infinity loop
while True:
    #Check button press
    a=win32api.GetAsyncKeyState(win32con.VK_LBUTTON)

    #While button is pressed
    while a != 0:
        time.sleep(1./((rounds_per_minute+2.)/60.))             #Start with waiting for first bullet to be fired
        x_current, y_current = win32api.GetCursorPos()          #Checks current cursor position
        y = y_current+recoil[count]                             #Moves the current mouse position with distance dictated by numbers of loop-runs
        win32api.SetCursorPos((x_current,y))                    #Set new position, do not change x-coordinate (lateral)
        count = count + 1                                       #Increase count by 1
        a=win32api.GetAsyncKeyState(win32con.VK_LBUTTON)        #Check if button is pressed

        #If button is not pressed anymore
        if a == 0:
            y_return = y - recoil_return[count]                 #Distance to move cursor up
            win32api.SetCursorPos((x_current,y_return))         #Moves cursor up from the last set position. No movement assumed to occur between setting location and this command.
            count = 0                                           #Resets counter

    time.sleep(1./((1000.*2.+2.))/60.)                      #Checks LMB button at Nyquist frequency +2 (CPU saving). Assumes mouse pulling = 1000 Hz