# Visual Analog Scales (VAS) - Subjective State Assessment

This oTree app implements a set of **Visual Analog Scales (VAS)** to measure subjective psychological states.

It is designed as a rapid assessment tool to track changes in the participant's state (e.g., fatigue, motivation) throughout an experiment, typically administered before and after cognitive tasks.

## Survey Mechanism

1.  **Items:** The participant rates 4 specific states:
    * Mental Fatigue
    * Motivation
    * Mental Workload (Demand)
    * Frustration
2.  **Scale:** Responses are collected using a continuous slider ranging from **0** ("Not at all") to **100** ("Very much").
3.  **Scoring:** The slider returns an integer value between 0 and 100. Higher values indicate a higher intensity of the respective feeling.
4.  **Goal:** To capture momentary fluctuations in subjective state with minimal time investment.

## App Structure

The app follows the modern oTree 5 flat structure.

* **`__init__.py`**: Contains the database models (`Player` class) defining the 0-100 integer fields and the logical conditions (`is_displayed`) for when the survey should appear.
* **`VASPage.html`**: The user interface. It features a custom CSS layout for the sliders, ensuring clear labeling of the start and end anchors ("Not at all" vs. "Very much").

## Configuration & Customization

The display logic and specific questions are defined in `__init__.py`.

### Display Logic (Repeated Measures)
To show this survey multiple times (e.g., after every task block), modify the `is_displayed` method in the `VASPage` class:

```python
@staticmethod
def is_displayed(player: Player):
    # Example: Show in specific rounds only
    return player.round_number in [3, 21, 39, 57, 75, 93]
