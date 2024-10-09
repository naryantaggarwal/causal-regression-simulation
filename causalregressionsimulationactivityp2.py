# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import default_rng
from pandas import Series
from pandas import concat
import statsmodels.api as sm

# Helpful in reproducing results
random_seed_id = 42

def simulate_topping_prices(topping="Ketchup", intercept=1.00, slope=0.042, sigma=0.021, num_weeks=56, rng=None):
    if rng == None:
        rng = default_rng()
    epsilons = rng.normal(loc=0, scale=sigma, size=num_weeks)
    times = np.arange(num_weeks)
    prices = intercept + slope * times + epsilons
    return Series(prices, name=f"{topping} Prices")

def simulate_sandwich_sales(ketchup_prices, mustard_prices, intercept=5.00, coeff_ketchup=0.021, coeff_mustard=0.036, sigma=0.001, rng=None):
    if rng == None:
        rng = default_rng()
    if len(ketchup_prices) != len(mustard_prices):
        return None
    epsilons = rng.normal(loc=0, scale=sigma, size=len(ketchup_prices))
    sales = intercept + coeff_ketchup * ketchup_prices + coeff_mustard * mustard_prices + epsilons
    return Series(sales, name="Sandwich Sales")

rng=default_rng(seed=random_seed_id)
ketchup_prices = simulate_topping_prices(topping="Ketchup", intercept=1.50, slope=0.004, sigma=0.02, rng=rng)
mustard_prices = simulate_topping_prices(topping="Mustard", intercept=2.50, slope=0.008, sigma=0.01, rng=rng)
sandwich_sales = simulate_sandwich_sales(ketchup_prices, mustard_prices, rng=rng)
data=concat([sandwich_sales, ketchup_prices, mustard_prices], axis="columns")

prices_data = data[["Ketchup Prices", "Mustard Prices"]]
print(prices_data.head())

x = sm.add_constant(data[["Ketchup Prices", "Mustard Prices"]])
y = data["Sandwich Sales"]
model = sm.OLS(y, x)
fit = model.fit()
print(fit.summary())

print("The `x` values")
print(x.head())
print("The `y` values")
print(y.head())