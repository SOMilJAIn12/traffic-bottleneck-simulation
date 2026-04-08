#  Traffic Bottleneck Optimization using Simulation

##  Problem Statement

Traffic congestion at bottlenecks (such as lane reductions or intersections) is often caused not just by high vehicle density, but by **unstructured driver behavior**.

When multiple lanes merge into one, lack of coordination leads to inefficiencies, increased waiting time, and reduced throughput.

---

##  Objective

To model and analyze traffic flow at a bottleneck and evaluate different strategies to **reduce congestion and improve efficiency**.

---

##  Approach

We simulate a **2-lane to 1-lane bottleneck system** where:

* Vehicles arrive randomly in both lanes
* Only one vehicle can pass through the bottleneck at a time
* Different merging strategies are applied and compared

---

##  Strategies Implemented

1. **Chaos (Unregulated Merging)**
   Vehicles merge randomly without any rules.

2. **Zipper Merge (Alternating Entry)**
   Vehicles from left and right lanes alternate systematically.

3. **Signal Control (Time-based Flow)**
   Each lane is allowed to pass vehicles in fixed time intervals.

4. **Smart Adaptive Strategy (Proposed)**
   The lane with higher congestion is prioritized dynamically.

---

##  Metrics Used

* **Average Waiting Time**
* **Throughput (Vehicles Passed)**

To ensure reliability, results are **averaged over multiple simulation runs**.

---

##  Results

* Chaotic merging leads to the **highest waiting time** due to conflicts.
* Structured strategies like zipper and signal improve flow efficiency.
* The **adaptive strategy performs best**, reducing congestion significantly by prioritizing overloaded lanes.

---

##  Key Insight

> Unstructured merging significantly increases congestion, while adaptive strategies improve flow efficiency, especially under high traffic conditions.

---

##  Experimental Observations

* Under low traffic, differences between strategies are minimal.
* Under high traffic, adaptive and structured strategies show **clear performance improvements**.
* Results demonstrate the importance of **behavioral coordination in traffic systems**.

---

##Project Report

* Full detailed preliminary report (PDF):
[View Report](https://drive.google.com/file/d/1aRctiU7f11OecbyXNNSrfn_ZASoJOIqE/view?usp=drivesdk)

---

##  How to Run

```bash
pip install -r requirements.txt
```

Open `simulation.ipynb` and run all cells to reproduce results and graphs.

---

##  Project Structure

```bash
traffic-bottleneck-simulation/
│
├── simulation.ipynb
├── utils.py
├── config.py
├── analysis.py
├── results/
│   ├── waiting_time.png
│   ├── throughput.png
│   ├── combined.png
├── requirements.txt
└── README.md
```

---

##  Future Work

* Integrate **Machine Learning** for adaptive traffic signal control
* Use **Computer Vision (OpenCV)** for real-time vehicle detection
* Extend model to multi-intersection urban systems

---

##  Conclusion

This project demonstrates that traffic congestion is not merely a density issue, but a **behavioral coordination problem**.

By introducing structured and adaptive strategies, significant improvements in traffic flow can be achieved.

---
