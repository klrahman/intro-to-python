## exercise and next steps
# - loads the packages that you will need at the beginning of the script
import pandas as pd
import seaborn as sns


# - adds a season variable
armagh = pd.read_csv('data/armaghdata.csv')

armagh['season'] = '' # initialize an empty string column
armagh.loc[armagh['mm'].isin([1, 2, 12]), 'season'] = 'winter' # if month is 1, 2, or 12, set season to winter
armagh.loc[armagh['mm'].isin(range(3, 6)), 'season'] = 'spring' # if month is 3, 4, or 5, set season to spring
armagh.loc[armagh['mm'].isin(range(6, 9)), 'season'] = 'summer' # if month is 6, 7, or 8, set season to summer
armagh.loc[armagh['mm'].isin(range(9, 12)), 'season'] = 'autumn' # if month is 9, 10, or 11, set season to autumn

# - adds a variable to divide the data into three 50 year periods: 1871-1920, 1921-1970, and 1971-2020
armagh['period'] = '' # initialize an empty string column
armagh.loc[armagh['yyyy'].isin(range(1871, 1921)), 'period'] = '1871-1920' # year is in [1871, 1921)
armagh.loc[armagh['yyyy'].isin(range(1921, 1971)), 'period'] = '1921-1970' # year is in [1921, 1971)
armagh.loc[armagh['yyyy'].isin(range(1971, 2021)), 'period'] = '1971-2020' # year is in [1971, 2021)

# - selects only those observations between 1871 and 2020 (inclusive)
armagh = armagh.loc[armagh.period.isin(['1871-1920', '1921-1970', '1971-2020'])]

# - creates a figure to plot the density distribution of tmin for each period in its own panel, colored by season (using both color and fill)
sep = sns.displot(data=armagh, kind='kde', col='period', hue='season', x='tmin', fill=True)

# - creates a figure to plot the density distribution of tmin for each period in the same panel, colored by the period (using both color and fill)
single = sns.displot(data=armagh, kind='kde', x='tmin', hue='period', fill=True) # plot the density distribution of the data, colored by period, filled in

# - sets appropriate labels and font sizes for the axis text
sep.axes_dict['1871-1920'].set_xlabel('') # remove the xlabel
sep.axes_dict['1921-1970'].set_xlabel('monthly minimum temperature (°C)', fontsize=14) # set the xlabel for the middle panel
sep.axes_dict['1971-2020'].set_xlabel('')
sep.set_ylabels('density', fontsize=14)

single.axes[0, 0].set_xlabel('monthly minimum temperature (°C)', fontsize=14) # set the xlabel for the single axis
single.axes[0, 0].set_ylabel('density', fontsize=14) # set the ylabel for the single axis

# - saves each plot to its own file. For the three-panel figure, make sure to change the width and height of the plot so that the plot is more rectangular, and each panel is approximately square
sep.fig.savefig('tmin_threepanel.svg') # use the fig attribute of a FacetGrid
single.fig.savefig('tmin_onepanel.svg') # for a figure, use savefig directly