# eyetracker_cleaner
Emerson Wenzel
12/21/2017

purpose: allow the editing of eye tracker footage to only
	include events that researchers want to observe

execution: this program takes no command line arguments

Workflow: the workflow for using this program with an eyetracker is as
	  follows:

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

