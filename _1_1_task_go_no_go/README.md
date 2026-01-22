# Go / No-Go Task (SART Paradigm)

This oTree app implements a classic **Go / No-Go Task**, specifically based on the **Sustained Attention to Response Task (SART)** paradigm.

The primary goal of this task is to measure **reaction time**, **sustained attention**, and **response inhibition**.

## Task Mechanism

1.  **Stimuli:** A series of single letters is presented to the participant one by one.
2.  **Go Condition:** For the majority of letters (Standard: A-Z), the participant must press the **SPACE** bar as quickly as possible.
3.  **No-Go Condition:** For a specific target letter (Standard: 'X'), the participant must inhibit their response and **not press** any key.
4.  **Theory:** Due to the high frequency of "Go" stimuli, a motor routine is established. The participant must actively suppress this routine when the rare "No-Go" stimulus appears.

## App Structure

The app is designed to be modular and can be easily copied into other oTree projects.

* **`__init__.py`**: Contains the configuration (`Constants`), database models (`Player`), and the server-side logic for data processing (`compute_summary_stats`).
* **`AssessmentPhaseTask.html`**: The experimental interface. It contains the JavaScript logic for precise millisecond timing and stimulus rendering.
* **`Introduction.html`**: A standardized instruction page for participants.

## Configuration & Customization

All scientific parameters can be adjusted centrally in `__init__.py` within the `C` (Constants) class. No changes to the JavaScript code are required.

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `NUM_TRIALS` | `45` | Total number of trials. *Note: Set to `5` for quick debugging.* |
| `NO_GO_LETTER` | `'X'` | The stimulus letter that requires response inhibition. |
| `NO_GO_PROPORTION`| `0.10` | The probability of a No-Go trial (here: 10%). |
| `STIM_DURATION_MS`| `250` | Duration the letter remains visible (in milliseconds). |
| `ISI_VALUES_MS` | `[1000, 2000, 4000]` | List of possible Inter-Stimulus Intervals (pause between trials). |

## Data Output

The app automatically calculates aggregated statistics and saves them to the standard oTree Excel export. Manual post-processing of raw logs is not required for standard analyses.

The following variables are available per participant:

* **`total_hits`**: Number of correct responses to Go stimuli.
* **`total_misses`**: Number of missed responses to Go stimuli (Omission Errors).
* **`total_false_alarms`**: Number of incorrect responses to No-Go stimuli (Commission Errors). *This is the primary metric for inhibition failure.*
* **`total_correct_rejections`**: Number of successfully withheld responses to No-Go stimuli.
* **`avg_rt_ms`**: Average reaction time (calculated for valid hits only).
* **`task_data_json`**: The complete raw data for every single trial (timestamps, stimulus, response status) stored as a JSON string for granular analysis.

## Usage in Your Experiment

1.  Copy the `task_go_no_go` folder into your oTree project root.
2.  Add the app to your `settings.py` under `SESSION_CONFIGS`.
3.  **Important:** Ensure `NUM_TRIALS` is set high enough for production runs (SART effects typically require a longer duration to induce fatigue and automaticity).
