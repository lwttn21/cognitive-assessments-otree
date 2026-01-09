# N-Back Task (Working Memory Paradigm)

This oTree app implements a classic **N-Back Task**, a widely used continuous performance task to measure **working memory capacity** and **cognitive fatigue**.

## Task Mechanism

1.  **Stimuli:** A sequence of letters is presented one by one.
2.  **The Rule ($n$):** The participant must determine if the current letter matches the one presented exactly **$n$** positions back in the sequence.
3.  **Response:** The participant must press the **SPACE** bar only when a match occurs (Target). No action is required for non-matches (Distractors).
4.  **Theory:** The task requires the participant to constantly update their mental "buffer," dropping the oldest letter and adding the newest. This continuous updating makes it a sensitive measure of mental effort and fatigue over time.

## App Structure

The app is designed to be modular and can be easily integrated into existing oTree projects.

* **`__init__.py`**: Contains the configuration (`Constants`), the sequence generation logic, and the server-side data processing.
* **`Instructions.html`**: A standardized introduction page explaining the $n$-back rule.
* **`PracticePage.html`**: A training phase featuring a visual "history bar" (memory aid) and immediate feedback to ensure participant understanding.
* **`StartMainTask.html`**: A transition page to notify participants that visual aids will be removed and the actual assessment is starting.
* **`TaskPage.html`**: The experimental interface. It contains the JavaScript logic for precise millisecond timing without visual assistance.

## Configuration & Customization

All scientific parameters can be adjusted centrally in `__init__.py` within the `C` (Constants) class.

| Parameter | Default       | Description |
| :--- |:--------------| :--- |
| `N_LEVEL` | `2`           | The difficulty level ($n$). $2$ is standard; $3$ significantly increases memory load. |
| `NUM_TRIALS` | `30`          | Total number of stimuli in the main task. |
| `MATCH_PROPORTION` | `0.25`        | Probability of a match (target) trial (Standard: 25%). |
| `STIMULUS_DURATION`| `600`         | Duration the letter remains visible (in milliseconds). |
| `ISI_FIXED` | `2000`        | Fixed Inter-Stimulus Interval (pause between trials) in milliseconds. |
| `PRACTICE_TRIALS` | `15`          | Number of trials in the guided practice phase. |
| `LETTERS` | `[B, C, ...]` | List of consonants used to prevent phonological grouping (vowels are excluded). |

## Data Output

The app automatically calculates aggregated statistics for standard analysis, while also providing raw trial-by-trial logs.

* **`total_hits`**: Number of correct identifications of a match.
* **`total_false_alarms`**: Number of incorrect responses to non-match stimuli (Commission Errors).
* **`avg_rt_ms`**: Average reaction time calculated for hits only.
* **`task_data_json`**: The complete raw data for every single trial (timestamps, stimulus, response status) stored as a JSON string for granular fatigue-slope analysis.

## Usage in Your Experiment

1.  Copy the `task_n_back` folder into your oTree project root.
2.  Add the app to your `SESSION_CONFIGS` in `settings.py`.
3.  **Note:** For fatigue research, ensure `NUM_TRIALS` is sufficiently high to observe performance degradation over time.