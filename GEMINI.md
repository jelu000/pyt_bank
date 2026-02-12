# Project Overview

This project consists of a Python script designed to analyze transaction data exported from Swedbank. The script, `saldo.py`, utilizes the `pandas` library to read a CSV file of account statements, process the data, and categorize transactions.

The primary function of the script is to distinguish "Swish" transactions from other transactions, presenting a summarized view of both income and expenses. This provides a clear and quick overview of financial activities, tailored for Swedbank's CSV format.

## Building and Running

### Dependencies

The script requires the `pandas` library. To install it, run the following command:

```bash
pip install pandas
```

### Execution

To run the script, execute the following command in your terminal:

```bash
python saldo.py
```

**Note:** The script currently has a hardcoded file path for the CSV file. You will need to edit `saldo.py` to point to the correct location of your transaction file.

## Development Conventions

The code is written in Python and follows standard practices. Key conventions observed in the script include:

-   **Use of Pandas:** The script leverages the `pandas` library for data manipulation, which is a common practice in data analysis with Python.
-   **Clear Variable Naming:** Variables are named descriptively (e.g., `swis_inb`, `icke_swish`) to enhance readability.
-   **Modular Structure:** The core logic is encapsulated within a `main()` function, which is a standard practice in Python for organizing code.
