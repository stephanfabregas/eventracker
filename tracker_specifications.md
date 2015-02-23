Air Flow Tracking Program Specification
====================

Author: stephan.fabregas@gmail.com
Date: 2015-02-23

Introduction
--------------------

An easy way to track a behavior or physiological state based on observation is not always an easy task. This program is set up to offer timed reminders to record an observation of such a behavior/state with minimal intrusion into the user's working environment.

## Front End

### Layout

Simple grid layout. Four columns, 3 rows.

- Row 1: Feedback
- Row 2: Data input. 4 buttons, 1 for each column.
  + Button 1: Left
  + Button 2: Right
  + Button 3: Both
  + Button 4: Neither
- Row 3: Program control. 1 button. 4th column.
  + Button 5: Exit

### Backend

#### Feedback Area
Feedback. Span the four columns. Show current state (no response, or selected state). Perhaps show number of recorded events/response rate.

#### Button control
1. Left. Label "Left". Record value 0.
2. Right. Label "Right". Record value 1.
3. Both. Label "Both". Record value 2.
4. Neither. Label "Neither". Record value 3.

#### Program Flow

- Open Program
  + All buttons active
  + Prompt for first input in feedback (show no response to start)
  + Start timer for next stimulus
- Stimuli
  + Stimulus occurs every 30-seconds, starting at next xx-hour:xx-minute:30-second boundary, that is, seconds on system clock should read either 00 or 30
  + Stimulus is simple, short tone/audio
- Data control
  + Default value (no response) is -1
  + Response can be updated by pressing any of the input buttons. However, once a response is made, it cannot be returned to no response (may include an undo option with different interface)
  + Responses are held in single item buffer until end of epoch/file write.
  + Data are written to file (csv) with timestamp for each 30-second epoch (first timestamp is based on start of program) upon:
    * End of epoch (after timer completes, start next timer, write data to file, prompt for next response). Close file connection after each write to ensure that data are locked.
    * Program exit
    * Note that last response may be lost due to crash/unexpected program exit

### Nice to Haves

- Program foregrounds when stimulus occurs. Backgrounds when response is made
