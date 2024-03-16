import pandas as pd
import os
from pathlib import Path

# # Get the user's home directory
# user_home = os.path.expanduser("~")

# # Specify the directory where the Excel file is located
# directory = os.path.join(user_home, "Documents")

# # Specify the filename
# filename = "data.xlsx"

# # Construct the full path to the Excel file
# excel_file = os.path.join(directory, filename)
# aa = str("r" + excel_file)
# print(aa)
# # Load the Excel file into a Pandas DataFrame
# df = pd.read_excel(aa)

# # Display the DataFrame
# # print(df)
path = Path("~/Documents/data.xlsx")
print(path)
df = pd.read_excel(path)
print(df)
