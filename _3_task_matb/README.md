# Multi-Attribute Task Battery (MATB-II) for oTree

This repository contains a professional, web-based implementation of the **NASA MATB-II** (Multi-Attribute Task Battery) task, specifically designed for integration into **oTree** experiments. The core simulation is powered by a **Unity WebGL** engine.

---

## Purpose and Research Application
This task is specifically designed to study **Mental Workload**, **Multitasking Performance**, and **Mental Fatigue**. 

The MATB-II environment is a highly effective tool for inducing mental fatigue by requiring participants to maintain sustained attention across four distinct tasks. In research settings, it is often used to:
* **Induce Cognitive Fatigue:** By setting the duration up to 10 minutes per round, the task reliably drains executive resources.
* **Measure Performance Degradation:** Researchers can analyze how accuracy and reaction times decrease as mental fatigue sets in.
* **Simulate Real-World Stress:** It mimics high-pressure environments like aviation or control room monitoring where multitasking is critical.

---

## Features
* **Plug-and-Play Integration:** Easily add the MATB-II cockpit simulation to any oTree study.
* **Intelligent Timing:** A JavaScript-based 10-minute timer that starts only *after* the Unity environment has fully loaded and the participant is ready.
* **Instructional Guardrail:** Built-in video tutorial (YouTube-based). The "Next" button only appears once the video has been watched in full.
* **Real-time Data Capture:** Scores from all four subsystems are streamed from Unity to oTree and saved automatically.

---
### Important: Task Duration & Data Saving
The internal Unity simulation is pre-configured for a **10-minute duration**. 

* **Do not shorten the timer:** To ensure that Unity successfully transmits the final performance scores to the oTree database, the task must be completed in full.
* **Technical Reason:** The data bridge (`receivePerformanceData`) is triggered by the Unity engine upon reaching its internal end-of-level state. If oTree terminates the page early (e.g., after only 5 minutes), the scores will remain at `0` because the transmission signal was never sent.
* **Recommendation:** Always keep the `DURATION_SECONDS` in the HTML file at `600` and the oTree `timeout_seconds` at `615` or higher to allow for a safe data transfer.

---

## Subsystems & Scoring
The task requires participants to manage four parallel systems, simulating a cockpit workload environment:

| Subsystem | Priority | Weight | Description |
| :--- | :---: | :---: | :--- |
| **System Monitoring** | 1 | 40% | Responding to warning lights and scale deviations. |
| **Tracking** | 2 | 25% | Keeping a target crosshair centered using a joystick/mouse. |
| **Communications** | 3 | 20% | Setting radio frequencies based on specific callsigns. |
| **Resource Management** | 4 | 15% | Balancing fuel levels across tanks using pumps. |

The `performance_score` is automatically calculated in the `before_next_page` method based on these weights.

## Installation & Setup

### 1. Prerequisites
* oTree (latest version recommended)
* Modern web browser with WebGL support

### 2. File Placement
Copy the contents into your oTree project structure:
* `matb_task/`: The app folder containing `__init__.py`, `MatbTask.html`, `InstructionsMatb.html`, and `Results.html`.
* `_static/matb/Build/`: Ensure this folder contains the Unity-compiled files (`webgl.wasm`, `webgl.data`, `webgl.framework.js`, `webgl.loader.js`).

### 3. Configuration
In your `__init__.py`, you can define the difficulty levels for each round:
```python
LEVELS = ["level1", "level2", "level3", "level4", "level5", "level6"]