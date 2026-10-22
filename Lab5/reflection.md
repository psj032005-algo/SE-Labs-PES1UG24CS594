\# Lab 5: Static Code Analysis — Reflection



\## 1. What is static code analysis, and why is it useful?



Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, maintainability problems, and style violations before the code is delivered.



\## 2. What did Pylint, Bandit, and Flake8 help identify?



Pylint identified code-quality issues such as missing docstrings, poor naming, mutable default arguments, unused variables, and unnecessarily complex conditions. Bandit identified security risks involving `eval()`, MD5, shell execution, and insecure random-number generation. Flake8 identified style and formatting problems.



\## 3. What changes did you make to improve the program?



I replaced `eval()` with a validated discount-rate parameter, replaced MD5 with SHA-256, used the `secrets` module for PIN generation, removed shell execution, and used a context manager with an explicit UTF-8 encoding for file writing. I also corrected function naming, added docstrings, removed unused variables, and fixed the mutable default argument.



\## 4. What did you learn from this lab?



I learned that a program can run successfully and still contain security, maintainability, and style problems. Using multiple static analysis tools provides complementary checks. After making changes, rerunning the tools helps verify that the reported issues have been addressed.

