# Code Commenter Application using DemoGPT

![Code Commenter Logo](logo.png)

The **Code Commenter** application is a tool that utilizes the power of **DemoGPT** to automatically generate detailed comments and explanations for code snippets written in Python. This tool is particularly useful for understanding complex algorithms and logic within functions, enhancing code comprehension, and aiding in the learning process.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Supported Features](#supported-features)
- [Examples](#examples)
- [License](#license)

## Installation

To install the Code Commenter application, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/mgrainger87/PaperSummarizer.git
   ```

2. Navigate to the project directory:

   ```
   cd PaperSummarizer
   ```

3. Install the required dependencies. We recommend using a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Download and configure the DemoGPT model. You can obtain the model from [DemoGPT's official website](https://demogpt.openai.com). Once you have the model, update the configuration in the `config.py` file.

5. Run the application:

   ```
   python app.py
   ```

## Usage

The Code Commenter application is designed to generate comments and explanations for Python code snippets. It takes the code snippets as input and provides detailed comments on the algorithms used in each function.

You can also use the Code Commenter tool with code generated by the ChatGPT code interpreter. Simply provide the generated code as input to the tool, and it will generate comments and explanations for the logic within the generated code.

1. Launch the application by following the installation instructions.

2. Input your Python code snippet into the application, whether it's manually written or generated by ChatGPT.

3. The application will process the input code and generate detailed comments explaining the logic and algorithm within each function.

4. Review the generated comments and gain a better understanding of the code's functionality.

## Supported Features

The Code Commenter application supports the following features:

- **Code Explanation:** Generates human-readable explanations for the logic and algorithm used in Python functions.
  
- **Variable Insights:** Explains the purpose and role of variables within the code snippet.
  
- **Algorithm Details:** Provides step-by-step explanations of complex algorithms.

## Examples

Here's an example of how the Code Commenter application can enhance code comprehension:

### Input Code:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

### Generated Comments:
- The `factorial` function calculates the factorial of a given positive integer `n`.
- It uses a recursive approach to compute the factorial.
- If the input `n` is 0, the function returns 1 as the base case.
- Otherwise, it recursively multiplies `n` with the factorial of `n - 1`.
- This recursive process continues until reaching the base case.
- The function effectively calculates `n!` using recursion.

## License

The Code Commenter application is distributed under the [MIT License](LICENSE).

---

Happy coding and understanding code better with the Code Commenter application!
