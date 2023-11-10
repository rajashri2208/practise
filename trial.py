import pandas as pd

# Get today's date
today = pd.Timestamp.today().date()

# Calculate the start date of the current quarter
current_quarter_start = pd.Timestamp(today.year, ((today.month - 1) // 3) * 3 + 1, 1).date()

# Calculate the start date of the next quarter
next_quarter_start = current_quarter_start + pd.DateOffset(months=3)

# Format the dates as strings in 'YYYY-MM-DD' format
current_quarter_dates = [date.strftime('%Y-%m-%d') for date in pd.date_range(start=current_quarter_start, periods=7, freq='D')]
next_quarter_dates = [date.strftime('%Y-%m-%d') for date in pd.date_range(start=next_quarter_start, periods=7, freq='D')]

# Print the list of first-week dates for the current and next quarter
print("First week dates for the current quarter:")
print(current_quarter_dates)
print("\nFirst week dates for the next quarter:")
print(next_quarter_dates)
print(today)
for dt in current_quarter_dates:
    if dt==today:
        print(today)
