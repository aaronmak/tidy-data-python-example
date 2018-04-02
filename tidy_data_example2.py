import matplotlib.pyplot as plt
import pandas as pd

# Only looking at 2010 for the example
un_dataframe = pd.read_excel(
    'UN_MigrantStockByOriginAndDestination_2015.xlsx',
    sheet_name='Table 15',
    skiprows=15
)

# Rename columns that are missing column labels
un_dataframe.rename(
    columns={
        'Unnamed: 3': 'Destination Country Code',
        'Unnamed: 1': 'Destination Country'
    },
    inplace=True
)

# Filter out regions and total
un_dataframe = un_dataframe[un_dataframe['Unnamed: 4'].notna()]

# Drop unused columns
un_dataframe.drop(['Unnamed: 0', 'Unnamed: 2', 'Unnamed: 4', 'Total'],
                  axis=1,
                  inplace=True)

# Reshape origin countries to a column using melt
un_dataframe = un_dataframe.melt(
    id_vars=['Destination Country', 'Destination Country Code'],
    value_name='People',
    var_name='Origin Country'
)

# Plot bar chart of top origin countries to Singapore

singapore_migrants = un_dataframe[
    un_dataframe['Destination Country'] == 'Singapore'
]

# Get top 10 origin countries by People
singapore_migrants_top_origin = singapore_migrants.sort_values(
    'People', ascending=False
).head(10)

# Reduce country name length for bar chart
singapore_migrants_top_origin['Origin Country'].replace(
    to_replace='China, Hong Kong Special Administrative Region',
    value='Hong Kong',
    inplace=True
)

singapore_migrants_top_origin.plot.bar(
    x='Origin Country',
    y='People',
    title='Origin Countries of Migrants to Singapore in 2010')

plt.tight_layout()
plt.savefig('top_origin_countries_migrants_singapore_2010.png',
            dpi=150)
