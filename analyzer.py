import pandas as pd
import numpy as np

# This file is the "brain" of our project. It contains all the 
# logic for cleaning, analyzing, and scoring the data.

def load_data(file_path):
    """Step 1: Just opening the file and bringing it into Python."""
    print(f"--- Loading the data from {file_path}... ---")
    return pd.read_csv(file_path)

def clean_data(df):
    """Step 2: Cleaning up any mess in the data."""
    print("--- Cleaning session started: Fixing missing values... ---")
    
    # Sometimes data has holes (NaN). We'll find them and fill them 
    # with the 'median' (middle) value so our math doesn't break.
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_columns:
        if df[col].isnull().any():
            median_value = df[col].median()
            df[col] = df[col].fillna(median_value)
            print(f"    Fixed missing values in: {col}")
    
    print("--- Cleaning finished! Data is now solid. ---")
    return df

def perform_analysis(df):
    """Step 3: Calculating some interesting stats."""
    print("\n--- Let's look at the averages by Major Category ---")
    
    # We'll group the data to see which categories pay the best on average
    category_summary = df.groupby('Major_category')['Median'].mean().sort_values(ascending=False)
    
    # We only show the top 5 to keep the terminal screen clean
    print(category_summary.head(5))
    
    return category_summary

def calculate_stability_score(df):
    """Step 4: Our custom formula to rank majors by 'Safety'. """
    print("\n--- Calculating Stability Scores for every major... ---")
    
    # We want to know: "High Salary + Low Unemployment = High Stability"
    
    # 1. Normalize Salary (Scale it from 0 to 1)
    # This keeps values fair (e.g., comparing $80,000 to a 0.05 unemployment rate)
    salary_min = df['Median'].min()
    salary_max = df['Median'].max()
    norm_salary = (df['Median'] - salary_min) / (salary_max - salary_min)
    
    # 2. Normalize Unemployment (Scale it, then flip it so 'Low' is 'Good')
    unemp_min = df['Unemployment_rate'].min()
    unemp_max = df['Unemployment_rate'].max()
    norm_unemp = 1 - ((df['Unemployment_rate'] - unemp_min) / (unemp_max - unemp_min))
    
    # 3. Combine them: Salary counts for 60%, Job Safety counts for 40%
    # We multiply by 100 to get a nice score out of 100.
    df['Stability_Score'] = ((norm_salary * 0.6) + (norm_unemp * 0.4)) * 100
    df['Stability_Score'] = df['Stability_Score'].round(2)
    
    # 4. Turn those scores into readable labels
    # High score = Highly Secure, Low score = Volatile
    conditions = [
        (df['Stability_Score'] >= 70),
        (df['Stability_Score'] >= 40),
        (df['Stability_Score'] < 40)
    ]
    labels = ['Highly Secure', 'Stable', 'Volatile']
    
    df['Status'] = np.select(conditions, labels, default='Standard')
    
    return df
