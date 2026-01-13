# Trail Making Test - Part B (TMT-B)

This oTree app implements **Part B of the Trail Making Test**.

The primary goal of this task is to measure **executive function**, specifically **cognitive flexibility** and **set-shifting** (the ability to switch between mental sets).

## Task Mechanism

1.  **Stimuli:** A set of blue circles containing both numbers (1, 2, 3...) and letters (A, B, C...) is randomly distributed.
2.  **Goal:** The participant must click the circles in an alternating sequence: **1 – A – 2 – B – 3 – C** and so on.
3.  **Task Load:** This part is significantly more demanding than Part A as it requires maintaining two different sequences in working memory and switching between them.
4.  **Fatigue Sensitivity:** TMT-B is highly sensitive to **Mental Fatigue**. As kognitive resources deplete, the "switching cost" (time needed to switch between number and letter) typically increases.

## App Structure

The app follows the modern oTree 5 flat structure.

* **`__init__.py`**: Manages the TMT-B specific data fields and the randomized alternating sequence generation.
* **`Exercise.html`**: Utilizes JavaScript for sequence validation, real-time feedback, and canvas-based line drawing.
* **`Introduction.html`**: Provides simplified instructions ("switch back and forth") and a visual example to ensure participants understand the switching rule.
* **`Results.html`**: Shows performance metrics specific to the switching task.

## Configuration & Customization

| Parameter | Default | Description |
| :--- |:--------| :--- |
| `NUM_CIRCLES` | `20`    | Total circles. Recommendation: use an even number for balanced number-letter pairs. |

## Data Output

* **`tmt_b_duration`**: Total completion time (in seconds).
* **`tmt_b_errors`**: Number of sequence errors made.
* **`tmt_b_avg_speed`**: Average time per item, reflecting the higher cognitive load of the switching condition.

## Scientific Analysis

To isolate the executive component of fatigue, it is common practice to calculate the **difference score**:
$$TMT_{Score} = tmt\_b\_duration - tmt\_a\_duration$$
A significant increase in this score over the course of an experiment is a strong indicator of kognitive exhaustion.