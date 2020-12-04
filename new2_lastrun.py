#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on Fri 27 Nov 2020 02:46:34 PM +0330
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.5'
expName = 'new2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/mnt/dc4b6596-70ce-42c3-b140-9e846e1f49e6/Documents/Semester 4/FalseNewsEmotion/new2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "code_positions"
code_positionsClock = core.Clock()
# set_positions()
# Positions used during the experiment
# Position variables end with _p.
def set_positions():
  global share_p # position of the share icon.
  global like_p # position of the like icon.
  global dislike_p # position of the dislike icon.
  global next_p # position of the next icon.
  global text_p #position of the text news
  global rate_p #position of the rating scale
  global rate_text_p #position of the rating description
  
  delta_x, delta_y = win.size/4
  quarter_centers = [ [-delta_x, +delta_y], [+delta_x, +delta_y], [+delta_x, -delta_y], [-delta_x, -delta_y] ] 
    #centers when window is quartered.
  half_centers = [ [0 , +delta_y], [0, -delta_y] ] #centers when window is halved.
  
  #rate_dist = win.size[1]/50
  #rate_centers = np.array([0, rate_dist])
  text_p = half_centers[0]
  rate_p = half_centers[1]
  rate_text_p = (0 , -0.1)
  
  icon_dist = win.size[0]/9
  icon_centers = np.array([icon_dist, 0])
  dislike_p = np.array( quarter_centers[3] ) + icon_centers
  next_p = np.array( quarter_centers[2]) + icon_centers
  like_p = np.array( quarter_centers[3]) - icon_centers
  share_p = np.array( quarter_centers[2]) - icon_centers
  
# set_sizes()
# Sizes used during the experiment
# Size variables end with _s.
def set_sizes():
    global image_frame_s #size of the image frame
    global image_s #size of the image stimuli 
    global text_frame_s #size of the text frame  
    global text_s #size of the image statements
    global icon_s #size of the icons
    
    screen_size = np.array( win.size )
    image_frame_s = (np.array( [ win.size[0]/2, win.size[1]/2 ] ))* 0.95
    image_s = (image_frame_s) * 0.95
    text_frame_s = np.array( [ win.size[0], win.size[1]/2 ] ) * 0.95
    text_s = (text_frame_s) 
    icon_s = np.array( [ win.size[0]/8, win.size[1]/4 ] )
    
set_positions()
set_sizes()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text='توضیحات و سلام',
    font='Nazli',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);

# Initialize components for Routine "prime_valence"
prime_valenceClock = core.Clock()
import pandas as pd
from numpy.random import choice

pic_choice = choice(5, size=3, replace=False)

image_blocks = ['NegBlock.csv', 'NeuBlock.csv', 'PosBlock.csv']
np.random.shuffle(image_blocks) # randomise order


