import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

# Constants
ELECTRICITY_FACTOR = 0.0005
NATURAL_GAS_FACTOR = 0.0053
FUEL_FACTOR = 2.32
WASTE_FACTOR = 0.57
BUSINESS_TRAVEL_FACTOR = 2.31

# Gathering inputs from user
def get_inputs():
    print("Enter the details to calculate carbon footprint:\n")
    try:
        
        electricity_cost = float(input("1. Average monthly electricity cost (in euros): "))
        natural_gas_cost = float(input("2. Average monthly natural gas cost (in euros): "))
        fuel_cost = float(input("3. Average monthly fuel cost for transportation (in euros): "))

        waste_generated = float(input("4. Total waste generated per month (in kilograms): "))
        recycling_percentage = float(input("5. Percentage of waste that is recycled/composted: "))
        
        kilometers_traveled = float(input("6. Total kilometers traveled per year for business: "))
        fuel_efficiency = float(input("7. Average fuel efficiency of vehicles (L/100 km): "))
        
        return {
            'electricity_cost': electricity_cost,
            'natural_gas_cost': natural_gas_cost,
            'fuel_cost': fuel_cost,
            'waste_generated': waste_generated,
            'recycling_percentage': recycling_percentage,
            'kilometers_traveled': kilometers_traveled,
            'fuel_efficiency': fuel_efficiency
        }
    except ValueError:
        print("Invalid input! Please enter numerical values.")
        return None