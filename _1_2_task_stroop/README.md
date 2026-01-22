# Stroop Task (Color-Word Interference)

This oTree app implements a standard **Stroop Color-Word Interference Test**.

The primary goal of this task is to measure **cognitive control**, **selective attention**, and **processing speed** (inhibition of cognitive interference).

## Task Mechanism

1.  **Stimuli:** A series of color words (e.g., "RED", "BLUE") is presented to the participant.
2.  **Congruent Condition:** The ink color of the word matches the semantic meaning (e.g., the word "RED" printed in red ink).
3.  **Incongruent Condition:** The ink color differs from the semantic meaning (e.g., the word "RED" printed in green ink).
4.  **Goal:** The participant must select the color of the **ink**, ignoring the meaning of the word itself.
5.  **Theory:** Reaction times are typically slower and error rates higher for incongruent stimuli due to the automaticity of reading (Stroop Effect).

## App Structure

The app follows the modern oTree 5 flat structure and is designed to be modular.

* **`__init__.py`**: Contains the configuration (`C`), database models (`Player`), and the server-side logic (`get_stroop_trials`) that generates the randomized trial sequence with a 50/50 split between congruent and incongruent items.
* **`Stroop.html`**: The experimental interface. It utilizes JavaScript for precise millisecond timing (`performance.now()`) and dynamic rendering of the colored words.
* **`StroopInstruction.html`**: A standardized instruction page for participants explaining the task rules.
* **`StroopResults.html`**: Displays immediate feedback to the participant regarding their accuracy and speed.

## Configuration & Customization

All scientific parameters can be adjusted centrally in `__init__.py` within the `C` (Constants) class.

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `NUM_TRIALS` | `20` | The total number of trials presented to the participant. |
| `TIMEOUT_SECONDS` | `120` | Hard time limit for the entire task page (in seconds). |
| `COLORS` | List | A list of tuples defining the available colors (Hex Code, Name). |
| `WORDS` | List | The list of words to be displayed (e.g., "RED", "BLUE"). |

## Data Output

The app automatically calculates aggregated statistics and saves them to the standard oTree Excel export.

The following variables are available per participant:

* **`stroop_score`**: Total number of correct responses.
* **`stroop_errors`**: Total number of incorrect responses.
* **`stroop_avg_rt`**: Average reaction time (in milliseconds) across all trials.
* **`stroop_raw_data`**: A raw log string containing the history of every trial (Index, Correctness, Reaction Time) for detailed post-hoc analysis.

## Usage in Your Experiment

1.  Copy the `task_stroop` folder into your oTree project root.
2.  Add the app to your `settings.py` under `SESSION_CONFIGS`.
3.  **Important:** Ensure `NUM_TRIALS` is set appropriate for your experimental design (typically 20-50 for short assessments).
