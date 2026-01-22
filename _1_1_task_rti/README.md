# Reaction Time Task (RTI) - Five Choice

This oTree app implements a **Five-Choice Reaction Time (RTI)** task.

It is designed to distinguish between **cognitive reaction time** (processing speed) and **motor movement time**. Unlike simple reaction time tasks, this version uses a "press-hold-release" mechanism to separate the decision phase from the movement phase.

## Task Mechanism

1.  **Home Position:** The participant clicks and **holds** the "HOME" button at the bottom of the screen.
2.  **Foreperiod:** A random delay (default 600-1500ms) occurs while holding.
3.  **Stimulus:** One of 5 circles arranged in an arc at the top turns **YELLOW**.
4.  **Reaction Time (RT):** The participant must **release** the mouse button as quickly as possible.
5.  **Movement Time (MT):** The participant moves the cursor to the yellow circle and clicks it.

## App Structure

The app follows the modern oTree 5 flat structure.

* **`__init__.py`**: Contains the trial generation logic (randomizing targets and delays) and database models.
* **`RTI.html`**: The main interface. It uses a custom CSS "Arc Layout" to position the 5 targets equidistantly from the home button. JavaScript event listeners handle the precise `mousedown` and `mouseup` timing logic.
* **`RTIInstruction.html`**: Explains the "Press and Hold" mechanic to the user.
* **`RTIResults.html`**: Displays the split performance metrics (RT vs. MT).

## Configuration & Customization

Parameters can be adjusted in `__init__.py` within the `C` (Constants) class.

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `NUM_TRIALS` | `15` | Total number of trials. |
| `NUM_LOCATIONS` | `5` | Number of target circles (1 = Simple RTI, 5 = Choice RTI). |
| `DELAY_MIN_MS` | `600` | Minimum wait time before stimulus appears. |
| `DELAY_MAX_MS` | `1500` | Maximum wait time before stimulus appears. |

## Data Output

The app automatically separates cognitive speed from motor speed.

The following variables are available per participant:

* **`rti_mean_rt`** (Reaction Time): Average time (ms) from Stimulus Onset -> Button Release. Represents processing speed.
* **`rti_mean_mt`** (Movement Time): Average time (ms) from Button Release -> Target Click. Represents motor speed.
* **`rti_total_score`**: Number of successfully completed trials.
* **`rti_errors`**: Number of failed trials (e.g., releasing the button too early).
* **`rti_raw_data`**: Detailed log string: `Trial_TargetIndex_RT_MT_Status`.

## Usage in Your Experiment

1.  Copy the `task_rti` folder into your oTree project root.
2.  Add the app to your `settings.py` under `SESSION_CONFIGS`.
3.  **Scientific Note:** This task is particularly useful for detecting motor deficits or slowing of processing speed independent of motor ability.
