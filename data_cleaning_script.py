import pandas as pd
# dataset
df = pd.read_csv("netflix_titles.csv")
# basic info
print("Dataset Overview:")
print(df.info())
# first few rows
print("\nFirst 5 rows")
print(df.head())

# missing values
print("\nMissing Values")
print(df.isnull().sum())

# handling missing values (fill or drop)
df.fillna(method='ffill',inplace=True) #forward fill

# df.dropna(inplace=True) # to remove rows with missing values

# standardize text columns
text_columns = ['title','director','cast', 'country', 'rating', 'listed_in', 'description']
for col in text_columns:
    df[col] = df[col].str.lower().str.strip()

# convert date columns to proper format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# detect and remove duplicates
duplicates_count = df.duplicated().sum()
print(f"\nDuplicate Entries Found: {duplicates_count}")
df.drop_duplicates(inplace=True)

# correct numerical columns
df['release_year'] = df['release_year'].astype(int)

# final overview
print("\nCleaned Dataset Info:")
print(df.info())

# cleaned dataset
df.to_csv("Cleaned_netflix_titles.csv",index=False)

print("\nData Cleaning Completed! Cleaned dataset saved as required")
