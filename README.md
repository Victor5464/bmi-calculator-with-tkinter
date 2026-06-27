# BMI Calculator

A lightweight, high-performance graphic user interface(GUI) built in Python to calculate Body Mass Index (BMI). This tool processes weight and height inputs, computes the BMI score, and provides instant health classifications based on World Health Organization (WHO) standards.

## Features

* **Instant Classification:** Automatically categorizes BMI results (Underweight, Normal, Overweight, Obese).
* **Input Validation:** Built-in error handling to prevent crashes from invalid numeric entries or text.
* **Clean GUI Output:** Intuitive, simple feedback from tkinter.

---

## BMI Classification Reference

The application determines health categories based on the following standard ranges:

| BMI Range | Classification |
| :--- | :--- |
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal Weight |
| 25.0 – 29.9 | Overweight |
| 30.0 and Above | Obese |

---

## Getting Started

### Prerequisites
* Python 3.8 or higher installed on your system.

### Installation
1. Clone the repository to your local machine:
   ```bash
   cd bmi-calculator

2. Navigate into the project directory:
   ```bash
   git clone [https://github.com/yourusername/bmi-calculator.git](https://github.com/yourusername/bmi-calculator.git)


### Running the Application
* Launch the script directly from your terminal:
    ```bash
    python bmi_calculator.py


## With uv

Install uv (if you do not have it):

* On macOS/Linux
    ```bash
    curl -LsSf https://astral.sh | sh

* On Windows
    ```bash
    powershell -c "irm https://astral.sh | iex"

* Run the project instantly:
    ```bash
    uv run main.py


### License
    This project is open-source and available under the MIT License.