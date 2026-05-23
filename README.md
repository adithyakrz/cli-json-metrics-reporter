#  CLI JSON Metrics Reporter

A lightweight, terminal-based executive dashboard designed to parse local machine learning model configurations and serialize historical metrics. This tool demonstrates core backend Python data engineering foundations by utilizing platform-agnostic file management, robust context execution, and dynamic text streaming.

---

##  Architecture & Module Layout

To break away from static script executions and ensure structured separation of concerns, the workspace separates local database storage from the active processing runtime:

```text
├── metrics.json   # Local Data Ingestion Hub (Stores serialized model metadata)
└── reporter.py    # Core Logic Engine (Parses structures and streams terminal layouts)
```
## Core Engineering Principles Mastered

Secure File Ingestion: Utilizes Python context managers (with open(...)) to establish safe memory streaming pipelines, guaranteeing that system file handles close properly even during an unhandled runtime error.

Data Serialization & Deserialization: Leverages the native json standard library to transform raw characters into native Python dictionaries (json.load), allowing seamless traversal of nested data metrics.

Mathematic Presentation Defenses: Prevents messy raw terminal dumps by using Python f-string formatting syntax ({value * 100:.2f}%). This automatically scales floating-point mathematical metrics (e.g., 0.9256) into rounded, user-friendly percentages (92.56%).

Conditional High-Performance Flags: Features integrated threshold evaluation logic (if accuracy > 0.90) to dynamically flag high-performing model variants directly in the terminal interface.

## Ingestion Blueprint (metrics.json)

The logic engine processes structured machine learning metadata formatted as follows:
```
{
  "project_name": "Deep_CNN_Classifier",
  "framework": "PyTorch 2.5",
  "training_parameters": {
    "epochs": 150,
    "learning_rate": 0.001,
    "batch_size": 32
  },
  "metrics": {
    "accuracy": 0.9425,
    "precision": 0.9180,
    "recall": 0.9312,
    "loss": 0.142
  }
}
```

🚀 How to Run the Tool
Ensure you have Python 3.x installed locally.

Clone this repository or navigate to your local working project directory:

```Bash
cd c:/Files/Code/Python/smallprojects
```

Run the report script via your active terminal shell or Miniconda environment:

```Bash
python reporter.py
```

## Executive Terminal Preview

==================================================
📈 MACHINE LEARNING METRICS REPORT
==================================================
Project Name: Deep_CNN_Classifier
Framework: PyTorch 2.5

[TRAINING PARAMS]
--------------------------------------------------
Epochs: 150
Learning Rate: 0.00100
Batch Size: 32

[EVALUATION METRICS]
--------------------------------------------------
Accuracy: 94.25% * [High Performance Target Cleared]
Precision: 91.80%
Recall: 93.12%
Loss: 0.1420
==================================================
