import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template

data = pd.read_csv('nba_all_star_data.csv')
data = data.dropna()
if data.isnull().sum().sum() == 0:
    print("Data is clean.")
else:
    print("Data is not clean.")

def descriptive_stats(field):
    mean = data[field].mean()
    median = data[field].median()
    std_dev = data[field].std()

    colors = ['red', 'orange', 'yellow']
    plt.bar(['Mean', 'Median', 'Standard Deviation'], [mean, median, std_dev], color=colors)
    plt.title(f"Descriptive Statistics for {field}")
    plt.xlabel("Statistics")
    plt.ylabel("Values")
    #plt.show()

descriptive_stats('fgm')
descriptive_stats('fg3m')
descriptive_stats('ftm')


numerical_fields = ['pts', 'reb', 'ast']

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
colors = ['#552244', '#55254d', '#542957', '#512e61', '#4c336b', '#443875', '#373e7f', '#224488']
for i, field in enumerate(numerical_fields):
    axes[i].hist(data[field], color=colors[i], bins=20)
    axes[i].set_xlabel(field)
    axes[i].set_ylabel('Frequency')
plt.tight_layout()


colors = sns.color_palette("viridis", as_cmap=True)
sns.scatterplot(data, x='reb', y='stl', palette=colors, hue='turnover', legend=False)
plt.xlabel('Average Rebounds per Game')
plt.ylabel('Average Steals per Game')
plt.title('Player Performance: Rebounds vs. Steals')

colors = sns.color_palette("rocket")
sns.scatterplot(data, x='fg_pct', y='fg3_pct', palette=colors, hue='turnover', legend=False)
plt.xlabel('Average Field Goal Percentage')
plt.ylabel('Average Three-Point Field Goal Percentage')
plt.title('Player Shooting Efficiency: FG% vs. 3P%')

#hypothesis: whether there is a significant difference in the average points scored per game between different teams.
team_points = data.groupby('team')['pts'].mean().reset_index()
colors = ['#003f5c', '#444e86','#955196','#dd5182','#ff6e54','#ffa600']
plt.bar(team_points['team'], team_points['pts'], color=colors)
plt.xlabel('Team')
plt.ylabel('Average Points Scored')
plt.title('Average Points Scored by one player per Game by Team')

data['total_fg'] = data['fgm'] + data['fg3m']
data['reb_per_game'] = data['reb'] / data['games_played']

colors = sns.cubehelix_palette(as_cmap=True)
sns.scatterplot(data, x='total_fg', y='reb_per_game', palette=colors, hue='turnover', legend=False)
plt.xlabel('Total field goals made')
plt.ylabel('Rebounds per all games')
plt.title('Rebounds per game against total field goals')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/statistics')
def descriptive_statistics():
    return render_template('statistics.html')

@app.route('/source_code')
def source_code():
    return render_template('source_code.html')

if __name__ == '__main__':
    app.run(debug=True)