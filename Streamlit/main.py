import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nba_all_star_data.csv')
data = data.dropna()

# Descriptive statistics
def descriptive_stats(field):
    # Calculate mean, median, and standard deviation
    mean = data[field].mean()
    median = data[field].median()
    std_dev = data[field].std()

    # Create a bar plot of the field with different colors
    colors = ['#FF0000', '#FFA500', '#FFFF00']
    local_data = pd.DataFrame(
        {
            'Statistics': ['Mean', 'Median', 'Standard Deviation'],
            'Values': [mean, median, std_dev],
            'Colors': colors,
        }
    )
    st.header(f"Descriptive Statistics for {field}")
    st.bar_chart(local_data, x='Statistics', y='Values', color='Colors')

teams = ["fgm", "fg3m", "ftm"]
team = st.radio('Choose team:', teams)

descriptive_stats(team)

st.header("Numerical fields")
# Select three numerical fields for plotting
numerical_fields = ['pts', 'reb', 'ast']

# Create three subplots for each numerical field
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
# Generate plots for each numerical field
colors = ['#552244', '#55254d', '#542957', '#512e61', '#4c336b', '#443875', '#373e7f', '#224488']
for i, field in enumerate(numerical_fields):
    axes[i].hist(data[field], color=colors[i], bins=20)
    axes[i].set_xlabel(field)
    axes[i].set_ylabel('Frequency')
plt.tight_layout()
st.pyplot(fig)

# Plot 1: Average Rebounds per Game vs. Average Steals per Game

local_data = pd.DataFrame(
    {
        'Average Rebounds per Game': data['reb'],
        'Average Steals per Game': data['stl']
    }
)

st.header('Player Performance: Rebounds vs. Steals')
st.scatter_chart(local_data, x='Average Rebounds per Game', y='Average Steals per Game')

# # Plot 2: Average Field Goal Percentage vs. Average Three-Point Field Goal Percentage
local_data = pd.DataFrame(
    {
        'Average Field Goal Percentage': data['fg_pct'],
        'Average Three-Point Field Goal Percentage': data['fg3_pct']
    }
)

st.header('Player Shooting Efficiency: FG% vs. 3P%')
st.scatter_chart(local_data, x='Average Field Goal Percentage', y='Average Three-Point Field Goal Percentage')

#hypothesis: whether there is a significant difference in the average points scored per game between different teams.
team_points = data.groupby('team')['pts'].mean().reset_index()
# colors = ['#003f5c', '#444e86','#955196','#dd5182','#ff6e54','#ffa600']

st.header('Average Points Scored by one player per Game by Team')
local_data = pd.DataFrame(
    {
        'Team': team_points['team'],
        'Average Points Scored': team_points['pts'],
    }
)
st.bar_chart(local_data, x='Team', y='Average Points Scored')

# Add new columns 'total_fg' and 'reb_per_game'
data['total_fg'] = data['fgm'] + data['fg3m']
data['reb_per_game'] = data['reb'] / data['games_played']

# Plot 'reb_per_game' against 'total_fg'

local_data = pd.DataFrame(
    {
        'Total field goals made': data['total_fg'],
        'Rebounds per all games': data['reb_per_game']
    }
)

st.header('Rebounds per game against total field goals')
st.scatter_chart(local_data, x='Total field goals made', y='Rebounds per all games')
