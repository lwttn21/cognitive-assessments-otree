# Stop-Signal Task (SST) for oTree

This application implements a  **Stop-Signal Task (SST)**, a cognitive experimental paradigm used to measure inhibitory control and response inhibition.

## Task Overview

The task requires participants to respond to visual stimuli as quickly as possible while occasionally suppressing their response when an auditory signal occurs.

### Part 1: Training
* **Stimulus:** An arrow pointing left (←) or right (→) inside a circular frame.
* **Action:** Press **'f'** for Left and press **'j'** for Right.
* **Goal:** Respond as accurately and quickly as possible.

### Part 2: Testing
* **Stimulus:** An arrow pointing left (←) or right (→) inside a circular frame. **and**
an auditory beep (Stop-Signal).
* **Action:** Press 'f' for left and 'j' for right as in part 1 and withhold (inhibit) the motor response if 
the beep came up.
* **Goal**: Respond as accurately and quickly as possible **and** 
successfully inhibit your reaction if you heard a beep.

---

## Experimental Structure

The experiment is divided into two distinct phases:

| Phase | Rounds | Description |
| :--- | :--- | :--- |
| **1: Training** | 1 - 16 | Only "Go" trials to establish a baseline reaction speed. |
| **2: Testing** | 17 - 32 | Mixed trials: 50% "Go" trials and 50% "Stop" trials (randomized). |

---

## Technical Features

* **Real-time Data:** Uses oTree's `live_method` to capture keystrokes and Reaction Times (RT) instantly without page refreshes.
* **Precise Timing:** RT is measured in milliseconds using `performance.now()` in the browser.
* **Automatic Scoring:** The logic automatically differentiates between "Go" accuracy and "Stop" inhibition success.
* **Inter-Trial Interval (ITI):** A 1.0-second blank page between trials ensures a clear separation of stimuli.

## Data Variables

The following data is recorded for every trial in the oTree database:

* `arrow_direction`: The direction of the stimulus (`left` or `right`).
* `stop_signal`: Boolean indicating if a beep was scheduled.
* `response`: The key pressed by the participant.
* `reaction_time`: Time from stimulus onset to keypress (in ms).
* `correct`: Boolean indicating if the trial requirement was met.
* `phase`: Indicates whether the trial was in the training or testing phase.

## Installation & Requirements

1.  **Audio File:** Ensure that `beep.wav` is located in `_static/task_stop_signal/`.
2.  **oTree Version:** Compatible with oTree 5.x and 6.x.
3.  **Browser:** Requires a modern browser (Chrome, Firefox, or Edge) with audio permissions enabled.
