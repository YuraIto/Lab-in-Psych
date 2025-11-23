#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on November 23, 2025, at 16:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Action Priming Exp'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\DELL\\OneDrive\\Desktop\\PsychoPy\\Solo Project_ Action Priming\\Action Priming Exp_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    Instruction = visual.TextStim(win=win, name='Instruction',
        text='You will be shown a video followed by partial images of objects. After which you will be given two options.\n\nSelect the option that is defining the image shown.\nPress 1 to select the left option\nPress 0 to slect the right option\n\nPress Space to Continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "writing_2" ---
    writing = visual.MovieStim(
        win, name='writing',
        filename='expvideos/writing.mp4', movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(0.5, 0.5), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    
    # --- Initialize components for Routine "write_img" ---
    writeimg = visual.ImageStim(
        win=win,
        name='writeimg', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    option1_text = visual.TextStim(win=win, name='option1_text',
        text='',
        font='Arial',
        pos=(-0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    option2_text = visual.TextStim(win=win, name='option2_text',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "walking" ---
    walkingvid = visual.MovieStim(
        win, name='walkingvid',
        filename='expvideos/walkingvideo.mp4', movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(0.5, 0.5), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    
    # --- Initialize components for Routine "walking_img" ---
    walkingimg = visual.ImageStim(
        win=win,
        name='walkingimg', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    option1_text_3 = visual.TextStim(win=win, name='option1_text_3',
        text='',
        font='Arial',
        pos=(-0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    option2_text_3 = visual.TextStim(win=win, name='option2_text_3',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "dancing" ---
    dance = visual.MovieStim(
        win, name='dance',
        filename='expvideos/dancing.mp4', movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(0.5, 0.5), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    
    # --- Initialize components for Routine "dance_img" ---
    danceimg = visual.ImageStim(
        win=win,
        name='danceimg', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    option1_text_2 = visual.TextStim(win=win, name='option1_text_2',
        text='',
        font='Arial',
        pos=(-0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    option2_text_2 = visual.TextStim(win=win, name='option2_text_2',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "Handswing" ---
    handswinging = visual.MovieStim(
        win, name='handswinging',
        filename='expvideos/handswing.mp4', movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(0.5, 0.5), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    
    # --- Initialize components for Routine "handswing_img" ---
    handswingimg = visual.ImageStim(
        win=win,
        name='handswingimg', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    option1_text_4 = visual.TextStim(win=win, name='option1_text_4',
        text='',
        font='Arial',
        pos=(-0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    option2_text_4 = visual.TextStim(win=win, name='option2_text_4',
        text='',
        font='Arial',
        pos=(0.3, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    
    # --- Initialize components for Routine "Bye" ---
    thanks = visual.TextStim(win=win, name='thanks',
        text='Thank you for participating!!!\n\nPress Space to Exit',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[Instruction, key_resp_3],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    thisExp.addData('Welcome.started', Welcome.tStart)
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instruction* updates
        
        # if Instruction is starting this frame...
        if Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instruction.frameNStart = frameN  # exact frame index
            Instruction.tStart = t  # local t and not account for scr refresh
            Instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instruction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instruction.started')
            # update status
            Instruction.status = STARTED
            Instruction.setAutoDraw(True)
        
        # if Instruction is active this frame...
        if Instruction.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Welcome.stopped', Welcome.tStop)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    main_loop = data.TrialHandler2(
        name='main_loop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(main_loop)  # add the loop to the experiment
    thisMain_loop = main_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop:
            globals()[paramName] = thisMain_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMain_loop in main_loop:
        currentLoop = main_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
        if thisMain_loop != None:
            for paramName in thisMain_loop:
                globals()[paramName] = thisMain_loop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        trial1_loop = data.TrialHandler2(
            name='trial1_loop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(trial1_loop)  # add the loop to the experiment
        thisTrial1_loop = trial1_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial1_loop.rgb)
        if thisTrial1_loop != None:
            for paramName in thisTrial1_loop:
                globals()[paramName] = thisTrial1_loop[paramName]
        
        for thisTrial1_loop in trial1_loop:
            currentLoop = trial1_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisTrial1_loop.rgb)
            if thisTrial1_loop != None:
                for paramName in thisTrial1_loop:
                    globals()[paramName] = thisTrial1_loop[paramName]
            
            # --- Prepare to start Routine "writing_2" ---
            # create an object to store info about Routine writing_2
            writing_2 = data.Routine(
                name='writing_2',
                components=[writing],
            )
            writing_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for writing_2
            writing_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            writing_2.tStart = globalClock.getTime(format='float')
            writing_2.status = STARTED
            thisExp.addData('writing_2.started', writing_2.tStart)
            writing_2.maxDuration = None
            # keep track of which components have finished
            writing_2Components = writing_2.components
            for thisComponent in writing_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "writing_2" ---
            # if trial has changed, end Routine now
            if isinstance(trial1_loop, data.TrialHandler2) and thisTrial1_loop.thisN != trial1_loop.thisTrial.thisN:
                continueRoutine = False
            writing_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 15.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *writing* updates
                
                # if writing is starting this frame...
                if writing.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    writing.frameNStart = frameN  # exact frame index
                    writing.tStart = t  # local t and not account for scr refresh
                    writing.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(writing, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'writing.started')
                    # update status
                    writing.status = STARTED
                    writing.setAutoDraw(True)
                    writing.play()
                
                # if writing is stopping this frame...
                if writing.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > writing.tStartRefresh + 15-frameTolerance or writing.isFinished:
                        # keep track of stop time/frame for later
                        writing.tStop = t  # not accounting for scr refresh
                        writing.tStopRefresh = tThisFlipGlobal  # on global time
                        writing.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'writing.stopped')
                        # update status
                        writing.status = FINISHED
                        writing.setAutoDraw(False)
                        writing.stop()
                if writing.isFinished:  # force-end the Routine
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[writing]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    writing_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in writing_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "writing_2" ---
            for thisComponent in writing_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for writing_2
            writing_2.tStop = globalClock.getTime(format='float')
            writing_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('writing_2.stopped', writing_2.tStop)
            writing.stop()  # ensure movie has stopped at end of Routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if writing_2.maxDurationReached:
                routineTimer.addTime(-writing_2.maxDuration)
            elif writing_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-15.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials = data.TrialHandler2(
                name='trials',
                nReps=1.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions('Instructional files/writing_trial.xlsx'), 
                seed=None, 
            )
            thisExp.addLoop(trials)  # add the loop to the experiment
            thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTrial in trials:
                currentLoop = trials
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
                if thisTrial != None:
                    for paramName in thisTrial:
                        globals()[paramName] = thisTrial[paramName]
                
                # --- Prepare to start Routine "write_img" ---
                # create an object to store info about Routine write_img
                write_img = data.Routine(
                    name='write_img',
                    components=[writeimg, option1_text, option2_text, key_resp],
                )
                write_img.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                writeimg.setImage(imagefile)
                option1_text.setText(option1)
                option2_text.setText(option2)
                # create starting attributes for key_resp
                key_resp.keys = []
                key_resp.rt = []
                _key_resp_allKeys = []
                # store start times for write_img
                write_img.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                write_img.tStart = globalClock.getTime(format='float')
                write_img.status = STARTED
                thisExp.addData('write_img.started', write_img.tStart)
                write_img.maxDuration = None
                # keep track of which components have finished
                write_imgComponents = write_img.components
                for thisComponent in write_img.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "write_img" ---
                # if trial has changed, end Routine now
                if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                    continueRoutine = False
                write_img.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *writeimg* updates
                    
                    # if writeimg is starting this frame...
                    if writeimg.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                        # keep track of start time/frame for later
                        writeimg.frameNStart = frameN  # exact frame index
                        writeimg.tStart = t  # local t and not account for scr refresh
                        writeimg.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(writeimg, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'writeimg.started')
                        # update status
                        writeimg.status = STARTED
                        writeimg.setAutoDraw(True)
                    
                    # if writeimg is active this frame...
                    if writeimg.status == STARTED:
                        # update params
                        pass
                    
                    # if writeimg is stopping this frame...
                    if writeimg.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > writeimg.tStartRefresh + 0.3-frameTolerance:
                            # keep track of stop time/frame for later
                            writeimg.tStop = t  # not accounting for scr refresh
                            writeimg.tStopRefresh = tThisFlipGlobal  # on global time
                            writeimg.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'writeimg.stopped')
                            # update status
                            writeimg.status = FINISHED
                            writeimg.setAutoDraw(False)
                    
                    # *option1_text* updates
                    
                    # if option1_text is starting this frame...
                    if option1_text.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                        # keep track of start time/frame for later
                        option1_text.frameNStart = frameN  # exact frame index
                        option1_text.tStart = t  # local t and not account for scr refresh
                        option1_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(option1_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'option1_text.started')
                        # update status
                        option1_text.status = STARTED
                        option1_text.setAutoDraw(True)
                    
                    # if option1_text is active this frame...
                    if option1_text.status == STARTED:
                        # update params
                        pass
                    
                    # *option2_text* updates
                    
                    # if option2_text is starting this frame...
                    if option2_text.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                        # keep track of start time/frame for later
                        option2_text.frameNStart = frameN  # exact frame index
                        option2_text.tStart = t  # local t and not account for scr refresh
                        option2_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(option2_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'option2_text.started')
                        # update status
                        option2_text.status = STARTED
                        option2_text.setAutoDraw(True)
                    
                    # if option2_text is active this frame...
                    if option2_text.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp* updates
                    waitOnFlip = False
                    
                    # if key_resp is starting this frame...
                    if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp.frameNStart = frameN  # exact frame index
                        key_resp.tStart = t  # local t and not account for scr refresh
                        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp.started')
                        # update status
                        key_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp.getKeys(keyList=['1','0'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_allKeys.extend(theseKeys)
                        if len(_key_resp_allKeys):
                            key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                            key_resp.rt = _key_resp_allKeys[0].rt
                            key_resp.duration = _key_resp_allKeys[0].duration
                            # was this correct?
                            if (key_resp.keys == str(corr_res)) or (key_resp.keys == corr_res):
                                key_resp.corr = 1
                            else:
                                key_resp.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        write_img.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in write_img.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "write_img" ---
                for thisComponent in write_img.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for write_img
                write_img.tStop = globalClock.getTime(format='float')
                write_img.tStopRefresh = tThisFlipGlobal
                thisExp.addData('write_img.stopped', write_img.tStop)
                # check responses
                if key_resp.keys in ['', [], None]:  # No response was made
                    key_resp.keys = None
                    # was no response the correct answer?!
                    if str(corr_res).lower() == 'none':
                       key_resp.corr = 1;  # correct non-response
                    else:
                       key_resp.corr = 0;  # failed to respond (incorrectly)
                # store data for trials (TrialHandler)
                trials.addData('key_resp.keys',key_resp.keys)
                trials.addData('key_resp.corr', key_resp.corr)
                if key_resp.keys != None:  # we had a response
                    trials.addData('key_resp.rt', key_resp.rt)
                    trials.addData('key_resp.duration', key_resp.duration)
                # the Routine "write_img" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'trials'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trial1_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        trials3_loop = data.TrialHandler2(
            name='trials3_loop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(trials3_loop)  # add the loop to the experiment
        thisTrials3_loop = trials3_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials3_loop.rgb)
        if thisTrials3_loop != None:
            for paramName in thisTrials3_loop:
                globals()[paramName] = thisTrials3_loop[paramName]
        
        for thisTrials3_loop in trials3_loop:
            currentLoop = trials3_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisTrials3_loop.rgb)
            if thisTrials3_loop != None:
                for paramName in thisTrials3_loop:
                    globals()[paramName] = thisTrials3_loop[paramName]
            
            # --- Prepare to start Routine "walking" ---
            # create an object to store info about Routine walking
            walking = data.Routine(
                name='walking',
                components=[walkingvid],
            )
            walking.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for walking
            walking.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            walking.tStart = globalClock.getTime(format='float')
            walking.status = STARTED
            thisExp.addData('walking.started', walking.tStart)
            walking.maxDuration = None
            # keep track of which components have finished
            walkingComponents = walking.components
            for thisComponent in walking.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "walking" ---
            # if trial has changed, end Routine now
            if isinstance(trials3_loop, data.TrialHandler2) and thisTrials3_loop.thisN != trials3_loop.thisTrial.thisN:
                continueRoutine = False
            walking.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 16.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *walkingvid* updates
                
                # if walkingvid is starting this frame...
                if walkingvid.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                    # keep track of start time/frame for later
                    walkingvid.frameNStart = frameN  # exact frame index
                    walkingvid.tStart = t  # local t and not account for scr refresh
                    walkingvid.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(walkingvid, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'walkingvid.started')
                    # update status
                    walkingvid.status = STARTED
                    walkingvid.setAutoDraw(True)
                    walkingvid.play()
                
                # if walkingvid is stopping this frame...
                if walkingvid.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > walkingvid.tStartRefresh + 15-frameTolerance or walkingvid.isFinished:
                        # keep track of stop time/frame for later
                        walkingvid.tStop = t  # not accounting for scr refresh
                        walkingvid.tStopRefresh = tThisFlipGlobal  # on global time
                        walkingvid.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'walkingvid.stopped')
                        # update status
                        walkingvid.status = FINISHED
                        walkingvid.setAutoDraw(False)
                        walkingvid.stop()
                if walkingvid.isFinished:  # force-end the Routine
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[walkingvid]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    walking.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in walking.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "walking" ---
            for thisComponent in walking.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for walking
            walking.tStop = globalClock.getTime(format='float')
            walking.tStopRefresh = tThisFlipGlobal
            thisExp.addData('walking.stopped', walking.tStop)
            walkingvid.stop()  # ensure movie has stopped at end of Routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if walking.maxDurationReached:
                routineTimer.addTime(-walking.maxDuration)
            elif walking.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-16.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_3 = data.TrialHandler2(
                name='trials_3',
                nReps=1.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions('Instructional files/walking_trial.xlsx'), 
                seed=None, 
            )
            thisExp.addLoop(trials_3)  # add the loop to the experiment
            thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    globals()[paramName] = thisTrial_3[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTrial_3 in trials_3:
                currentLoop = trials_3
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
                if thisTrial_3 != None:
                    for paramName in thisTrial_3:
                        globals()[paramName] = thisTrial_3[paramName]
                
                # --- Prepare to start Routine "walking_img" ---
                # create an object to store info about Routine walking_img
                walking_img = data.Routine(
                    name='walking_img',
                    components=[walkingimg, option1_text_3, option2_text_3, key_resp_4],
                )
                walking_img.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                walkingimg.setImage(imagefile)
                option1_text_3.setText(option1)
                option2_text_3.setText(option2)
                # create starting attributes for key_resp_4
                key_resp_4.keys = []
                key_resp_4.rt = []
                _key_resp_4_allKeys = []
                # store start times for walking_img
                walking_img.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                walking_img.tStart = globalClock.getTime(format='float')
                walking_img.status = STARTED
                thisExp.addData('walking_img.started', walking_img.tStart)
                walking_img.maxDuration = None
                # keep track of which components have finished
                walking_imgComponents = walking_img.components
                for thisComponent in walking_img.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "walking_img" ---
                # if trial has changed, end Routine now
                if isinstance(trials_3, data.TrialHandler2) and thisTrial_3.thisN != trials_3.thisTrial.thisN:
                    continueRoutine = False
                walking_img.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *walkingimg* updates
                    
                    # if walkingimg is starting this frame...
                    if walkingimg.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                        # keep track of start time/frame for later
                        walkingimg.frameNStart = frameN  # exact frame index
                        walkingimg.tStart = t  # local t and not account for scr refresh
                        walkingimg.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(walkingimg, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'walkingimg.started')
                        # update status
                        walkingimg.status = STARTED
                        walkingimg.setAutoDraw(True)
                    
                    # if walkingimg is active this frame...
                    if walkingimg.status == STARTED:
                        # update params
                        pass
                    
                    # if walkingimg is stopping this frame...
                    if walkingimg.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > walkingimg.tStartRefresh + 0.3-frameTolerance:
                            # keep track of stop time/frame for later
                            walkingimg.tStop = t  # not accounting for scr refresh
                            walkingimg.tStopRefresh = tThisFlipGlobal  # on global time
                            walkingimg.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'walkingimg.stopped')
                            # update status
                            walkingimg.status = FINISHED
                            walkingimg.setAutoDraw(False)
                    
                    # *option1_text_3* updates
                    
                    # if option1_text_3 is starting this frame...
                    if option1_text_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                        # keep track of start time/frame for later
                        option1_text_3.frameNStart = frameN  # exact frame index
                        option1_text_3.tStart = t  # local t and not account for scr refresh
                        option1_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(option1_text_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'option1_text_3.started')
                        # update status
                        option1_text_3.status = STARTED
                        option1_text_3.setAutoDraw(True)
                    
                    # if option1_text_3 is active this frame...
                    if option1_text_3.status == STARTED:
                        # update params
                        pass
                    
                    # *option2_text_3* updates
                    
                    # if option2_text_3 is starting this frame...
                    if option2_text_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                        # keep track of start time/frame for later
                        option2_text_3.frameNStart = frameN  # exact frame index
                        option2_text_3.tStart = t  # local t and not account for scr refresh
                        option2_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(option2_text_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'option2_text_3.started')
                        # update status
                        option2_text_3.status = STARTED
                        option2_text_3.setAutoDraw(True)
                    
                    # if option2_text_3 is active this frame...
                    if option2_text_3.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_4* updates
                    waitOnFlip = False
                    
                    # if key_resp_4 is starting this frame...
                    if key_resp_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_4.frameNStart = frameN  # exact frame index
                        key_resp_4.tStart = t  # local t and not account for scr refresh
                        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_4.started')
                        # update status
                        key_resp_4.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_4.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_4.getKeys(keyList=['1','0'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_4_allKeys.extend(theseKeys)
                        if len(_key_resp_4_allKeys):
                            key_resp_4.keys = _key_resp_4_allKeys[0].name  # just the first key pressed
                            key_resp_4.rt = _key_resp_4_allKeys[0].rt
                            key_resp_4.duration = _key_resp_4_allKeys[0].duration
                            # was this correct?
                            if (key_resp_4.keys == str(corr_res)) or (key_resp_4.keys == corr_res):
                                key_resp_4.corr = 1
                            else:
                                key_resp_4.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        walking_img.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in walking_img.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "walking_img" ---
                for thisComponent in walking_img.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for walking_img
                walking_img.tStop = globalClock.getTime(format='float')
                walking_img.tStopRefresh = tThisFlipGlobal
                thisExp.addData('walking_img.stopped', walking_img.tStop)
                # check responses
                if key_resp_4.keys in ['', [], None]:  # No response was made
                    key_resp_4.keys = None
                    # was no response the correct answer?!
                    if str(corr_res).lower() == 'none':
                       key_resp_4.corr = 1;  # correct non-response
                    else:
                       key_resp_4.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_3 (TrialHandler)
                trials_3.addData('key_resp_4.keys',key_resp_4.keys)
                trials_3.addData('key_resp_4.corr', key_resp_4.corr)
                if key_resp_4.keys != None:  # we had a response
                    trials_3.addData('key_resp_4.rt', key_resp_4.rt)
                    trials_3.addData('key_resp_4.duration', key_resp_4.duration)
                # the Routine "walking_img" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'trials_3'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials3_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        trial2_loop = data.TrialHandler2(
            name='trial2_loop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(trial2_loop)  # add the loop to the experiment
        thisTrial2_loop = trial2_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial2_loop.rgb)
        if thisTrial2_loop != None:
            for paramName in thisTrial2_loop:
                globals()[paramName] = thisTrial2_loop[paramName]
        
        for thisTrial2_loop in trial2_loop:
            currentLoop = trial2_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisTrial2_loop.rgb)
            if thisTrial2_loop != None:
                for paramName in thisTrial2_loop:
                    globals()[paramName] = thisTrial2_loop[paramName]
            
            # --- Prepare to start Routine "dancing" ---
            # create an object to store info about Routine dancing
            dancing = data.Routine(
                name='dancing',
                components=[dance],
            )
            dancing.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for dancing
            dancing.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            dancing.tStart = globalClock.getTime(format='float')
            dancing.status = STARTED
            thisExp.addData('dancing.started', dancing.tStart)
            dancing.maxDuration = None
            # keep track of which components have finished
            dancingComponents = dancing.components
            for thisComponent in dancing.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "dancing" ---
            # if trial has changed, end Routine now
            if isinstance(trial2_loop, data.TrialHandler2) and thisTrial2_loop.thisN != trial2_loop.thisTrial.thisN:
                continueRoutine = False
            dancing.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 16.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *dance* updates
                
                # if dance is starting this frame...
                if dance.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                    # keep track of start time/frame for later
                    dance.frameNStart = frameN  # exact frame index
                    dance.tStart = t  # local t and not account for scr refresh
                    dance.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dance, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dance.started')
                    # update status
                    dance.status = STARTED
                    dance.setAutoDraw(True)
                    dance.play()
                
                # if dance is stopping this frame...
                if dance.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dance.tStartRefresh + 15-frameTolerance or dance.isFinished:
                        # keep track of stop time/frame for later
                        dance.tStop = t  # not accounting for scr refresh
                        dance.tStopRefresh = tThisFlipGlobal  # on global time
                        dance.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dance.stopped')
                        # update status
                        dance.status = FINISHED
                        dance.setAutoDraw(False)
                        dance.stop()
                if dance.isFinished:  # force-end the Routine
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[dance]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    dancing.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in dancing.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "dancing" ---
            for thisComponent in dancing.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for dancing
            dancing.tStop = globalClock.getTime(format='float')
            dancing.tStopRefresh = tThisFlipGlobal
            thisExp.addData('dancing.stopped', dancing.tStop)
            dance.stop()  # ensure movie has stopped at end of Routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if dancing.maxDurationReached:
                routineTimer.addTime(-dancing.maxDuration)
            elif dancing.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-16.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_2 = data.TrialHandler2(
                name='trials_2',
                nReps=1.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions('Instructional files/dance_trial.xlsx'), 
                seed=None, 
            )
            thisExp.addLoop(trials_2)  # add the loop to the experiment
            thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTrial_2 in trials_2:
                currentLoop = trials_2
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
                if thisTrial_2 != None:
                    for paramName in thisTrial_2:
                        globals()[paramName] = thisTrial_2[paramName]
                
                # --- Prepare to start Routine "dance_img" ---
                # create an object to store info about Routine dance_img
                dance_img = data.Routine(
                    name='dance_img',
                    components=[danceimg, option1_text_2, option2_text_2, key_resp_2],
                )
                dance_img.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                danceimg.setImage(imagefile)
                option1_text_2.setText(option1)
                option2_text_2.setText(option2)
                # create starting attributes for key_resp_2
                key_resp_2.keys = []
                key_resp_2.rt = []
                _key_resp_2_allKeys = []
                # store start times for dance_img
                dance_img.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                dance_img.tStart = globalClock.getTime(format='float')
                dance_img.status = STARTED
                thisExp.addData('dance_img.started', dance_img.tStart)
                dance_img.maxDuration = None
                # keep track of which components have finished
                dance_imgComponents = dance_img.components
                for thisComponent in dance_img.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "dance_img" ---
                # if trial has changed, end Routine now
                if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
                    continueRoutine = False
                dance_img.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *danceimg* updates
                    
                    # if danceimg is starting this frame...
                    if danceimg.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                        # keep track of start time/frame for later
                        danceimg.frameNStart = frameN  # exact frame index
                        danceimg.tStart = t  # local t and not account for scr refresh
                        danceimg.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(danceimg, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'danceimg.started')
                        # update status
                        danceimg.status = STARTED
                        danceimg.setAutoDraw(True)
                    
                    # if danceimg is active this frame...
                    if danceimg.status == STARTED:
                        # update params
                        pass
                    
                    # if danceimg is stopping this frame...
                    if danceimg.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > danceimg.tStartRefresh + 0.3-frameTolerance:
                            # keep track of stop time/frame for later
                            danceimg.tStop = t  # not accounting for scr refresh
                            danceimg.tStopRefresh = tThisFlipGlobal  # on global time
                            danceimg.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'danceimg.stopped')
                            # update status
                            danceimg.status = FINISHED
                            danceimg.setAutoDraw(False)
                    
                    # *option1_text_2* updates
                    
                    # if option1_text_2 is starting this frame...
                    if option1_text_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                        # keep track of start time/frame for later
                        option1_text_2.frameNStart = frameN  # exact frame index
                        option1_text_2.tStart = t  # local t and not account for scr refresh
                        option1_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(option1_text_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'option1_text_2.started')
                        # update status
                        option1_text_2.status = STARTED
                        option1_text_2.setAutoDraw(True)
                    
                    # if option1_text_2 is active this frame...
                    if option1_text_2.status == STARTED:
                        # update params
                        pass
                    
                    # *option2_text_2* updates
                    
                    # if option2_text_2 is starting this frame...
                    if option2_text_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                        # keep track of start time/frame for later
                        option2_text_2.frameNStart = frameN  # exact frame index
                        option2_text_2.tStart = t  # local t and not account for scr refresh
                        option2_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(option2_text_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'option2_text_2.started')
                        # update status
                        option2_text_2.status = STARTED
                        option2_text_2.setAutoDraw(True)
                    
                    # if option2_text_2 is active this frame...
                    if option2_text_2.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_2* updates
                    waitOnFlip = False
                    
                    # if key_resp_2 is starting this frame...
                    if key_resp_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_2.frameNStart = frameN  # exact frame index
                        key_resp_2.tStart = t  # local t and not account for scr refresh
                        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_2.started')
                        # update status
                        key_resp_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_2.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_2.getKeys(keyList=['1','0'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_2_allKeys.extend(theseKeys)
                        if len(_key_resp_2_allKeys):
                            key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                            key_resp_2.rt = _key_resp_2_allKeys[0].rt
                            key_resp_2.duration = _key_resp_2_allKeys[0].duration
                            # was this correct?
                            if (key_resp_2.keys == str(corr_res)) or (key_resp_2.keys == corr_res):
                                key_resp_2.corr = 1
                            else:
                                key_resp_2.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        dance_img.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in dance_img.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "dance_img" ---
                for thisComponent in dance_img.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for dance_img
                dance_img.tStop = globalClock.getTime(format='float')
                dance_img.tStopRefresh = tThisFlipGlobal
                thisExp.addData('dance_img.stopped', dance_img.tStop)
                # check responses
                if key_resp_2.keys in ['', [], None]:  # No response was made
                    key_resp_2.keys = None
                    # was no response the correct answer?!
                    if str(corr_res).lower() == 'none':
                       key_resp_2.corr = 1;  # correct non-response
                    else:
                       key_resp_2.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_2 (TrialHandler)
                trials_2.addData('key_resp_2.keys',key_resp_2.keys)
                trials_2.addData('key_resp_2.corr', key_resp_2.corr)
                if key_resp_2.keys != None:  # we had a response
                    trials_2.addData('key_resp_2.rt', key_resp_2.rt)
                    trials_2.addData('key_resp_2.duration', key_resp_2.duration)
                # the Routine "dance_img" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'trials_2'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trial2_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        trials4_loop = data.TrialHandler2(
            name='trials4_loop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(trials4_loop)  # add the loop to the experiment
        thisTrials4_loop = trials4_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrials4_loop.rgb)
        if thisTrials4_loop != None:
            for paramName in thisTrials4_loop:
                globals()[paramName] = thisTrials4_loop[paramName]
        
        for thisTrials4_loop in trials4_loop:
            currentLoop = trials4_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisTrials4_loop.rgb)
            if thisTrials4_loop != None:
                for paramName in thisTrials4_loop:
                    globals()[paramName] = thisTrials4_loop[paramName]
            
            # --- Prepare to start Routine "Handswing" ---
            # create an object to store info about Routine Handswing
            Handswing = data.Routine(
                name='Handswing',
                components=[handswinging],
            )
            Handswing.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for Handswing
            Handswing.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Handswing.tStart = globalClock.getTime(format='float')
            Handswing.status = STARTED
            thisExp.addData('Handswing.started', Handswing.tStart)
            Handswing.maxDuration = None
            # keep track of which components have finished
            HandswingComponents = Handswing.components
            for thisComponent in Handswing.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Handswing" ---
            # if trial has changed, end Routine now
            if isinstance(trials4_loop, data.TrialHandler2) and thisTrials4_loop.thisN != trials4_loop.thisTrial.thisN:
                continueRoutine = False
            Handswing.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 16.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *handswinging* updates
                
                # if handswinging is starting this frame...
                if handswinging.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                    # keep track of start time/frame for later
                    handswinging.frameNStart = frameN  # exact frame index
                    handswinging.tStart = t  # local t and not account for scr refresh
                    handswinging.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(handswinging, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'handswinging.started')
                    # update status
                    handswinging.status = STARTED
                    handswinging.setAutoDraw(True)
                    handswinging.play()
                
                # if handswinging is stopping this frame...
                if handswinging.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > handswinging.tStartRefresh + 15-frameTolerance or handswinging.isFinished:
                        # keep track of stop time/frame for later
                        handswinging.tStop = t  # not accounting for scr refresh
                        handswinging.tStopRefresh = tThisFlipGlobal  # on global time
                        handswinging.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'handswinging.stopped')
                        # update status
                        handswinging.status = FINISHED
                        handswinging.setAutoDraw(False)
                        handswinging.stop()
                if handswinging.isFinished:  # force-end the Routine
                    continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[handswinging]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Handswing.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Handswing.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Handswing" ---
            for thisComponent in Handswing.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Handswing
            Handswing.tStop = globalClock.getTime(format='float')
            Handswing.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Handswing.stopped', Handswing.tStop)
            handswinging.stop()  # ensure movie has stopped at end of Routine
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Handswing.maxDurationReached:
                routineTimer.addTime(-Handswing.maxDuration)
            elif Handswing.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-16.000000)
            
            # set up handler to look after randomisation of conditions etc
            trials_4 = data.TrialHandler2(
                name='trials_4',
                nReps=1.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions('Instructional files/handswing_trial.xlsx'), 
                seed=None, 
            )
            thisExp.addLoop(trials_4)  # add the loop to the experiment
            thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    globals()[paramName] = thisTrial_4[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTrial_4 in trials_4:
                currentLoop = trials_4
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
                if thisTrial_4 != None:
                    for paramName in thisTrial_4:
                        globals()[paramName] = thisTrial_4[paramName]
                
                # --- Prepare to start Routine "handswing_img" ---
                # create an object to store info about Routine handswing_img
                handswing_img = data.Routine(
                    name='handswing_img',
                    components=[handswingimg, option1_text_4, option2_text_4, key_resp_5],
                )
                handswing_img.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                handswingimg.setImage(imagefile)
                option1_text_4.setText(option1)
                option2_text_4.setText(option2)
                # create starting attributes for key_resp_5
                key_resp_5.keys = []
                key_resp_5.rt = []
                _key_resp_5_allKeys = []
                # store start times for handswing_img
                handswing_img.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                handswing_img.tStart = globalClock.getTime(format='float')
                handswing_img.status = STARTED
                thisExp.addData('handswing_img.started', handswing_img.tStart)
                handswing_img.maxDuration = None
                # keep track of which components have finished
                handswing_imgComponents = handswing_img.components
                for thisComponent in handswing_img.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "handswing_img" ---
                # if trial has changed, end Routine now
                if isinstance(trials_4, data.TrialHandler2) and thisTrial_4.thisN != trials_4.thisTrial.thisN:
                    continueRoutine = False
                handswing_img.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *handswingimg* updates
                    
                    # if handswingimg is starting this frame...
                    if handswingimg.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                        # keep track of start time/frame for later
                        handswingimg.frameNStart = frameN  # exact frame index
                        handswingimg.tStart = t  # local t and not account for scr refresh
                        handswingimg.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(handswingimg, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'handswingimg.started')
                        # update status
                        handswingimg.status = STARTED
                        handswingimg.setAutoDraw(True)
                    
                    # if handswingimg is active this frame...
                    if handswingimg.status == STARTED:
                        # update params
                        pass
                    
                    # if handswingimg is stopping this frame...
                    if handswingimg.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > handswingimg.tStartRefresh + 0.3-frameTolerance:
                            # keep track of stop time/frame for later
                            handswingimg.tStop = t  # not accounting for scr refresh
                            handswingimg.tStopRefresh = tThisFlipGlobal  # on global time
                            handswingimg.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'handswingimg.stopped')
                            # update status
                            handswingimg.status = FINISHED
                            handswingimg.setAutoDraw(False)
                    
                    # *option1_text_4* updates
                    
                    # if option1_text_4 is starting this frame...
                    if option1_text_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                        # keep track of start time/frame for later
                        option1_text_4.frameNStart = frameN  # exact frame index
                        option1_text_4.tStart = t  # local t and not account for scr refresh
                        option1_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(option1_text_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'option1_text_4.started')
                        # update status
                        option1_text_4.status = STARTED
                        option1_text_4.setAutoDraw(True)
                    
                    # if option1_text_4 is active this frame...
                    if option1_text_4.status == STARTED:
                        # update params
                        pass
                    
                    # *option2_text_4* updates
                    
                    # if option2_text_4 is starting this frame...
                    if option2_text_4.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                        # keep track of start time/frame for later
                        option2_text_4.frameNStart = frameN  # exact frame index
                        option2_text_4.tStart = t  # local t and not account for scr refresh
                        option2_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(option2_text_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'option2_text_4.started')
                        # update status
                        option2_text_4.status = STARTED
                        option2_text_4.setAutoDraw(True)
                    
                    # if option2_text_4 is active this frame...
                    if option2_text_4.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_5* updates
                    waitOnFlip = False
                    
                    # if key_resp_5 is starting this frame...
                    if key_resp_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_5.frameNStart = frameN  # exact frame index
                        key_resp_5.tStart = t  # local t and not account for scr refresh
                        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_5.started')
                        # update status
                        key_resp_5.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_5.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_5.getKeys(keyList=['1','0'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_5_allKeys.extend(theseKeys)
                        if len(_key_resp_5_allKeys):
                            key_resp_5.keys = _key_resp_5_allKeys[0].name  # just the first key pressed
                            key_resp_5.rt = _key_resp_5_allKeys[0].rt
                            key_resp_5.duration = _key_resp_5_allKeys[0].duration
                            # was this correct?
                            if (key_resp_5.keys == str(corr_res)) or (key_resp_5.keys == corr_res):
                                key_resp_5.corr = 1
                            else:
                                key_resp_5.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        handswing_img.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in handswing_img.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "handswing_img" ---
                for thisComponent in handswing_img.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for handswing_img
                handswing_img.tStop = globalClock.getTime(format='float')
                handswing_img.tStopRefresh = tThisFlipGlobal
                thisExp.addData('handswing_img.stopped', handswing_img.tStop)
                # check responses
                if key_resp_5.keys in ['', [], None]:  # No response was made
                    key_resp_5.keys = None
                    # was no response the correct answer?!
                    if str(corr_res).lower() == 'none':
                       key_resp_5.corr = 1;  # correct non-response
                    else:
                       key_resp_5.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_4 (TrialHandler)
                trials_4.addData('key_resp_5.keys',key_resp_5.keys)
                trials_4.addData('key_resp_5.corr', key_resp_5.corr)
                if key_resp_5.keys != None:  # we had a response
                    trials_4.addData('key_resp_5.rt', key_resp_5.rt)
                    trials_4.addData('key_resp_5.duration', key_resp_5.duration)
                # the Routine "handswing_img" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'trials_4'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials4_loop'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'main_loop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Bye" ---
    # create an object to store info about Routine Bye
    Bye = data.Routine(
        name='Bye',
        components=[thanks, key_resp_6],
    )
    Bye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_6
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # store start times for Bye
    Bye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Bye.tStart = globalClock.getTime(format='float')
    Bye.status = STARTED
    thisExp.addData('Bye.started', Bye.tStart)
    Bye.maxDuration = None
    # keep track of which components have finished
    ByeComponents = Bye.components
    for thisComponent in Bye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Bye" ---
    Bye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thanks* updates
        
        # if thanks is starting this frame...
        if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thanks.frameNStart = frameN  # exact frame index
            thanks.tStart = t  # local t and not account for scr refresh
            thanks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks.started')
            # update status
            thanks.status = STARTED
            thanks.setAutoDraw(True)
        
        # if thanks is active this frame...
        if thanks.status == STARTED:
            # update params
            pass
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Bye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Bye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Bye" ---
    for thisComponent in Bye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Bye
    Bye.tStop = globalClock.getTime(format='float')
    Bye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Bye.stopped', Bye.tStop)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "Bye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
