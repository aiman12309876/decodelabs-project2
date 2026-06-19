import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_sample_data():
    np.random.seed(42)
    data = {
        'Age': np.random.randint(18, 60, 100),
        'Salary': np.random.randint(30000, 90000, 100),
        'Experience': np.random.randint(0, 25, 100),
        'Education_Score': np.random.randint(4, 10, 100),
        'Department': np.random.choice(['IT', 'HR', 'Finance', 'Marketing'], 100),
        'Satisfaction': np.random.randint(1, 10, 100)
    }
    return pd.DataFrame(data)

def perform_eda(df):
    print("\n" + "=" * 60)
    print("   EXPLORATORY DATA ANALYSIS (EDA)")
    print("=" * 60)

    print("\n[1] Dataset Overview:")
    print("-" * 40)
    print(f"Total Rows: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]}")
    print("\nFirst 5 rows:")
    print(df.head())

    print("\n[2] Data Types and Missing Values:")
    print("-" * 40)
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\n[3] Descriptive Statistics:")
    print("-" * 40)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print(df[numeric_cols].describe())

    print("\n[4] Categorical Analysis:")
    print("-" * 40)
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        print(f"\n{col} Distribution:")
        print(df[col].value_counts())

    print("\n[5] Identifying Outliers (IQR Method):")
    print("-" * 40)
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        print(f"{col}: {len(outliers)} outliers")

    print("\n[6] Key Insights:")
    print("-" * 40)
    print("Average Age:", df['Age'].mean())
    print("Average Salary:", df['Salary'].mean())
    print("Average Experience:", df['Experience'].mean())
    print("Average Satisfaction:", df['Satisfaction'].mean())
    print("Most Common Department:", df['Department'].mode().iloc[0])
    print("\nCorrelation between Age and Salary:", df['Age'].corr(df['Salary']))

    print("\n" + "=" * 60)
    print("   EDA COMPLETE")
    print("=" * 60)

    return numeric_cols

def plot_visualizations(df, numeric_cols):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    axes[0, 0].hist(df['Age'], bins=10, color='blue', edgecolor='black')
    axes[0, 0].set_title('Age Distribution')
    axes[0, 0].set_xlabel('Age')
    axes[0, 0].set_ylabel('Frequency')

    axes[0, 1].hist(df['Salary'], bins=10, color='green', edgecolor='black')
    axes[0, 1].set_title('Salary Distribution')
    axes[0, 1].set_xlabel('Salary')
    axes[0, 1].set_ylabel('Frequency')

    axes[1, 0].boxplot(df['Satisfaction'])
    axes[1, 0].set_title('Satisfaction Box Plot')
    axes[1, 0].set_ylabel('Satisfaction Score')

    dept_counts = df['Department'].value_counts()
    axes[1, 1].bar(dept_counts.index, dept_counts.values, color='purple')
    axes[1, 1].set_title('Department Distribution')
    axes[1, 1].set_ylabel('Count')

    plt.tight_layout()
    plt.show()

def main():
    df = create_sample_data()
    numeric_cols = perform_eda(df)
    plot_visualizations(df, numeric_cols)

if __name__ == "__main__":
    main()