# CampusIQ Acadlytics: Institute Performance Analysis

## 📌 Project Overview
CampusIQ Analytics is a data analytics project focused on evaluating the performance of an educational institute using real-world styled datasets and as per the requirement analyzing institute operations to generate decision-making insights through ETL Power Query and DAX measures as well.      
 The purpose is to integrates multiple data sources—student admissions, certificate records, and student queries—to generate meaningful business insights.

This project demonstrates an end-to-end analytics workflow including data cleaning, transformation, integration, analysis, and visualization using Python, ETL concepts, and Power BI.

---

## 🎯 Objectives
- Analyze student admission trends and course demand
- Evaluate certificate completion rates
- Assess revenue generation and pending fees
- Measure counselor performance
- Understand query sources and student engagement

---

## 🛠️ Tools & Technologies
- **Python** (Pandas, NumPy)
- **Data Visualization** (Matplotlib, Seaborn)
- **Power BI** (for DAX/dashboard creation)
- **Excel** (Data source)

---

## 📂 Raw Dataset Description
The project uses three datasets:

1. **Admission Data**
   - Student ID, Name, Course, Admission Date
   - Fees (Total, Paid, Pending)
   - Payment Mode, Counselor Name

2. **Certificate Data**
   - Student ID, Course Name
   - Certificate Status, Certificate Number
   - Issue Date

3. **Query Data**
   - Query ID, Student Name
   - Course Interested, Query Source
   - Status, Counselor Name

---

## 🔄 Data Processing Steps
- Imported datasets using Pandas
- Removed duplicates and handled missing values
- Fixed data types (especially datetime columns)
- Created new feature: **Certificate Issued (0/1)**
- Merged all datasets into a single unified dataset
- Cleaned and standardized column names
- Exported final dataset for analysis

---

## 📊 Key Insights
- Approximately **50% of students did not receive certificates**
- Significant gap between **fees collected and pending revenue**
- Certain courses show higher demand and enrollment
- Counselor workload distribution is uneven
- Query sources highlight effectiveness of marketing channels

---

## 📈 Visualizations
- Course popularity (Bar Chart)
  
  ![image URL](https://github.com/Sarthak2077/Acadlytics-Performance/blob/main/processed_script/py%20images/Screenshot%202026-03-31%20222546.png)
  
- Fees distribution (Histogram)

  ![image URL](https://github.com/Sarthak2077/Acadlytics-Performance/blob/main/processed_script/py%20images/Screenshot%202026-03-31%20222629.png)

- Certificate status (pie Chart)

  ![image URL](https://github.com/Sarthak2077/Acadlytics-Performance/blob/main/processed_script/py%20images/Screenshot%202026-03-31%20222815.png)
  
- Counselor performance (Count Plot)

  ![image URL](https://github.com/Sarthak2077/Acadlytics-Performance/blob/main/processed_script/py%20images/Screenshot%202026-03-31%20222752.png)
  
- Monthly admission trends (Line Chart)

  ![image URL](https://github.com/Sarthak2077/Acadlytics-Performance/blob/main/processed_script/py%20images/Screenshot%202026-03-31%20222729.png)

---
