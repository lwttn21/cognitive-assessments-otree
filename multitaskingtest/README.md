# oTree Multitasking Test (MTT)

This repository contains an **oTree implementation of a CANTAB-like Multitasking Test (MTT)**.
The task is inspired by the Multitasking Test of the **Cambridge Neuropsychological Test Automated Battery (CANTAB)** and is intended **for research and educational purposes only**.

---

## 📌 Task Description

In each trial, an arrow is presented that:
- appears either on the **left or right side** of the screen
- points either **left or right**

At the top of the screen, a **cue** indicates the currently relevant rule:
- **SIDE**: respond according to the side on which the arrow appears
- **DIRECTION**: respond according to the direction in which the arrow points

Participants respond using the **left and right arrow keys**.

---

## 🧠 Cognitive Processes Assessed

The task assesses:
- Multitasking ability
- Task switching
- Cognitive control
- Interference processing (Stroop-like effects)

Both **congruent** (e.g., arrow on the right pointing right) and **incongruent** trials are included.

---

## 🧪 Experimental Structure

- Implemented using **oTree 5**
- **Single oTree round**
- All trials are administered on a **single page using JavaScript**
  - avoids latency caused by page reloads
- Typical structure:
  - First block: single-task (fixed rule)
  - Second block: multitasking (random rule switching)

---

## 📊 Outcome Measures

For each trial, the following variables are recorded:
- Reaction time (ms)
- Accuracy (correct / incorrect)
- Task rule (SIDE vs. DIRECTION)
- Arrow side
- Arrow direction
- Congruency (congruent vs. incongruent)

All trial-level data are stored as a **JSON string** in the oTree dataset and can be exported for further analysis.

---

## 📁 Project Structure

