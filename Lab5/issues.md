\# Lab 5: Static Code Analysis — Issue Report



| Issue | Type | Line(s) in original code | Description | Fix Approach |

|---|---|---|---|---|

| Shell command execution | Security — High | 58 | `os.system()` executes a shell command using a filename. | Removed shell execution and used `print()` to report the exported filename. |

| MD5 hashing | Security — High | 47 | MD5 is not suitable when a cryptographic hash needs collision resistance. | Replaced MD5 with SHA-256. |

| Dynamic expression evaluation | Security — Medium | 42 | `eval()` executes an expression supplied as a string and can execute unintended code. | Replaced expression evaluation with a numeric discount-rate parameter and validation. |

| Insecure random PIN generation | Security — Low | 51 | `random.randint()` is not intended for security-sensitive random values. | Used `secrets.randbelow()` to generate a four-digit PIN. |

| Mutable default argument | Code quality | 15 | `order\_history=\[]` can share a list between calls. | Changed the default to `None` and initialized the list inside the function. |

| Bare exception handler | Code quality | 26 | A bare `except` can hide unexpected errors. | Caught `KeyError` specifically when the seat does not exist. |

| Incorrect `None` comparison | Code quality | 32 | Compared a value to `None` using `==`. | Used `is None` and simplified the availability check. |

| Missing function documentation | Code quality | Multiple | Several functions lacked docstrings. | Added docstrings describing each function's purpose. |

| Naming and formatting issues | Style | Multiple | The original code had a non-snake-case function name and formatting issues. | Renamed the function and corrected formatting. |

| Unspecified file encoding | Code quality | 55 | File writing did not explicitly specify an encoding or use a context manager. | Used `with open(..., encoding="utf-8")`. |

| Hardcoded secret | Security | 75 | A token-like value was embedded in the source code and printed. | Removed the hardcoded token and its print statement. |



\## Verification



\- Bandit: no issues identified in the final scan.

\- Pylint: 10.00/10.

\- Flake8: no reported issues in the final scan.

