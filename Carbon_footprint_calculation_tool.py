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
    
# Calculations
def calculate_emissions(data):
    emissions = {}

    # Energy
    emissions['Energy Usage'] = ((data['electricity_cost'] * 12 * ELECTRICITY_FACTOR) +
                                 (data['natural_gas_cost'] * 12 * NATURAL_GAS_FACTOR) +
                                 (data['fuel_cost'] * 12 * FUEL_FACTOR))

    # Waste
    emissions['Waste'] = data['waste_generated'] * 12 * (WASTE_FACTOR - data['recycling_percentage'] / 100)

    # Business Travel
    emissions['Business Travel'] = (data['kilometers_traveled'] * (1 / data['fuel_efficiency']) * BUSINESS_TRAVEL_FACTOR)

    return emissions

# Recommendations
def generate_recommendations(emissions):
    recommendations = []
    
    if emissions['Energy Usage'] > 1000:
        recommendations.append("Try to use renewable energy sources and use machines and electronics which are efficient and consume less energy.")
    if emissions['Waste'] > 500:
        recommendations.append("Classify the waste and try to implement modern and efficient waste management system.")
    if emissions['Business Travel'] > 1000:
        recommendations.append("Make a campain to use public transport and go for online meetings instead of offline where ever it is possible.")

    if not recommendations:
        recommendations.append("Your carbon footprint is within acceptable limits.")
    
    return recommendations

# Visualization
def create_visualization(emissions):
    categories = list(emissions.keys())
    values = list(emissions.values())

    plt.figure(figsize=(8, 6))
    plt.bar(categories, values, color=['green', 'blue', 'orange'])
    plt.title('Carbon Footprint by Category')
    plt.ylabel('Emissions (kg CO2)')
    plt.tight_layout()
    chart_path = "carbon_footprint_chart.png"
    plt.savefig(chart_path)
    print(f"Visualization saved as {chart_path}")
    plt.show()

    return chart_path

# Function to generate a PDF report
def generate_pdf(emissions, recommendations, chart_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="Carbon Footprint Report", ln=True, align='C')
    pdf.ln(10)

    # Emissions Summary
    pdf.cell(200, 10, txt="Emissions Summary:", ln=True)
    for category, value in emissions.items():
        pdf.cell(0, 10, txt=f"{category}: {value:.2f} kg CO2", ln=True)
    pdf.ln(10)

    # Recommendations
    pdf.cell(200, 10, txt="Recommendations:", ln=True)
    for rec in recommendations:
        pdf.multi_cell(0, 10, txt=f"- {rec}")
    pdf.ln(10)

    # Add Visualization
    pdf.cell(200, 10, txt="See the chart below for visual representation.", ln=True)
    pdf.image(chart_path, x=10, y=None, w=190)

    # Save PDF
    pdf_path = "carbon_footprint_report.pdf"
    pdf.output(pdf_path)
    print(f"PDF report saved as {pdf_path}")