# Causal Regression Simulation Project

This project simulates a causal relationship between the prices of toppings (ketchup and mustard) and sandwich sales over a given period using Python. It demonstrates how changes in input variables (prices) affect the output variable (sales), which is a common application of causal regression in data analysis.

## Prerequisites

- Python 3.x
- Required libraries:
  - `numpy`
  - `pandas`
  - `statsmodels`

You can install the required libraries using the following command:

```bash
pip install numpy pandas statsmodels
```

## Files

### 1. `causalregressionsimulationactivity.py`

This script simulates the price data for two sandwich toppings (ketchup and mustard) and generates sandwich sales data based on these prices. It models the relationship using a linear equation with added noise for realism.

- **Functions:**
  - `generate_ketchup_prices(start=0)`: Generates simulated ketchup prices using a linear model with Gaussian noise.
  - `simulate_sales(ketchup_prices, mustard_prices)`: Simulates sandwich sales based on the prices of ketchup and mustard.

- **Data Generation:**
  - A fixed number of weeks (56 weeks) of data is generated.
  - Prices are modeled as a linear trend with some random noise.
  - Sandwich sales are simulated as a function of ketchup and mustard prices, along with random variation.

- **Output:**
  - A `DataFrame` is created containing simulated sandwich sales, ketchup prices, and mustard prices.
  - The result is printed, showing how sales fluctuate based on changes in prices.

### 2. `causalregressionsimulationactivityp2.py`

This script extends the simulation by allowing further customization of parameters and integrates the **Ordinary Least Squares (OLS)** regression to analyze the relationship between the prices and sales data.

- **Functions:**
  - `simulate_topping_prices(topping, intercept, slope, sigma, num_weeks)`: Generates prices for toppings (ketchup or mustard) using a linear model with random noise.
  - `simulate_sandwich_sales(ketchup_prices, mustard_prices)`: Simulates sandwich sales based on ketchup and mustard prices, with noise for realism.

- **OLS Regression:**
  - The script performs an OLS regression using the `statsmodels` library.
  - The independent variables (`Ketchup Prices` and `Mustard Prices`) are used to predict the dependent variable (`Sandwich Sales`).
  - The regression results, including coefficients, R-squared value, and p-values, are printed.

- **Output:**
  - The script outputs the regression summary, showing the statistical relationship between topping prices and sales.
  - It also prints the first few values of the independent (`x`) and dependent (`y`) variables used in the regression model.

## Running the Scripts

To run the simulations and regression analysis, simply execute the scripts in your Python environment:

```bash
python causalregressionsimulationactivity.py
python causalregressionsimulationactivityp2.py
```

## Summary

This project demonstrates the use of causal regression in a practical scenario by simulating sales data based on the prices of two sandwich toppings. By performing OLS regression, it helps analyze the strength and significance of the relationship between topping prices and sandwich sales, which can be applied in broader business contexts such as pricing strategy and demand forecasting.
