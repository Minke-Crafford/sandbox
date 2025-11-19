# Python Project

A simple Python package demonstrating basic structure and best practices.

## Structure

```
python-project/
├── src/
│   ├── mypackage/          # Main package
│   │   ├── __init__.py    # Package initialization
│   │   ├── calculator.py  # Calculator module
│   │   └── utils.py       # Utility functions
│   └── main.py            # Example CLI application
├── tests/                 # Unit tests
│   ├── test_calculator.py
│   └── test_utils.py
└── requirements.txt       # Python dependencies
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Create a virtual environment (recommended):
```bash
cd python-project
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package in development mode:
```bash
pip install -e .
```

Alternatively, add the `src` directory to your Python path:
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/python-project/src"
```

### Running the Application

Run the example CLI application:
```bash
cd src
python main.py
python main.py "Your Name"
```

Run individual modules:
```bash
cd src
python -m mypackage.calculator
python -m mypackage.utils
```

### Testing

Run all tests:
```bash
python -m unittest discover tests
```

Run specific test file:
```bash
python -m unittest tests.test_calculator
```

Run with pytest (if installed):
```bash
pytest tests/
pytest tests/ -v  # Verbose output
pytest tests/ --cov=mypackage  # With coverage
```

### Code Quality

Format code with black:
```bash
black src/ tests/
```

Lint with flake8:
```bash
flake8 src/ tests/
```

Type check with mypy:
```bash
mypy src/
```

## Features

### Calculator Module
- Basic arithmetic operations (add, subtract, multiply, divide)
- Power operation
- Error handling for division by zero

### Utils Module
- Greeting formatter
- Timestamp generation
- Even number checker
- String reversal

## Development

Add your own modules to the `src/mypackage/` directory and corresponding tests to the `tests/` directory.

## Testing

All modules include comprehensive unit tests with good coverage. Tests follow Python's unittest framework and can also be run with pytest.
