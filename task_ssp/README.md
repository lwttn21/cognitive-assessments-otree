# Spatial Span Task (Corsi Block Tapping)

This oTree app implements a **Spatial Span** task, widely known as the **Corsi Block Tapping Test**.

It measures **visuospatial working memory capacity**. The participant observes a sequence of blocks lighting up and must attempt to reproduce the sequence in the exact order. The test is adaptive: the sequence length increases as the participant succeeds.

## Task Mechanism

1.  **Stimuli:** 9 white boxes are displayed in a dispersed layout on a dark background.
2.  **Sequence:** A specific number of boxes flash green one after another.
3.  **Reproduction:** The participant clicks the boxes to reproduce the sequence.
4.  **Adaptive Logic:**
    * **Success:** If the sequence is recalled correctly, the span (length) increases by 1 for the next round.
    * **Failure:** If recalled incorrectly, the same span length is repeated (second chance).
    * **Termination:** If the participant makes two consecutive errors at the same span length, the task ends.

## App Structure

The app follows the modern oTree 5 flat structure.

* **`__init__.py`**:
    * Manages the adaptive difficulty using `participant.vars` (tracking current span and errors).
    * Contains `generate_sequence()` to create random non-repeating path sequences.
    * **Technical Note:** Uses `IntegerField` (0/1) instead of `BooleanField` for the `ssp_is_correct` field to ensure stability with hidden form inputs.
* **`SSP.html`**:
    * The visual interface using absolute positioning for the Corsi layout.
    * JavaScript handles the precise timing of the flash animation (`setTimeout`) and records click timestamps.
* **`SSPInstruction.html`**: Explains the rules to the participant.
* **`SSPResults.html`**: Displays the final "Spatial Span" (maximum length achieved).

## Configuration & Customization

Parameters can be adjusted in `__init__.py` within the `C` (Constants) class.

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `NUM_ROUNDS` | `20` | A buffer number. The task usually terminates earlier via logic, but this sets the hard limit. |
| `BOX_POSITIONS` | List | A list of (Top%, Left%) coordinates defining the layout of the 9 boxes. |
| `START_SPAN` | `2` | The length of the sequence in the first round. |
| `BOX_FLASH_DURATION_MS` | `500` | How long a box stays green during the sequence. |
| `BOX_PAUSE_DURATION_MS` | `250` | The pause between two flashes. |

## Data Output

The app stores detailed performance data for every round.

The following variables are available per participant:

* **`ssp_max_span`**: The primary outcome variable. The longest sequence length successfully recalled.
* **`ssp_current_span_length`**: The difficulty level of the specific round.
* **`ssp_is_correct`**: `1` if the sequence was reproduced correctly, `0` otherwise.
* **`ssp_sequence`**: The target sequence string (e.g., `"0-4-2"`).
* **`ssp_response`**: The user's input string (e.g., `"0-4-5"`).
* **`ssp_rt_seq`**: Timestamps for every single click in the sequence.

## Usage in Your Experiment

1.  Copy the `task_ssp` folder into your oTree project root.
2.  Add the app to your `settings.py` under `SESSION_CONFIGS`.
3.  **Database Reset:** Since this app uses specific field types (`blank=True`, `IntegerField`) to handle the form logic, ensure you run `otree resetdb` after adding it to avoid validation errors.
