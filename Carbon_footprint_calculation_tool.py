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

