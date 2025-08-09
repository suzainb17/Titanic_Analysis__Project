import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folder for graphs
os.makedirs("graphs", exist_ok=True)

# Load dataset
df = pd.read_csv("train.csv")

# Data cleaning
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop('Cabin', axis=1, inplace=True)

# Convert categorical variables
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Graph 1: Survival count
plt.figure()
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.savefig("graphs/survival_count.png")
plt.close()

# Graph 2: Age distribution
plt.figure()
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.savefig("graphs/age_distribution.png")
plt.close()

# Graph 3: Survival by Gender
plt.figure()
sns.barplot(x='Sex', y='Survived', data=df, ci=None)
plt.title('Survival by Gender')
plt.savefig("graphs/survival_by_gender.png")
plt.close()

# Graph 4: Survival by Class
plt.figure()
sns.barplot(x='Pclass', y='Survived', data=df, ci=None)
plt.title('Survival by Class')
plt.savefig("graphs/survival_by_class.png")
plt.close()

# Heatmap (ONLY numeric columns)
numeric_df = df.select_dtypes(include=[np.number]).copy()
if 'PassengerId' in numeric_df.columns:
    numeric_df = numeric_df.drop(columns=['PassengerId'])
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.savefig("graphs/correlation_heatmap.png")
plt.close()

# Insights
insights = [
    "1) More females survived than males.",
    "2) 1st class passengers had higher survival rates."
]

with open("graphs/insights.txt", "w") as f:
    for line in insights:
        f.write(line + "\n")

print("✅ Analysis complete!")
print("📁 All graphs saved in 'graphs' folder.")
print("📝 Insights saved in 'graphs/insights.txt'.")