stim_frame_valence = visual.Rect(
    win=win, name='stim_frame_valence',units='pix', 
    width=image_frame_s[0], height=image_frame_s[1],
    ori=0, pos=text_p,
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
stim_image_valence = visual.ImageStim(
    win=win, name='stim_image_valence',units='pix', 
    image='sin', mask=None,
    ori=0, pos=text_p, size=image_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
valence_rating = visual.RatingScale(win=win, name='valence_rating', marker='triangle', size=1.0, low=-4, high=4, labels=[''], scale='')
scale_message = visual.TextStim(win=win, name='scale_message',
    text='احساس شما نسبت به این تصویر چگونه است؟',
    font='Nazli',
    pos=rate_text_p, height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-4.0);

# Initialize components for Routine "blank_valence"
blank_valenceClock = core.Clock()
blank_frame = visual.Rect(
    win=win, name='blank_frame',units='pix', 
    width=(1366, 768)[0], height=(1366, 768)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "statement_selection_code"
statement_selection_codeClock = core.Clock()
import random
block_num = 3
statement_per_block = 4
#sample_num = int((block_num*statement_per_block)/2)
request_num = int(statement_per_block/2)

news = pd.read_csv("news-statements.csv") 

news["displayed_yet"] = 0
not_displayed_news = news.loc[news["displayed_yet"]== 0] #creating a new dataframe
overall_selected_statements = {}
#np.zeros((block_num , statement_per_block), dtype = str)
for i in range(block_num):
    not_displayed_news = news.loc[news["displayed_yet"]== 0]
    selected_statements = not_displayed_news.groupby("Accuracy").sample(n= request_num)
    selected_ids = selected_statements.index
    news.at[selected_ids,"displayed_yet"] = 1
    print(news)
    #selected_statements_array = np.array(selected_statements["Statements"])
    #selected_statements_array = np.random.permutation(selected_statements_array)
    #overall_selected_statements[i] = selected_statements_array
    selected_statements_list = list(selected_ids)
    random.shuffle(selected_statements_list)
    print(selected_statements_list)
    overall_selected_statements[i] = selected_statements_list
    
    


# Initialize components for Routine "statement_interaction"
statement_interactionClock = core.Clock()
text_frame = visual.Rect(
    win=win, name='text_frame',units='pix', 
    width=text_frame_s[0], height=text_frame_s[1],
    ori=0, pos=text_p,
    lineWidth=10, lineColor='black', lineColorSpace='rgb',
    fillColor='gray', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
statement_image = visual.ImageStim(
    win=win, name='statement_image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=text_p, size=text_frame_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
next_image = visual.ImageStim(
    win=win, name='next_image',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=next_p, size=icon_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
share_image = visual.ImageStim(
    win=win, name='share_image',units='pix', 
    image='noun_share.png', mask=None,
    ori=0, pos=share_p, size=icon_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
like_image = visual.ImageStim(
    win=win, name='like_image',units='pix', 
    image='noun_like.png', mask=None,
    ori=0, pos=like_p, size=icon_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
dislike_image = visual.ImageStim(
    win=win, name='dislike_image',units='pix', 
    image='noun_Dislike.png', mask=None,
    ori=0, pos=dislike_p, size=icon_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response = event.Mouse(win=win)
x, y = [None, None]
response.mouseClock = core.Clock()

# Initialize components for Routine "rest_question"
rest_questionClock = core.Clock()

inputText = ""
question_text = visual.TextStim(win=win, name='question_text',
    text='default text',
    font='Nazli',
    pos=[-0.5, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "description1"
description1Clock = core.Clock()
description_next_phase = visual.TextStim(win=win, name='description_next_phase',
    text='توضیحات',
    font='Nazli',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);

# Initialize components for Routine "prime_arousal"
prime_arousalClock = core.Clock()
image_blocks = ['NegBlock.csv', 'NeuBlock.csv', 'PosBlock.csv']
np.random.shuffle(image_blocks) # randomise order
stim_frame_arousal = visual.Rect(
    win=win, name='stim_frame_arousal',units='pix', 
    width=image_frame_s[0], height=image_frame_s[1],
    ori=0, pos=text_p,
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
stim_image_arousal = visual.ImageStim(
    win=win, name='stim_image_arousal',units='pix', 
    image='sin', mask=None,
    ori=0, pos=text_p, size=image_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
arousal_rating = visual.RatingScale(win=win, name='arousal_rating', marker='triangle', size=1.0, low=1, high=7, labels=[''], scale='')
scale_message2 = visual.TextStim(win=win, name='scale_message2',
    text='انگیختگی شما نسبت به این تصویر چگونه است؟',
    font='Nazli',
    pos=rate_text_p, height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-4.0);

# Initialize components for Routine "blank_arousal"
blank_arousalClock = core.Clock()
blank_frame2 = visual.Rect(
    win=win, name='blank_frame2',units='pix', 
    width=(1366, 768)[0], height=(1366, 768)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "statement_accuracy"
statement_accuracyClock = core.Clock()
text_frame2 = visual.Rect(
    win=win, name='text_frame2',units='pix', 
    width=text_frame_s[0], height=text_frame_s[1],
    ori=0, pos=text_p,
    lineWidth=5, lineColor='black', lineColorSpace='rgb',
    fillColor='gray', fillColorSpace='rgb',
    opacity=10, depth=0.0, interpolate=True)
statement_image2 = visual.ImageStim(
    win=win, name='statement_image2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=text_p, size=text_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
validity_rating = visual.RatingScale(win=win, name='validity_rating', marker='triangle', size=1.0, low=1, high=7, labels=[''], scale='')
scale_message3 = visual.TextStim(win=win, name='scale_message3',
    text='تا چه میزان از صحت و اعتبار این متن اطمینان دارید؟',
    font='Nazli',
    pos=rate_text_p, height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-3.0);

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
thanks_text = visual.TextStim(win=win, name='thanks_text',
    text='دست شما درد نکنه',
    font='Nazli',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "code_positions"-------
t = 0
code_positionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat


# keep track of which components have finished
code_positionsComponents = []
for thisComponent in code_positionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "code_positions"-------
while continueRoutine:
    # get current time
    t = code_positionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in code_positionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "code_positions"-------
for thisComponent in code_positionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# the Routine "code_positions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
welcome_key = event.BuilderKeyResponse()
# keep track of which components have finished
WelcomeComponents = [welcome_text, welcome_key]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if t >= 0.0 and welcome_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_text.tStart = t  # not accounting for scr refresh
        welcome_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_key* updates
    if t >= 0.0 and welcome_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_key.tStart = t  # not accounting for scr refresh
        welcome_key.frameNStart = frameN  # exact frame index
        win.timeOnFlip(welcome_key, 'tStartRefresh')  # time at next scr refresh
        welcome_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if welcome_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcome_text.started', welcome_text.tStartRefresh)
thisExp.addData('welcome_text.stopped', welcome_text.tStopRefresh)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
conditionSelectLoop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('chooseBlocks.csv'),
    seed=None, name='conditionSelectLoop')
thisExp.addLoop(conditionSelectLoop)  # add the loop to the experiment
thisConditionSelectLoop = conditionSelectLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConditionSelectLoop.rgb)
if thisConditionSelectLoop != None:
    for paramName in thisConditionSelectLoop:
        exec('{} = thisConditionSelectLoop[paramName]'.format(paramName))

for thisConditionSelectLoop in conditionSelectLoop:
    currentLoop = conditionSelectLoop
    # abbreviate parameter names if possible (e.g. rgb = thisConditionSelectLoop.rgb)
    if thisConditionSelectLoop != None:
        for paramName in thisConditionSelectLoop:
            exec('{} = thisConditionSelectLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(thisConditionSelectLoop['condsFile'], selection=pic_choice ),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "prime_valence"-------
            t = 0
            prime_valenceClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            #if conditionSelectLoop.thisN == 0:
            #    shuffle(image_blocks)
            stim_image_valence.setImage(stimFile)
            valence_rating.reset()
            # keep track of which components have finished
            prime_valenceComponents = [stim_frame_valence, stim_image_valence, valence_rating, scale_message]
            for thisComponent in prime_valenceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "prime_valence"-------
            while continueRoutine:
                # get current time
                t = prime_valenceClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *stim_frame_valence* updates
                if t >= 0.0 and stim_frame_valence.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stim_frame_valence.tStart = t  # not accounting for scr refresh
                    stim_frame_valence.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(stim_frame_valence, 'tStartRefresh')  # time at next scr refresh
                    stim_frame_valence.setAutoDraw(True)
                
                # *stim_image_valence* updates
                if t >= 0.0 and stim_image_valence.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stim_image_valence.tStart = t  # not accounting for scr refresh
                    stim_image_valence.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(stim_image_valence, 'tStartRefresh')  # time at next scr refresh
                    stim_image_valence.setAutoDraw(True)
                # *valence_rating* updates
                if t >= 0.0 and valence_rating.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    valence_rating.tStart = t  # not accounting for scr refresh
                    valence_rating.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(valence_rating, 'tStartRefresh')  # time at next scr refresh
                    valence_rating.setAutoDraw(True)
                continueRoutine &= valence_rating.noResponse  # a response ends the trial
                
                # *scale_message* updates
                if t >= 0.0 and scale_message.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    scale_message.tStart = t  # not accounting for scr refresh
                    scale_message.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(scale_message, 'tStartRefresh')  # time at next scr refresh
                    scale_message.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in prime_valenceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "prime_valence"-------
            for thisComponent in prime_valenceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            trials.addData('stim_frame_valence.started', stim_frame_valence.tStartRefresh)
            trials.addData('stim_frame_valence.stopped', stim_frame_valence.tStopRefresh)
            trials.addData('stim_image_valence.started', stim_image_valence.tStartRefresh)
            trials.addData('stim_image_valence.stopped', stim_image_valence.tStopRefresh)
            # store data for trials (TrialHandler)
            trials.addData('valence_rating.response', valence_rating.getRating())
            trials.addData('valence_rating.rt', valence_rating.getRT())
            trials.addData('valence_rating.started', valence_rating.tStart)
            trials.addData('valence_rating.stopped', valence_rating.tStop)
            trials.addData('scale_message.started', scale_message.tStartRefresh)
            trials.addData('scale_message.stopped', scale_message.tStopRefresh)
            # the Routine "prime_valence" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "blank_valence"-------
            t = 0
            blank_valenceClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.250000)
            # update component parameters for each repeat
            # keep track of which components have finished
            blank_valenceComponents = [blank_frame]
            for thisComponent in blank_valenceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "blank_valence"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = blank_valenceClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_frame* updates
                if t >= 0 and blank_frame.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    blank_frame.tStart = t  # not accounting for scr refresh
                    blank_frame.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(blank_frame, 'tStartRefresh')  # time at next scr refresh
                    blank_frame.setAutoDraw(True)
                frameRemains = 0 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
                if blank_frame.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    blank_frame.tStop = t  # not accounting for scr refresh
                    blank_frame.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank_frame, 'tStopRefresh')  # time at next scr refresh
                    blank_frame.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blank_valenceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "blank_valence"-------
            for thisComponent in blank_valenceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('blank_frame.started', blank_frame.tStartRefresh)
            trials.addData('blank_frame.stopped', blank_frame.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('news-statements.csv', selection=overall_selected_statements[conditionSelectLoop.thisN][(blocks.thisN *( statement_per_block)): ((blocks.thisN + 1) * ( statement_per_block))]),
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    exec('{} = thisTrial_2[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "statement_selection_code"-------
            t = 0
            statement_selection_codeClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            
            # keep track of which components have finished
            statement_selection_codeComponents = []
            for thisComponent in statement_selection_codeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "statement_selection_code"-------
            while continueRoutine:
                # get current time
                t = statement_selection_codeClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in statement_selection_codeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "statement_selection_code"-------
            for thisComponent in statement_selection_codeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # the Routine "statement_selection_code" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "statement_interaction"-------
            t = 0
            statement_interactionClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            statement_image.setImage(Statements)
            # setup some python lists for storing info about the response
            response.x = []
            response.y = []
            response.leftButton = []
            response.midButton = []
            response.rightButton = []
            response.time = []
            response.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            statement_interactionComponents = [text_frame, statement_image, next_image, share_image, like_image, dislike_image, response]
            for thisComponent in statement_interactionComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "statement_interaction"-------
            while continueRoutine:
                # get current time
                t = statement_interactionClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_frame* updates
                if t >= 0.0 and text_frame.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_frame.tStart = t  # not accounting for scr refresh
                    text_frame.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(text_frame, 'tStartRefresh')  # time at next scr refresh
                    text_frame.setAutoDraw(True)
                
                # *statement_image* updates
                if t >= 0.0 and statement_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    statement_image.tStart = t  # not accounting for scr refresh
                    statement_image.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(statement_image, 'tStartRefresh')  # time at next scr refresh
                    statement_image.setAutoDraw(True)
                
                # *next_image* updates
                if t >= 0.0 and next_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    next_image.tStart = t  # not accounting for scr refresh
                    next_image.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(next_image, 'tStartRefresh')  # time at next scr refresh
                    next_image.setAutoDraw(True)
                
                # *share_image* updates
                if t >= 0.0 and share_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    share_image.tStart = t  # not accounting for scr refresh
                    share_image.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(share_image, 'tStartRefresh')  # time at next scr refresh
                    share_image.setAutoDraw(True)
                
                # *like_image* updates
                if t >= 0.0 and like_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    like_image.tStart = t  # not accounting for scr refresh
                    like_image.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(like_image, 'tStartRefresh')  # time at next scr refresh
                    like_image.setAutoDraw(True)
                
                # *dislike_image* updates
                if t >= 0.0 and dislike_image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    dislike_image.tStart = t  # not accounting for scr refresh
                    dislike_image.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(dislike_image, 'tStartRefresh')  # time at next scr refresh
                    dislike_image.setAutoDraw(True)
                # *response* updates
                if t >= 0.0 and response.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    response.tStart = t  # not accounting for scr refresh
                    response.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                    response.status = STARTED
                    response.mouseClock.reset()
                    prevButtonState = response.getPressed()  # if button is down already this ISN'T a new click
                if response.status == STARTED:  # only update if started and not finished!
                    buttons = response.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            for obj in [like_image,share_image,dislike_image,next_image]:
                                if obj.contains(response):
                                    gotValidClick = True
                                    response.clicked_name.append(obj.name)
                            x, y = response.getPos()
                            response.x.append(x)
                            response.y.append(y)
                            buttons = response.getPressed()
                            response.leftButton.append(buttons[0])
                            response.midButton.append(buttons[1])
                            response.rightButton.append(buttons[2])
                            response.time.append(response.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in statement_interactionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "statement_interaction"-------
            for thisComponent in statement_interactionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_2.addData('text_frame.started', text_frame.tStartRefresh)
            trials_2.addData('text_frame.stopped', text_frame.tStopRefresh)
            trials_2.addData('statement_image.started', statement_image.tStartRefresh)
            trials_2.addData('statement_image.stopped', statement_image.tStopRefresh)
            trials_2.addData('next_image.started', next_image.tStartRefresh)
            trials_2.addData('next_image.stopped', next_image.tStopRefresh)
            trials_2.addData('share_image.started', share_image.tStartRefresh)
            trials_2.addData('share_image.stopped', share_image.tStopRefresh)
            trials_2.addData('like_image.started', like_image.tStartRefresh)
            trials_2.addData('like_image.stopped', like_image.tStopRefresh)
            trials_2.addData('dislike_image.started', dislike_image.tStartRefresh)
            trials_2.addData('dislike_image.stopped', dislike_image.tStopRefresh)
            # store data for trials_2 (TrialHandler)
            if len(response.x): trials_2.addData('response.x', response.x[0])
            if len(response.y): trials_2.addData('response.y', response.y[0])
            if len(response.leftButton): trials_2.addData('response.leftButton', response.leftButton[0])
            if len(response.midButton): trials_2.addData('response.midButton', response.midButton[0])
            if len(response.rightButton): trials_2.addData('response.rightButton', response.rightButton[0])
            if len(response.time): trials_2.addData('response.time', response.time[0])
            if len(response.clicked_name): trials_2.addData('response.clicked_name', response.clicked_name[0])
            trials_2.addData('response.started', response.tStart)
            trials_2.addData('response.stopped', response.tStop)
            # the Routine "statement_interaction" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_2'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(QuestionFiles, selection='0:3'),
            seed=None, name='trials_3')
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        for thisTrial_3 in trials_3:
            currentLoop = trials_3
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    exec('{} = thisTrial_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "rest_question"-------
            t = 0
            rest_questionClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            
            theseKeys=""
            shift_flag = False
            question_text.alignHoriz ='left'
            answers = event.BuilderKeyResponse()
            # keep track of which components have finished
            rest_questionComponents = [question_text, answers]
            for thisComponent in rest_questionComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "rest_question"-------
            while continueRoutine:
                # get current time
                t = rest_questionClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                n= len(theseKeys)
                i = 0
                while i < n:
                
                    if theseKeys[i] == 'return' and len(inputText) > 1:
                        # pressing RETURN means time to stop
                        continueRoutine = False
                        break
                
                    elif theseKeys[i] == 'backspace':
                        inputText = inputText[:-1]  # lose the final character
                        i = i + 1
                
                    elif theseKeys[i] == 'space':
                        inputText += ' '
                        i = i + 1
                
                    elif theseKeys[i] in ['lshift', 'rshift']:
                        shift_flag = True
                        i = i + 1
                    elif theseKeys[i] == 'period':
                        inputText = inputText + "."
                        i = i + 1
                
                    else:
                        if len(theseKeys[i]) == 1:
                            # we only have 1 char so should be a normal key, 
                            # otherwise it might be 'ctrl' or similar so ignore it
                            if shift_flag:
                                inputText += chr( ord(theseKeys[i]) - ord(' '))
                                shift_flag = False
                            else:
                                inputText += theseKeys[i]
                
                        i = i + 1
                
                
                
                
                
                
                # *question_text* updates
                if t >= 0.0 and question_text.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    question_text.tStart = t  # not accounting for scr refresh
                    question_text.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(question_text, 'tStartRefresh')  # time at next scr refresh
                    question_text.setAutoDraw(True)
                if question_text.status == STARTED:  # only update if drawing
                    question_text.setText((word + '\n' + inputText), log=False)
                
                # *answers* updates
                if t >= 0.0 and answers.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    answers.tStart = t  # not accounting for scr refresh
                    answers.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(answers, 'tStartRefresh')  # time at next scr refresh
                    answers.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(answers.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if answers.status == STARTED:
                    theseKeys = event.getKeys()
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        answers.keys.extend(theseKeys)  # storing all keys
                        answers.rt.append(answers.clock.getTime())
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in rest_questionComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "rest_question"-------
            for thisComponent in rest_questionComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # let's store the final text string into the results finle...
            thisExp.addData('inputText', inputText)
            inputText=""
            trials_3.addData('question_text.started', question_text.tStartRefresh)
            trials_3.addData('question_text.stopped', question_text.tStopRefresh)
            # check responses
            if answers.keys in ['', [], None]:  # No response was made
                answers.keys=None
            trials_3.addData('answers.keys',answers.keys)
            if answers.keys != None:  # we had a response
                trials_3.addData('answers.rt', answers.rt)
            trials_3.addData('answers.started', answers.tStartRefresh)
            trials_3.addData('answers.stopped', answers.tStopRefresh)
            # the Routine "rest_question" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_3'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blocks'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'conditionSelectLoop'


# ------Prepare to start Routine "description1"-------
t = 0
description1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
resp_next_phase = event.BuilderKeyResponse()
# keep track of which components have finished
description1Components = [description_next_phase, resp_next_phase]
for thisComponent in description1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "description1"-------
while continueRoutine:
    # get current time
    t = description1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *description_next_phase* updates
    if t >= 0.0 and description_next_phase.status == NOT_STARTED:
        # keep track of start time/frame for later
        description_next_phase.tStart = t  # not accounting for scr refresh
        description_next_phase.frameNStart = frameN  # exact frame index
        win.timeOnFlip(description_next_phase, 'tStartRefresh')  # time at next scr refresh
        description_next_phase.setAutoDraw(True)
    
    # *resp_next_phase* updates
    if t >= 0.0 and resp_next_phase.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_next_phase.tStart = t  # not accounting for scr refresh
        resp_next_phase.frameNStart = frameN  # exact frame index
        win.timeOnFlip(resp_next_phase, 'tStartRefresh')  # time at next scr refresh
        resp_next_phase.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if resp_next_phase.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in description1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "description1"-------
for thisComponent in description1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('description_next_phase.started', description_next_phase.tStartRefresh)
thisExp.addData('description_next_phase.stopped', description_next_phase.tStopRefresh)
# the Routine "description1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
conditionSelectLoop_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('chooseBlocks.csv'),
    seed=None, name='conditionSelectLoop_2')
thisExp.addLoop(conditionSelectLoop_2)  # add the loop to the experiment
thisConditionSelectLoop_2 = conditionSelectLoop_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisConditionSelectLoop_2.rgb)
if thisConditionSelectLoop_2 != None:
    for paramName in thisConditionSelectLoop_2:
        exec('{} = thisConditionSelectLoop_2[paramName]'.format(paramName))

for thisConditionSelectLoop_2 in conditionSelectLoop_2:
    currentLoop = conditionSelectLoop_2
    # abbreviate parameter names if possible (e.g. rgb = thisConditionSelectLoop_2.rgb)
    if thisConditionSelectLoop_2 != None:
        for paramName in thisConditionSelectLoop_2:
            exec('{} = thisConditionSelectLoop_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    blocks_2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blocks_2')
    thisExp.addLoop(blocks_2)  # add the loop to the experiment
    thisBlock_2 = blocks_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_2.rgb)
    if thisBlock_2 != None:
        for paramName in thisBlock_2:
            exec('{} = thisBlock_2[paramName]'.format(paramName))
    
    for thisBlock_2 in blocks_2:
        currentLoop = blocks_2
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_2.rgb)
        if thisBlock_2 != None:
            for paramName in thisBlock_2:
                exec('{} = thisBlock_2[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_4 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(thisConditionSelectLoop_2['condsFile'], selection=pic_choice),
            seed=None, name='trials_4')
        thisExp.addLoop(trials_4)  # add the loop to the experiment
        thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        for thisTrial_4 in trials_4:
            currentLoop = trials_4
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    exec('{} = thisTrial_4[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "prime_arousal"-------
            t = 0
            prime_arousalClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            
            stim_image_arousal.setImage(stimFile)
            arousal_rating.reset()
            # keep track of which components have finished
            prime_arousalComponents = [stim_frame_arousal, stim_image_arousal, arousal_rating, scale_message2]
            for thisComponent in prime_arousalComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "prime_arousal"-------
            while continueRoutine:
                # get current time
                t = prime_arousalClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                # *stim_frame_arousal* updates
                if t >= 0.0 and stim_frame_arousal.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stim_frame_arousal.tStart = t  # not accounting for scr refresh
                    stim_frame_arousal.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(stim_frame_arousal, 'tStartRefresh')  # time at next scr refresh
                    stim_frame_arousal.setAutoDraw(True)
                
                # *stim_image_arousal* updates
                if t >= 0.0 and stim_image_arousal.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    stim_image_arousal.tStart = t  # not accounting for scr refresh
                    stim_image_arousal.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(stim_image_arousal, 'tStartRefresh')  # time at next scr refresh
                    stim_image_arousal.setAutoDraw(True)
                # *arousal_rating* updates
                if t >= 0.0 and arousal_rating.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    arousal_rating.tStart = t  # not accounting for scr refresh
                    arousal_rating.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(arousal_rating, 'tStartRefresh')  # time at next scr refresh
                    arousal_rating.setAutoDraw(True)
                continueRoutine &= arousal_rating.noResponse  # a response ends the trial
                
                # *scale_message2* updates
                if t >= 0.0 and scale_message2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    scale_message2.tStart = t  # not accounting for scr refresh
                    scale_message2.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(scale_message2, 'tStartRefresh')  # time at next scr refresh
                    scale_message2.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in prime_arousalComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "prime_arousal"-------
            for thisComponent in prime_arousalComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            trials_4.addData('stim_frame_arousal.started', stim_frame_arousal.tStartRefresh)
            trials_4.addData('stim_frame_arousal.stopped', stim_frame_arousal.tStopRefresh)
            trials_4.addData('stim_image_arousal.started', stim_image_arousal.tStartRefresh)
            trials_4.addData('stim_image_arousal.stopped', stim_image_arousal.tStopRefresh)
            # store data for trials_4 (TrialHandler)
            trials_4.addData('arousal_rating.response', arousal_rating.getRating())
            trials_4.addData('arousal_rating.rt', arousal_rating.getRT())
            trials_4.addData('arousal_rating.started', arousal_rating.tStart)
            trials_4.addData('arousal_rating.stopped', arousal_rating.tStop)
            trials_4.addData('scale_message2.started', scale_message2.tStartRefresh)
            trials_4.addData('scale_message2.stopped', scale_message2.tStopRefresh)
            # the Routine "prime_arousal" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "blank_arousal"-------
            t = 0
            blank_arousalClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(0.250000)
            # update component parameters for each repeat
            # keep track of which components have finished
            blank_arousalComponents = [blank_frame2]
            for thisComponent in blank_arousalComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "blank_arousal"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = blank_arousalClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_frame2* updates
                if t >= 0.0 and blank_frame2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    blank_frame2.tStart = t  # not accounting for scr refresh
                    blank_frame2.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(blank_frame2, 'tStartRefresh')  # time at next scr refresh
                    blank_frame2.setAutoDraw(True)
                frameRemains = 0.0 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
                if blank_frame2.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    blank_frame2.tStop = t  # not accounting for scr refresh
                    blank_frame2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank_frame2, 'tStopRefresh')  # time at next scr refresh
                    blank_frame2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blank_arousalComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "blank_arousal"-------
            for thisComponent in blank_arousalComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_4.addData('blank_frame2.started', blank_frame2.tStartRefresh)
            trials_4.addData('blank_frame2.stopped', blank_frame2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_4'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_5 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('news-statements.csv', selection=overall_selected_statements[conditionSelectLoop_2.thisN][(blocks_2.thisN *( statement_per_block)): ((blocks_2.thisN + 1) * ( statement_per_block))]),
            seed=None, name='trials_5')
        thisExp.addLoop(trials_5)  # add the loop to the experiment
        thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        for thisTrial_5 in trials_5:
            currentLoop = trials_5
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
            if thisTrial_5 != None:
                for paramName in thisTrial_5:
                    exec('{} = thisTrial_5[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "statement_accuracy"-------
            t = 0
            statement_accuracyClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            statement_image2.setImage(Statements)
            validity_rating.reset()
            # keep track of which components have finished
            statement_accuracyComponents = [text_frame2, statement_image2, validity_rating, scale_message3]
            for thisComponent in statement_accuracyComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "statement_accuracy"-------
            while continueRoutine:
                # get current time
                t = statement_accuracyClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_frame2* updates
                if t >= 0.0 and text_frame2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_frame2.tStart = t  # not accounting for scr refresh
                    text_frame2.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(text_frame2, 'tStartRefresh')  # time at next scr refresh
                    text_frame2.setAutoDraw(True)
                
                # *statement_image2* updates
                if t >= 0.0 and statement_image2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    statement_image2.tStart = t  # not accounting for scr refresh
                    statement_image2.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(statement_image2, 'tStartRefresh')  # time at next scr refresh
                    statement_image2.setAutoDraw(True)
                # *validity_rating* updates
                if t >= 0.0 and validity_rating.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    validity_rating.tStart = t  # not accounting for scr refresh
                    validity_rating.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(validity_rating, 'tStartRefresh')  # time at next scr refresh
                    validity_rating.setAutoDraw(True)
                continueRoutine &= validity_rating.noResponse  # a response ends the trial
                
                # *scale_message3* updates
                if t >= 0.0 and scale_message3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    scale_message3.tStart = t  # not accounting for scr refresh
                    scale_message3.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(scale_message3, 'tStartRefresh')  # time at next scr refresh
                    scale_message3.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in statement_accuracyComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "statement_accuracy"-------
            for thisComponent in statement_accuracyComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_5.addData('text_frame2.started', text_frame2.tStartRefresh)
            trials_5.addData('text_frame2.stopped', text_frame2.tStopRefresh)
            trials_5.addData('statement_image2.started', statement_image2.tStartRefresh)
            trials_5.addData('statement_image2.stopped', statement_image2.tStopRefresh)
            # store data for trials_5 (TrialHandler)
            trials_5.addData('validity_rating.response', validity_rating.getRating())
            trials_5.addData('validity_rating.rt', validity_rating.getRT())
            trials_5.addData('validity_rating.started', validity_rating.tStart)
            trials_5.addData('validity_rating.stopped', validity_rating.tStop)
            trials_5.addData('scale_message3.started', scale_message3.tStartRefresh)
            trials_5.addData('scale_message3.stopped', scale_message3.tStopRefresh)
            # the Routine "statement_accuracy" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials_5'
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blocks_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'conditionSelectLoop_2'


# ------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = [thanks_text]
for thisComponent in ThanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_text* updates
    if t >= 0.0 and thanks_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks_text.tStart = t  # not accounting for scr refresh
        thanks_text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thanks_text, 'tStartRefresh')  # time at next scr refresh
        thanks_text.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanks_text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        thanks_text.tStop = t  # not accounting for scr refresh
        thanks_text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(thanks_text, 'tStopRefresh')  # time at next scr refresh
        thanks_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks_text.started', thanks_text.tStartRefresh)
thisExp.addData('thanks_text.stopped', thanks_text.tStopRefresh)







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
