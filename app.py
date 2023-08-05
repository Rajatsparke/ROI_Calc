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
        return (hours_per_day/2) *240

yearly_automated_hours = automated_hours(temp_hours)

# Display
#st.write('Yearly Manual Cost: $', yearly_manual_cost)
#st.write('Yearly Automated Cost: $', yearly_automated_cost
#st.metric('My metric', 42, 2)
#st.info(f"{total_savings} $ per year")



#st.write('Total Savings: $', total_savings)

#st.write('Yearly Manual Hours Spent: ', yearly_manual_hours)
#st.write('Yearly Automated Hours Spent: ', yearly_automated_hours)

# Graphs
fig, ax = plt.subplots(2, 1)
# Cost comparison per annum ($)
# Cost comparison per annum ($)
st.header('Cost Comparison per annum')
bars = ax[0].bar(['Automated', 'Manual'], [yearly_automated_cost, yearly_manual_cost])
ax[0].set_title('Cost Comparison per Annum ($)')

# Adding the data value on head of each bar
for bar in bars:
    yval = bar.get_height()
    ax[0].text(bar.get_x() + bar.get_width() / 2, yval + 0.05, round(yval, 2), ha='center', va='bottom')

st.metric(label="Total Savings ($ per year) :", value= total_savings)

# Effort Comparison per annum
st.header('Effort Comparison per annum')
bars = ax[1].bar(['Automated', 'Manual'], [yearly_automated_hours, yearly_manual_hours])
ax[1].set_title('Effort Comparison per annum')

# Adding the data value on head of each bar
for bar in bars:
    yval = bar.get_height()
    ax[1].text(bar.get_x() + bar.get_width() / 2, yval + 0.05, round(yval, 2), ha='center', va='bottom')

plt.tight_layout()
st.pyplot(fig)
