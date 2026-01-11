# Multidimensional Fatigue Inventory (MFI) - Short Subscale

This oTree app implements a short version of the **Multidimensional Fatigue Inventory (MFI)**.

It is designed to assess the participant's current state of **mental fatigue** using a visual analogue scale (slider). The implementation is based on the psychometric instrument developed by Smets et al. (1995).

## Survey Mechanism

1.  **Items:** The participant is presented with 4 statements regarding their current physical and mental state (e.g., "I feel tired", "I feel fit").
2.  **Scale:** Responses are collected using a 7-point slider scale ranging from **-3** ("No, that is not true") to **+3** ("Yes, that is true").
3.  **Scoring:** The center point (0) represents a neutral stance. Positive values indicate agreement, while negative values indicate disagreement.
4.  **Goal:** To measure dynamic changes in fatigue levels, typically before and after a cognitive workload (e.g., MATB-II or Stroop Task).

## App Structure

The app follows the modern oTree 5 flat structure and is designed to be modular.

* **`__init__.py`**: Contains the database models (`Player` class) defining the specific questions and the logical conditions (`is_displayed`) for when the survey should appear.
* **`MentalFatigueInventory.html`**: The user interface. It features a custom CSS grid layout for the sliders and JavaScript logic to synchronize the visual slider positions with hidden input fields for data storage.

## Configuration & Customization

The questions and scale parameters can be adjusted directly in `__init__.py`.

### Changing Questions
To modify the text of the items, locate the `Player` class in `__init__.py` and change the `label` attribute:

```python
mfi_1 = models.IntegerField(min=-3, max=3, label="New question text here")
