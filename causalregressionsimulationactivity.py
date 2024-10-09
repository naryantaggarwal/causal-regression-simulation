import numpy as np
from pandas import Series

# Helps in reproducing the scenario
random_seed_id = 42

def generate_ketchup_prices(start=0):
    
    np.random.seed(random_seed_id)

    # Define parameters for generating prices (linear model)
    intercept = 1.50   # Constant term
    slope = 0.042      # Slope coefficient
    sigma = 0.0314     # Standard deviation of noise/error term
    num_weeks = 56     # Number of observations to generate

    # Create an array of times from start to end
    t = np.arange(num_weeks) + start

    # Calculate price values based on linear model
    y = intercept + slope * t

    # Add Gaussian noise to create realistic variation
    epsilon = np.random.normal(loc=0, scale=sigma, size=(len(t),))
    noisy_y = y + epsilon

    return Series(noisy_y, index=range(start, start+num_weeks), name="Ketchup Prices")


def simulate_sales(ketchup_prices, mustard_prices):
    # Import required libraries
    from pandas import Series
    import numpy as np

    np.random.seed(random_seed_id)

    # Define parameters for simulation
    intercept = 5.00
    coef_ketchup = 0.021
    coef_mustard = 0.036
    sigma = 0.0314

    # Calculate total number of simulations (weeks)
    nsimulations = len(ketchup_prices)

    # Simulate sales using random errors and model coefficients
    randn = np.random.normal(loc=0, scale=sigma, size=(nsimulations))
    yhat = intercept + coef_ketchup * ketchup_prices + coef_mustard * mustard_prices + randn

    # Create series object to store results
    return Series(yhat, index=range(len(ketchup_prices)), name="Sandwich Sales")

from pandas import DataFrame
# This is how you would simulate the data for the regression analysis
ketchup_prices = generate_ketchup_prices()
mustard_prices = generate_mustard_prices()
sandwich_sales = simulate_sales(ketchup_prices, mustard_prices)
data = DataFrame({ "Sandwich Sales": sandwich_sales, "Ketchup Prices": ketchup_prices, "Mustard Prices": mustard_prices})
print(data)