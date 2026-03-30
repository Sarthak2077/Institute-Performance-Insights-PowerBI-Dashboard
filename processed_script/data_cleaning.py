import pandas as pd
import numpy as np

admission = pd.read_excel("C:/Users/Sarthak Yadav/Downloads/Admission_Data_Generated.xlsx")
certificates = pd.read_excel("C:/Users/Sarthak Yadav/Downloads/Certificate_Data_Generated.xlsx")
queries = pd.read_excel("C:/Users/Sarthak Yadav/Downloads/Query_Data_Generated.xlsx")
print(certificates.head())
print(admission.head())
print(admission.info())
print(admission.describe())

# Remove duplicates
admission.drop_duplicates(inplace=True)
certificates.drop_duplicates(inplace=True)
queries.drop_duplicates(inplace=True)

# Handle missing values
print(admission.isnull().sum())
print(certificates.isnull().sum())
print(queries.isnull().sum())


# Fix certificate number
certificates['Certificate No'] = certificates['Certificate No'].fillna("Not Issed")

# Keep Issue Date as datetime (no string fill)
# (optional but safe)
certificates['Issue Date'] = pd.to_datetime(certificates['Issue Date'], errors='coerce')

# Create new column
certificates['Certificate Issued'] = certificates['Issue Date'].notna().astype(int)
print(certificates.head())
print(certificates['Certificate Issued'].value_counts())

merged = admission.merge(certificates, on='Student ID', how='left')
merged = merged.merge(queries, left_on='Student Name_x', right_on='Student Name', how='left')
print(merged.columns)

merged.rename(columns={
    'Student Name_x': 'Student Name',
    'Course Name_x': 'Course Name',
    'Counselor Name_x': 'Counselor Name'
}, inplace=True)


merged.drop(columns=[
    'Student Name_y',
    'Course Name_y',
    'Counselor Name_y'
], inplace=True)


print(merged.columns)
print(merged.shape)
print(merged.head())

print("Total Revenue:", merged['Fees Paid'].sum())
print("Pending Revenue:", merged['Fees Pending'].sum())

print(merged['Certificate Issued'].value_counts())
print(merged['Course Name'].value_counts())
print(merged['Counselor Name'].value_counts())


print(merged['Query Source'].value_counts())
print(merged['Status'].value_counts())

conversion = merged['Certificate Issued'].mean() * 100
print("Conversion Rate:", conversion)

import matplotlib.pyplot as plt

merged['Course Name'].value_counts().head(3).plot(kind='bar')
plt.title("Course Popularity")
plt.xticks(rotation=45)
plt.show()

import seaborn as sns

# Set style (WRITE HERE ✅)
sns.set(style="whitegrid")

# Your plots below
sns.histplot(merged['Fees Paid'], kde=True)
plt.title("Fees Paid Distribution")
plt.show()


sns.boxplot(x='Course Name', y='Fees Paid', data=merged)
plt.xticks(rotation=45)
plt.title("Fees Paid by Course")
plt.show()

# Create year-month column
merged['YearMonth'] = merged['Admission Date'].dt.to_period('M')

# Count admissions per month
trend = merged.groupby('YearMonth')['Student ID'].count()

# Plot
trend.plot(kind='line', marker='o')
plt.title("Monthly Admission Trend")
plt.xticks(rotation=45)
plt.show()

sns.countplot(y='Counselor Name', data=merged, order=merged['Counselor Name'].value_counts().index)
plt.title("Counselor-wise Student Handling")
plt.show()

cert_counts = merged['Certificate Issued'].value_counts()

plt.pie(cert_counts, labels=['Issued', 'Not Issued'], autopct='%1.1f%%')
plt.title("Certificate Distribution")
plt.show()

avg_fees = merged.groupby('Course Name')['Fees Paid'].mean().sort_values()

sns.barplot(x=avg_fees.values, y=avg_fees.index)
plt.title("Average Fees Paid by Course")
plt.xlabel("Average Fees Paid")
plt.ylabel("Course")
plt.show()

top_courses = merged['Course Name'].value_counts().tail(2).index

filtered = merged[merged['Course Name'].isin(top_courses)]

sns.boxplot(x='Course Name', y='Fees Paid', data=filtered)
plt.xticks(rotation=45)
plt.title("Fees Distribution (bottom 2 Courses)")
plt.show()

revenue = merged.groupby('Course Name')['Fees Paid'].sum().sort_values()

revenue.plot(kind='barh')
plt.title("Total Revenue by Course")
plt.xlabel("Revenue")
plt.show()

