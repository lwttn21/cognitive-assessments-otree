# Motor Screening Task (MOT)

This oTree app implements a standard **Motor Screening Task (MOT)**.

It serves two primary purposes:
1.  **Screening:** To ensure the participant has adequate visual and motor skills to comprehend and perform the subsequent cognitive tests using a computer mouse.
2.  **Assessment:** To measure basic **psychomotor speed** and **fine motor precision**.

## Task Mechanism

1.  **Stimuli:** A green cross appears at a random location within a fixed 800x600 pixel area.
2.  **Action:** The participant must move the mouse cursor to the cross and click on its center as quickly as possible.
3.  **Progression:** Upon clicking, the current cross disappears, and a new one appears at a different location after a short delay.
4.  **Metrics:** The task measures how fast the participant reacts (Reaction Time) and how close they clicked to the true center of the cross (Spatial Error).

## App Structure

The app follows the modern oTree 5 flat structure.

* **`__init__.py`**: Contains the configuration (`C`) and database models.
* **`MOT.html`**: The main interface. It uses JavaScript to randomize the cross positions and calculates the **Euclidean distance** between the click coordinates and the center of the target.
* **`MOTInstruction.html`**: Brief instructions.
* **`MOTResults.html`**: Displays the average speed and accuracy (pixel deviation).

## Configuration & Customization

Parameters can be adjusted in `__init__.py` within the `C` (Constants) class.

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `NUM_TRIALS` | `10` | The total number of crosses presented. |
| `CROSS_SIZE_PX` | `40` | The width/height of the cross stimulus in pixels. |
| `CONTAINER_WIDTH` | `800` | Width of the active task area (px). |
| `CONTAINER_HEIGHT` | `600` | Height of the active task area (px). |

## Data Output

The app automatically calculates mean performance metrics and saves detailed logs.

The following variables are available per participant:

* **`mot_mean_rt`**: Average Reaction Time (in milliseconds). Lower is faster.
* **`mot_mean_error`**: Average Spatial Error (in pixels). This is the distance between the click point and the exact center of the cross. Lower is more precise.
* **`mot_raw_data`**: A detailed log string containing data for every click: `Trial_TargetX_TargetY_ClickX_ClickY_Error_RT`.

## Usage in Your Experiment

1.  Copy the `task_mot` folder into your oTree project root.
2.  Add the app to your `settings.py` under `SESSION_CONFIGS`.
3.  **Recommendation:** It is standard practice to run this task **first** in your test battery. If a participant has an unusually high error rate or RT here, their results in complex tasks (like RTI or SSP) may be invalid due to motor/visual deficits.
