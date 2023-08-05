import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title('ROI Calculator')

# Sliders
head_count = st.slider('Head Count', 0, 30, 0)
hours_spent = st.slider('Hours spent per person per day', 0, 8, 0)

# Input
hourly_rate = st.number_input('Hourly rate per person ($)', value=0)

# Calculations
yearly_manual_cost = head_count * hours_spent * hourly_rate * 240
yearly_manual_hours = head_count * hours_spent * 240

yearly_automated_cost = 0.1 * yearly_manual_cost

total_savings = yearly_manual_cost - yearly_automated_cost

temp_hours = head_count * hours_spent

def automated_hours(hours_per_day):
    if hours_per_day < 2:
        return 0
    else:
        return (hours_per_day/4) *240

yearly_automated_hours = automated_hours(temp_hours)

# Display
#st.write('Yearly Manual Cost: $', yearly_manual_cost)
#st.write('Yearly Automated Cost: $', yearly_automated_cost
st.metric('My metric', 42, 2)

st.metric(label="'Total Savings: $", value= total_savings)

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
