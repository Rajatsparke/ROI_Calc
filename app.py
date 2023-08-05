import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title('ROI Calculator')

# Sliders
head_count = st.slider('Head Count', 1, 100, 1)
hours_spent = st.slider('Hours spent per person per day', 1, 24, 1)

# Input
hourly_rate = st.number_input('Hourly rate per person ($)', value=10)

# Calculations
yearly_manual_cost = head_count * hours_spent * hourly_rate * 365
yearly_manual_hours = head_count * hours_spent * 365

yearly_automated_cost = 0.1 * yearly_manual_cost

total_savings = yearly_manual_cost - yearly_automated_cost

def automated_hours(yearly_manual_hours):
    if yearly_manual_hours <= 6:
        return 240
    elif yearly_manual_hours <= 14:
        return 480
    elif yearly_manual_hours <= 30:
        return 960
    elif yearly_manual_hours <= 60:
        return 1920
    else:
        # And so on...
        return 0

yearly_automated_hours = automated_hours(yearly_manual_hours)

# Display
st.write('Yearly Manual Cost: $', yearly_manual_cost)
st.write('Yearly Automated Cost: $', yearly_automated_cost)
st.write('Total Savings: $', total_savings)

st.write('Yearly Manual Hours Spent: ', yearly_manual_hours)
st.write('Yearly Automated Hours Spent: ', yearly_automated_hours)

# Graphs
fig, ax = plt.subplots(2, 1)

# Cost comparison per annum ($)
ax[0].bar(['Automated', 'Manual'], [yearly_automated_cost, yearly_manual_cost])
ax[0].set_title('Cost Comparison per Annum ($)')

# Effort comparison per annum (Manhours) 
ax[1].bar(['Automated', 'Manual'], [yearly_automated_hours, yearly_manual_hours])
ax[1].set_title('Effort Comparison per Annum (Manhours)')

plt.tight_layout()
st.pyplot(fig)
