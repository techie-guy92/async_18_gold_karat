# Gold Price Fetcher in Toman (18 Karat)

## Overview

This project provides two functions to fetch and calculate the price of 18-karat gold in Iranian Toman using data from **tgju.org**. It supports both **synchronous** and **asynchronous** implementations.

## Features

- Fetches live data for gold ounce price and USD exchange rate.
- Supports **requests-cache** for reduced redundant requests.
- Provides both **synchronous** and **asynchronous** versions.
- Implements data validation for robustness.

## Requirements

Make sure you have the following dependencies installed:

```bash
pip install requests requests-cache beautifulsoup4 aiohttp
```

## Usage

### **Function 1 (Synchronous Implementation)**

```python
from gold_price_fetcher import calculate_18k_gold_price_toman_1

price = calculate_18k_gold_price_toman_1()
print(price)
```

**Workflow:**

1. Sends a request to `https://www.tgju.org/`.
2. Extracts the gold ounce price and USD exchange rate.
3. Converts ounce price to 18-karat gold price in toman.
4. Returns formatted output.

### **Function 2 (Asynchronous Implementation)**

```python
import asyncio
from gold_price_fetcher import calculate_18k_gold_price_toman_2

async def main():
    price = await calculate_18k_gold_price_toman_2()
    print(price)

asyncio.run(main())
```

**Workflow:**

1. Uses `aiohttp` for asynchronous requests.
2. Fetches gold ounce price and USD exchange rate.
3. Performs necessary conversions.
4. Returns formatted output.

## Notes

- Function **1** (synchronous) uses `requests-cache` to cache responses for 5 minutes.
- Function **2** (asynchronous) ensures efficient network operations using `aiohttp`.
- Validates extracted values to prevent invalid calculations.

## License

This project is for personal and educational use. Modify it freely!
