# Cognitive Assessment Battery (Mental Fatigue Study)

This repository contains a comprehensive battery of oTree-based cognitive tasks and questionnaires specifically curated to study **Mental Fatigue**.

## Background: Mental Fatigue & Cognitive Control
Mental fatigue is a psychobiological state caused by prolonged periods of demanding cognitive activity. It is characterized by feelings of tiredness and a reduced capacity to sustain cognitive performance.

### The Logic of this Battery
The tests in this repository are designed to target specific components of **Cognitive Control** that are highly sensitive to fatigue:

* **Sensitivity to Effort:** Tasks like *N-Back* or *Stroop* require high executive demand. Fatigued individuals often show a "disengagement" effect, where performance drops as cognitive resources are depleted.
* **Vigilance & Omission:** Long-duration tasks (e.g., *RVP* or *Go/No-Go*) measure the ability to maintain attention over time.
* **Dual-Taxonomy:** By combining **objective performance metrics** with **subjective self-reports**, this battery allows for a holistic analysis of the participant's state.



---

## Project Structure & Task Categories

The apps follow a hierarchical naming convention: `[Category]_[Sub-Category]_[Task_Name]`.

### 1. Objective Performance Tasks
| ID | Category | Task | Folder |
| :--- | :--- | :--- | :--- |
| **1.1** | **Attention & Speed** | Go/No-Go Task | `_1_1_task_go_no_go` |
| | | Reaction Time Task (RTI) | `_1_1_task_rti` |
| | | Rapid Visual Processing (RVP) | `_1_1_task_rvp` |
| **1.2** | **Executive Function** | Stop Signal Task (SST) | `_1_2_task_stop_signal` |
| | | Stroop Color-Word Task | `_1_2_task_stroop` |
| | | Task Switching | `_1_2_task_switching` |
| | | Trail Making Test A | `_1_2_task_tmt_a` |
| | | Trail Making Test B | `_1_2_task_tmt_b` |
| **1.3** | **Memory** | N-Back Task (Working Memory) | `_1_3_task_n_back` |
| | | Spatial Span (SSP) | `_1_3_task_ssp` |
| | | Multiple Object Tracking (MOT) | `_1_3_task_mot` |

### 2. Subjective Questionnaires
| ID | Measure | Description | Folder |
| :--- | :--- | :--- | :--- |
| **2.1** | **MFI** | Multidimensional Fatigue Inventory | `_2_survey_mfi` |
| **2.2** | **VAS** | Visual Analogue Scales (Fatigue/Alertness) | `_2_survey_vas` |

---

## Recommended Experimental Design

To effectively measure mental fatigue, this battery is designed to be integrated into a **Pre-Intervention-Post** paradigm. The primary goal is to capture the performance decline (objective) and the increase in perceived exhaustion (subjective) caused by a demanding cognitive task.

### Typical Study Workflow
A standard experimental session using this repository would follow a structured cycle:

1. **Baseline Assessment (Pre-Test)**
   * Subjective state using **VAS** or **MFI**.
   * Baseline performance on selected cognitive tasks (e.g., **RTI**, **Stroop**, **N-Back**).

2. **Fatigue Induction (Intervention)**
   * A prolonged period (typically 60–90 minutes) of high cognitive load.
   * *Example:* Using the **Multi-Attribute Task Battery (MATB-II)** or a simulated high-demand task.

3. **Fatigue Assessment (Post-Test)**
   * Repetition of subjective scales to measure the change in perceived fatigue.
   * Repetition of objective tasks to measure the **Time-on-Task (ToT)** effect and performance decrement.

### Visualizing the Cycle


```text
[ START ] 
    |
    v
+-----------------------+      +-----------------------+      +-----------------------+
|  PRE-ASSESSMENT       |      |  FATIGUE INDUCTION    |      |  POST-ASSESSMENT      |
|  (Baseline Metrics)   | ===> |  (e.g., MATB-II)      | ===> |  (Fatigue Metrics)    |
|  - Subjective Scales  |      |  - 60-90 min duration |      |  - Subjective Scales  |
|  - Cognitive Tasks    |      |  - High Cognitive Load|      |  - Cognitive Tasks    |
+-----------------------+      +-----------------------+      +-----------------------+
                                                                         |
                                                                         v
                                                                   [ DATA ANALYSIS ]
                                                                 (Delta: Post - Pre)
```
---

##  How to Use

1. **Prerequisites:** Ensure you have Python 3.9+ and oTree 5.x installed.
2. **Setup:** - Clone this repository.
   - Run `pip install -r requirements.txt`.
3. **Run:** Execute `otree devserver` and navigate to the admin interface to start a demo session.

---
## Integration
Each folder is a standalone oTree app. To integrate a task into your own study, copy the folder and add it to your `SESSION_CONFIGS` in `settings.py`.

---
*Developed for research on Mental Fatigue and Cognitive Performance.*