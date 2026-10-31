import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Department': ['Cardiology', 'Neurology',
                   'Orthopaedics', 'General Medicine',
                   'Pediatrics', 'Cardiology',
                   'Neurology', 'Orthopaedics'],

    'Patients': [120, 90, 110, 150, 80, 130, 100, 95],

    'Doctors': [10, 8, 9, 12, 7, 10, 8, 9],

    'Revenue': [500000, 350000, 400000, 450000,
                250000, 550000, 380000, 370000],

    'Satisfaction': [4.5, 4.2, 4.3, 4.6,
                     4.7, 4.4, 4.1, 4.5]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.info())
print(df.describe())
df = df.drop_duplicates()

print(df.isnull().sum())

df = df.fillna(0)
performance = df.groupby('Department').agg({
    'Patients': 'sum',
    'Doctors': 'sum',
    'Revenue': 'sum',
    'Satisfaction': 'mean'
})

print(performance)
performance['Patients_per_Doctor'] = (
    performance['Patients'] /
    performance['Doctors']
)

print(performance)
performance['Patients'].plot(
    kind='bar',
    title='Patients per Department',
    color='skyblue'
)

plt.ylabel('Number of Patients')
plt.xlabel('Department')
plt.show()
performance['Revenue'].plot(
    kind='bar',
    title='Revenue per Department',
    color='green'
)

plt.ylabel('Revenue')
plt.show()
performance['Satisfaction'].plot(
    kind='pie',
    autopct='%1.1f%%',
    title='Department Satisfaction'
)

plt.ylabel('')
plt.show()
fig, axes = plt.subplots(2, 2, figsize=(14, 9))

performance['Patients'].plot(
    kind='bar', ax=axes[0, 0],
    title='Total Patients'
)

performance['Revenue'].plot(
    kind='bar', ax=axes[0, 1],
    title='Department Revenue'
)

performance['Satisfaction'].plot(
    kind='bar', ax=axes[1, 0],
    title='Patient Satisfaction'
)

performance['Patients_per_Doctor'].plot(
    kind='bar', ax=axes[1, 1],
    title='Patients per Doctor'
)

plt.tight_layout()
plt.show()
performance.to_excel(
    'Hospital_Performance_Report.xlsx'
)

print("Dashboard created successfully!")