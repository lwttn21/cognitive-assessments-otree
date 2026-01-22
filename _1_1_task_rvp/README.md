# Rapid Visual Information Processing (RVP) - Single Target

This oTree app implements a variation of the **Rapid Visual Information Processing (RVP)** task.

It is a test of sustained attention and working memory. Unlike the standard version where participants look for multiple sequences simultaneously, this version assigns **one specific target sequence** (e.g., "2-4-6") that the participant must search for during the block.

## Task Mechanism

1.  **Stimuli:** A continuous stream of single digits (1-9) appears in the center of the screen (default speed: 600ms per digit).
2.  **Target Assignment:** At the start of the round, the system randomly selects **one** target sequence from the configured list (e.g., "3-5-7").
3.  **Goal:** The participant must press the button as soon as they detect the **last digit** of the assigned sequence.
4.  **Constraint:** Occurrences of other valid RVP sequences (that are not the assigned target) are treated as non-targets.

## App Structure

The app follows the modern oTree 5 flat structure.

* **`__init__.py`**:
    * Contains the `generate_rvp_stream` function, which creates a pseudo-random digit stream.
    * Ensures the specific target appears exactly `NUM_TARGETS` times.
    * Calculates the correct indices for server-side validation.
* **`RVP.html`**:
    * The main interface using JavaScript `setInterval` for precise display timing.
    * Dynamically displays the assigned target (e.g., "Target: 2-4-6") at the bottom of the screen.
* **`RVPInstruction.html`**: General instructions explaining the concept of number sequences.
* **`RVPResults.html`**: Displays Hits, Misses, False Alarms, and Reaction Time.

## Configuration & Customization

Parameters can be adjusted in `__init__.py` within the `C` (Constants) class.

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `DIGIT_SPEED_MS` | `600` | Duration each digit is visible (in milliseconds). Standard RVP is often 600ms (100 digits/min). |
| `NUM_DIGITS_TOTAL` | `100` | Total length of the digit stream. |
| `NUM_TARGETS` | `8` | How often the target sequence appears within the stream. |
| `TARGET_SEQUENCES` | List | The pool of possible sequences (e.g., `[2,4,6]`, `[3,5,7]`, `[4,6,8]`). One is chosen randomly per round. |

## Data Output

The app automatically calculates performance metrics and saves them to the database.

The following variables are available per participant:

* **`rvp_hits`**: Number of correct button presses (within the target window).
* **`rvp_misses`**: Number of targets that passed without a response.
* **`rvp_false_alarms`**: Number of clicks when no target was present.
* **`rvp_avg_rt`**: Average reaction time (in ms) for correct hits.
* **`rvp_active_target`**: The specific sequence the player searched for in this round (e.g., "3-5-7").
* **`rvp_raw_data`**: Detailed log string: `Index_Digit_IsCorrect_RT`.

## Usage in Your Experiment

1.  Copy the `task_rvp` folder into your oTree project root.
2.  Add the app to your `settings.py` under `SESSION_CONFIGS`.
3.  **Note on Difficulty:** This "Single Target" version is generally less demanding on working memory than the 3-target version but requires high sustained attention.
