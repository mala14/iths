import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# The file path
file_path = '../Study/Labs/Weather/data/' 

# Read csv files to gather weather info
humi = pd.read_csv(f'{file_path}smhi-opendata_humidity_blge.csv') # Humidity
prec = pd.read_csv(f'{file_path}smhi-opendata_precipitation_blge.csv') # Precipitation
temp = pd.read_csv(f'{file_path}smhi-opendata_temp_blge.csv') # Temperature

# Select columns to use from humidity, precipitation and temperature
df_hum = humi[['Datum', 'Tid (UTC)', 'Relativ Luftfuktighet']]
df_pre = prec[['Datum', 'Tid (UTC)', 'Nederbördsmängd']]
df_temp = temp[['Datum', 'Tid (UTC)', 'Lufttemperatur']]

# Create a complete timestamp range
humi['Datum'] = pd.to_datetime(humi['Datum'])
prec['Datum'] = pd.to_datetime(prec['Datum'])
temp['Datum'] = pd.to_datetime(temp['Datum'])

full_timestamp_range = pd.date_range(start=min(humi['Datum']), end=max(humi['Datum']), freq='H')

# Create DataFrames with complete timestamp range
full_humi = pd.DataFrame({'Datum': full_timestamp_range})
full_prec = pd.DataFrame({'Datum': full_timestamp_range})
full_temp = pd.DataFrame({'Datum': full_timestamp_range})

# Merge existing data with complete timestamp range
humi = pd.merge(full_humi, humi, on='Datum', how='left')
prec = pd.merge(full_prec, prec, on='Datum', how='left')
temp = pd.merge(full_temp, temp, on='Datum', how='left')

# Merge dataframes
merged_df = pd.merge(df_hum, df_pre, on=['Datum', 'Tid (UTC)'], how='outer')
merged_df = pd.merge(merged_df, df_temp, on=['Datum', 'Tid (UTC)'], how='outer')

# Fill missing values with forward 'ffill' values
merged_df = merged_df.ffill()

# Convert 'Datum' and 'Tid (UTC)' to datetime format
merged_df['Datum'] = pd.to_datetime(merged_df['Datum'] + ' ' + merged_df['Tid (UTC)'])
# Create a complete timestamp range
full_timestamp_range = pd.date_range(start=merged_df['Datum'].min(), end=merged_df['Datum'].max(), freq='H')

# Create DataFrame with complete timestamp range
full_timestamp_df = pd.DataFrame({'Datum': full_timestamp_range})
# Merge with complete timestamp range
merged_df = pd.merge(full_timestamp_df, merged_df, on='Datum', how='left')

# Select features and target variable
X = merged_df[['Lufttemperatur', 'Nederbördsmängd']]
y = merged_df['Relativ Luftfuktighet']

# forwardfill missing values
X = X.ffill() # temp & precipitation
y = y.ffill() # humidity


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0032, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')
