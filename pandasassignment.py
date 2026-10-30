# task 1  Create a NumPy array of integers from 1 to 10 (inclusive).
import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
# ------------------------------------------------
# task 2 Reshape the array from the previous question into a 2x5 matrix.
import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Age': [20, 21, 19, 22],
    'Marks': [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print(df[['Name', 'Age']])
# ------------------------------------------------------------

# task3 Perform element-wise multiplication of two NumPy arrays.
import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha', 'Riya'],
    'Department': ['IT', 'HR', 'IT', 'HR', 'Sales'],
    'Salary': [30000, 25000, 40000, 35000, 28000]
}

df = pd.DataFrame(data)

result = df.groupby('Department')['Salary'].mean()

print(result)
# ---------------------------------------------------------------------

# task4 Create one multidimensional array of shape (3,4,2) and perform indexing and slicing on it.
import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha'],
    'Date': ['2024-05-10', '2024-01-15',
             '2024-03-20', '2024-02-12'],
    'Marks': [85, 90, 78, 88]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

sorted_df = df.sort_values(by='Date', ascending=True)

print(sorted_df)
# -------------------------------------------------------------------------------
# task5Generate a 3x3 matrix with random values between 0 and 1.
import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

df['City'] = ['Ahmedabad', 'Surat', 'Vadodara']

print(df)
# ------------------------------------------------------------------------

# task6 Create two 2D arrays and perform hstack and vstack NumPy operations.
import pandas as pd

data = {
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Age': [20, 21, 19],
    'Marks': [85, 90, 78]
}

df = pd.DataFrame(data)

print("Using loc:")
print(df.loc[0, 'Name'])

print("Using iloc:")
print(df.iloc[0, 0])
# ------------------------------------------------------------------------------