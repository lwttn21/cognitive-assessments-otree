# Cognitive Assessment Battery (Mental Fatigue Study)

This repository contains a comprehensive battery of oTree-based cognitive tasks and questionnaires specifically curated to study **Mental Fatigue**. It features a high-fidelity **MATB-II** simulation for inducing and measuring cognitive load.

## Background: Mental Fatigue & Cognitive Control
Mental fatigue is a psychobiological state caused by prolonged periods of demanding cognitive activity. It is characterized by feelings of tiredness and a reduced capacity to sustain cognitive performance.

### Why this Battery?
The tests in this repository are designed to quantify how **Mental Fatigue** affects performance. Instead of just measuring subjective "tiredness," these tasks target specific executive functions that degrade under load:

* **Executive Control:** Tasks like *N-Back* or *Stroop* require high-level processing. Fatigue often leads to "task disengagement" as the required mental effort becomes too costly.
* **Sustained Attention:** Long or repetitive tasks (like *Go/No-Go*) test vigilance. We measure "microsleeps" or lapses in attention where the brain fails to react.
* **Multitasking & Resource Allocation:** Using the **MATB-II**, we can observe how fatigue causes "cognitive tunneling," where participants focus on one task while neglecting others.

---

## Project Structure & Task Categories

The apps follow a hierarchical naming convention: `[Category]_[Sub-Category]_[Task_Name]`.

### 1. Objective Performance Tasks (Assessment)
| ID | Category | Task | Folder |
| :--- | :--- | :--- | :--- |
| **1.1** | **Attention & Speed** | Go/No-Go / RTI / RVP | `_1_1_task_...` |
| **1.2** | **Executive Function** | Stroop / Task Switching / TMT A&B | `_1_2_task_...` |
| **1.3** | **Memory** | N-Back / Spatial Span / MOT | `_1_3_task_...` |

### 2. Subjective Questionnaires
| ID | Measure | Description | Folder |
| :--- | :--- | :--- | :--- |
| **2.1** | **MFI** | Multidimensional Fatigue Inventory | `_2_survey_mfi` |
| **2.2** | **VAS** | Visual Analogue Scales (Fatigue/Alertness) | `_2_survey_vas` |

### 3. Complex Multitasking & Fatigue Induction
| ID | Category | Task | Folder |
| :--- | :--- | :--- | :--- |
| **3.1** | **Induction** | **Multi-Attribute Task Battery (MATB-II)** | `_3_task_matb` |

---

## Recommended Experimental Design

To effectively measure mental fatigue, this battery is designed to be integrated into a **Pre-Intervention-Post** paradigm.

### Typical Study Workflow
1. **Baseline Assessment (Pre-Test)**
   * Subjective state using **VAS** or **MFI**.
   * Baseline performance on selected cognitive tasks.
2. **Fatigue Induction (Intervention)**
   * **Task:** Use the **MATB-II** module.
   * **Goal:** A prolonged period (typically 30–60 minutes) of high cognitive load to induce mental fatigue.
3. **Fatigue Assessment (Post-Test)**
   * Repetition of subjective scales and objective tasks to measure performance decrement.

### Visualizing the Cycle



```text
[ START ] 
    |
    v
+-----------------------+      +-----------------------+      +-----------------------+
|  PRE-ASSESSMENT       |      |   FATIGUE INDUCTION   |      |   POST-ASSESSMENT     |
|  (Baseline Metrics)   | ===> |   (e.g., MATB-II)     | ===> |   (Fatigue Metrics)   |
|  - Subjective Scales  |      |   - 30-60 min duration|      |   - Subjective Scales |
|  - Cognitive Tasks    |      |   - High Cognitive Load|      |   - Cognitive Tasks   |
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