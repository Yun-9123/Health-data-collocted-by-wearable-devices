### EDA, short for "Exploratory Data Analysis"
### Goals : 
1. Data cleaning : check for missing values, and Data Types
2. Univariate analysis : extreme values in Price, Brand proportion in dataset
3. Bivariate analysis : output a scatter plot for relevent between performance score and price, use box plot to compare hardware size in different brands
4. Correlation analysis : draw correlation analysis to find which specifications(battery life, number of sensors) have the greatest impact on performance scores.

### Workflow :
1. Load data "Wearable Health Device Performance Data 2025" from kaggle
* Data stored in ./Data
***
2. Check for missing values
```
------ info ------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2375 entries, 0 to 2374
Data columns (total 17 columns):
 #   Column                           Non-Null Count  Dtype
---  ------                           --------------  -----
 0   Test_Date                        2375 non-null   object
 1   Device_Name                      2375 non-null   object
 2   Brand                            2375 non-null   object
 3   Model                            2375 non-null   object
 4   Category                         2375 non-null   object
 5   Price_USD                        2375 non-null   float64
 6   Battery_Life_Hours               2375 non-null   float64
 7   Heart_Rate_Accuracy_Percent      2375 non-null   float64
 8   Step_Count_Accuracy_Percent      2375 non-null   float64
 9   Sleep_Tracking_Accuracy_Percent  2375 non-null   float64
 10  Water_Resistance_Rating          2375 non-null   object
 11  User_Satisfaction_Rating         2375 non-null   float64
 12  GPS_Accuracy_Meters              1743 non-null   float64
 13  Connectivity_Features            2375 non-null   object
 14  Health_Sensors_Count             2375 non-null   int64
 15  App_Ecosystem_Support            2375 non-null   object
 16  Performance_Score                2375 non-null   float64
dtypes: float64(8), int64(1), object(8)
memory usage: 315.6+ KB
```
```
Column Descriptions
Test_Date: Date of performance evaluation (YYYY-MM-DD)
Device_Name: Full name of the device (Brand + Model)
Brand: Manufacturer of the device
Model: Specific model name
Category: Device type (e.g., Smartwatch, Fitness Tracker)
Price_USD: Retail price in US dollars
Battery_Life_Hours: Battery life (in hours) on a full charge
Heart_Rate_Accuracy_Percent: Heart rate monitoring accuracy (%)
Step_Count_Accuracy_Percent: Step counting accuracy (%)
Sleep_Tracking_Accuracy_Percent: Sleep tracking accuracy (%)
Water_Resistance_Rating: Water resistance certification (e.g., IP68, 5ATM)
User_Satisfaction_Rating: User satisfaction score (1–10 scale)
GPS_Accuracy_Meters: GPS accuracy (in meters, if available)
Connectivity_Features: Supported connectivity options (e.g., Bluetooth, WiFi, NFC, LTE)
Health_Sensors_Count: Number of health-related sensors
App_Ecosystem_Support: Supported app ecosystems (e.g., iOS, Android, Cross-platform)
Performance_Score: Composite performance score (0–100
```
```
df.info()
# Non-Null Count: number of non-null values in each column which is useful for spotting missing data.
```
***
3.
***

### Questions:
1. In the field of health informatics, due to privacy issues (such as the HIPAA legislation), it is very difficult to obtain real patient data. Scientists often use synthetic data to Simulate experiments, and train models