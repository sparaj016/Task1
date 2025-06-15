# Task1 - Data Cleaning and Preprocessing (Netflix Titles)

This task focuses on cleaning and preprocessing the Netflix Titles Dataset using Pandas and Python. The dataset contains information about Netflix shows, including title, release year, director, cast, country, rating, and description.

1. Objective
The goal of this task is to:
- Identify and handle missing values.
- Standardize text formatting for consistency.
- Convert date columns to proper formats.
- Detect and remove duplicate entries.
- Ensure numerical columns have the correct data types.

2. Dataset Overview
The dataset was originally provided in CSV format and contained various inconsistencies, including:
- Missing values in key columns such as director, cast, and country.
- Inconsistent text formatting across categorical columns.
- Date columns stored as strings instead of proper datetime format.
- Duplicate entries affecting data accuracy.

3. Data Cleaning Steps
Step 1: Handling Missing Values
- Used df.isnull().sum() to detect missing values.
- Applied df.fillna(method='ffill') (forward fill) to handle missing values logically.
- Alternative approach: Could have used df.dropna() to remove rows where crucial data was missing.

Step 2: Standardizing Text Columns
- Converted categorical columns to lowercase using .str.lower() and removed leading/trailing spaces with .str.strip().
- Columns cleaned: title, director, cast, country, rating, listed_in, description.

Step 3: Converting Date Columns
- Used pd.to_datetime(df['date_added'], errors='coerce') to format the date_added column correctly.

Step 4: Detecting & Removing Duplicates
- Checked for duplicates using df.duplicated().sum().
- Removed duplicate entries using df.drop_duplicates().

Step 5: Fixing Data Types
- Converted release_year column to integer using df['release_year'].astype(int).
- Ensured proper formatting for all columns.

4. Final Dataset & Output
- The cleaned dataset is saved as "cleaned_netflix_titles.csv".
- All transformations were implemented in data_cleaning_script.py.

5. Acknowledgment
This task is part of an internship data cleaning challenge. The dataset was sourced from Netflix Titles Dataset from Kaggle.



