# Trail Making Test - Part A (TMT-A)

This oTree app implements **Part A of the Trail Making Test**, a widely recognized neuropsychological instrument.

The primary goal of this task is to measure **visual search**, **motor speed**, and **perceptual processing speed**.

## Task Mechanism

1.  **Stimuli:** A set of blue circles containing numbers (1, 2, 3...) is randomly distributed across the screen.
2.  **Anti-Collision:** The app utilizes a custom algorithm to ensure circles are placed without overlapping.
3.  **Goal:** The participant must click the circles in ascending numerical order ($1 \rightarrow 2 \rightarrow 3 \dots$).
4.  **Visual Feedback:** Correct clicks turn the circle **green** and draw a connecting line from the previous circle. Incorrect clicks flash **red** and are recorded as errors.
5.  **Theory:** Part A serves as a baseline for motor and visual speed, which is essential for calculating "switching costs" when compared to Part B.

## App Structure

The app follows the modern oTree 5 flat structure.

* **`__init__.py`**: Contains the configuration (`C`), database models (`Player`), and the page sequence logic.
* **`Exercise.html`**: The interactive interface using HTML5 Canvas for real-time line drawing and JavaScript for precise timing.
* **`Introduction.html`**: Includes a standardized English instruction with a dynamic CSS-based visual example of the task.
* **`Results.html`**: Displays immediate feedback regarding total time, average speed per circle, and error count.

## Configuration & Customization

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `NUM_CIRCLES` | `15` | The total number of circles generated for the task. |

## Data Output

The following variables are available per participant:

* **`tmt_a_duration`**: Total time from start to completion (in seconds).
* **`tmt_a_errors`**: Total number of incorrect clicks.
* **`tmt_a_avg_speed`**: Average time taken to find and click each circle (seconds per item).