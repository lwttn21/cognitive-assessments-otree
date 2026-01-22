# Task Switching Paradigm

Classic **Task Switching** paradigm, a core instrument in neuropsychology used to measure **executive control** and **cognitive flexibility**.

The primary goal of this task is to assess the cognitive overhead incurred when the brain must transition between different mental sets or rules.

## Task Mechanism

* **Stimuli:** Participants are shown a central stimulus (an arrow) that possesses two distinct attributes: its **location** on the screen (Left/Right) and the **direction** it points (Left/Right).
* **The Rules:** The task alternates between two instructional sets based on the arrow's vertical position:
    1. **Rule: LOCATION (Upper Half)** — The participant must respond to the arrow's position on the screen.
    2. **Rule: DIRECTION (Lower Half)** — The participant must respond to the direction the arrow is pointing.
* **Controls:** The participant uses the **Left Arrow Key** and **Right Arrow Key** to respond.
* **Conflict (Incongruency):** The app generates incongruent trials (e.g., an arrow on the left side pointing to the right) to measure interference and inhibitory control.
* **Goal:** The participant must react as quickly and accurately as possible according to the rule defined by the arrow's vertical position.

## App Structure

The app follows the modern oTree 5 flat structure:

* **`__init__.py`**: Contains the configuration (`C`), randomized trial generation logic in `creating_session`, and the server-side calculation of accuracy and response latencies.
* **`MyPage.html`**: The interactive interface using JavaScript to capture millisecond-precise reaction times and keyboard inputs (Arrow Keys). It includes a timer that automatically proceeds if `STIMULUS_DURATION` is reached.
* **`Instructions.html`**: Comprehensive instructions explaining the spatial rule (Upper vs. Lower half) with dynamic information about time limits.
* **`Results.html`**: Displays final performance metrics, including accuracy, mean reaction time, and specific error counts.

## Configuration & Customization

| Parameter | Default | Description |
| :--- | :--- | :--- |
| **NUM_ROUNDS** | 10 | The total number of stimuli presented in the session. |
| **STIMULUS_DURATION** | None | Time limit in milliseconds. If set to `None`, the task is self-paced. For 2 seconds, use `2000`. |

## Data Output

The following variables are recorded per participant for analysis:

* **`is_correct`**: Boolean recorded for each trial indicating if the response matched the rule (taking into account the vertical position).
* **`reaction_time`**: The response latency in milliseconds for each trial.
* **`accuracy`**: The percentage of correct responses across all rounds.
* **`mean_rt`**: Mean reaction time (ms) for correct trials, calculated at the end of the session.
* **`err_loc`**: Total number of errors made during LOCATION trials (Upper Half).
* **`err_dir`**: Total number of errors made during DIRECTION trials (Lower Half).