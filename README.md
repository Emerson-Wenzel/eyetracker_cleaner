# eyetracker_cleaner
Emerson Wenzel
12/21/2017

# Purpose
This tool was developed to help conduct Engineering Psychology Research at the Volpe National Transporation Systems Center. Part of the work at the center involves running participants through a driving simulator to understand how humans may react in specific driving events. To measure reactions, Eyetrackers are used. Unfortunately, the events researchers want to observe only make up ~1/4 of the total eyetracker footage. 

To improve the workflow process, the tool can be used in conjunction when overseeing participants to allow the active editing of footage so that when scoring the videos and conducting analysis, researchers only have to view the important parts of the footage.



# Execution
This program takes no command line arguments

# Workflow
the workflow for using this program with an eyetracker is as follows:

	- Fit eyetracker onto participant.
	- Prepare experimental environment.
	- start eyetracker recording AND hit "Start Timer" on
		stopwatch.py at the same time (this is required to ensure
		the footage is edited properly)
	- Use the "Start Cut" and "End Cut" buttons to select the
	  wanted footage
	- Once all events have occured, hit "Stop Timing"
	- After "Stop Timing" has been hit, end the eyetracker AVI
	- Use "Select file" to select the recently created eyetracker AVI 
	- Hit "Make New AVI" to create the edited AVI.

Note: For the desired results, ensure that you are not trying to
	select time frames that do not exist in the video
	(e.g. 2:30 to 2:45 in a 2 minute video)

