import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_and_clean_data(filepath):
    """Loads the CSV and drops missing values to ensure data integrity."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset {filepath} not found in the directory.")
    df = pd.read_csv(filepath)
    df_clean = df.dropna().copy()
    print(f"Data loaded successfully. Analyzed records: {len(df_clean)}")
    return df_clean

def analyze_yield_variations(df):
    """Generates a boxplot showing crop yield variations across seasons."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='Season', y='Yield_Tonnes_Ha', palette='Set2')
    plt.title('Crop Yield Variations by Season')
    plt.ylabel('Yield (Tonnes per Hectare)')
    plt.tight_layout()
    plt.savefig('yield_analysis.png', dpi=300)
    plt.close()
    print("- Yield analysis chart saved.")

def analyze_economic_performance(df):
    """Calculates and visualizes the average profit per hectare by season."""
    profit_sum = df.groupby('Season')['Profit_INR'].sum()
    area_sum = df.groupby('Season')['Farm_Area_Hectares'].sum()
    profit_per_ha = profit_sum / area_sum

    plt.figure(figsize=(8, 5))
    profit_per_ha.plot(kind='bar', color=['#4C72B0', '#DD8452', '#C44E52'])
    plt.title('Economic Performance: Profit per Hectare by Season')
    plt.ylabel('Profit (INR)')
    plt.axhline(0, color='black', linewidth=1.2, linestyle='--')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig('economic_performance.png', dpi=300)
    plt.close()
    print("- Economic performance chart saved.")

def analyze_water_efficiency(df):
    """Visualizes the difference in water efficiency across different periods."""
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='Season', y='Water_Efficiency_t_per_1000m3', palette='viridis', errorbar=None)
    plt.title('Water Efficiency Comparison Across Seasons')
    plt.ylabel('Efficiency (Tonnes per 1000m³ water)')
    plt.tight_layout()
    plt.savefig('water_efficiency.png', dpi=300)
    plt.close()
    print("- Water efficiency chart saved.")

def analyze_environmental_impact(df):
    """Explores the relationship between rainfall, season, and yield."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Rainfall_mm', y='Yield_Tonnes_Ha', hue='Season', alpha=0.6)
    plt.title('Relationship Between Rainfall and Crop Yield')
    plt.xlabel('Rainfall (mm)')
    plt.ylabel('Yield (Tonnes/Ha)')
    plt.legend(title='Season')
    plt.tight_layout()
    plt.savefig('environmental_impact.png', dpi=300)
    plt.close()
    print("- Environmental impact chart saved.")

if __name__ == "__main__":
    dataset_file = 'seasonal_agriculture_performance_dataset.csv'
    
    # Execute analytical pipeline
    print("Starting Seasonal Agriculture Analysis Pipeline...")
    clean_data = load_and_clean_data(dataset_file)
    
    analyze_yield_variations(clean_data)
    analyze_economic_performance(clean_data)
    analyze_water_efficiency(clean_data)
    analyze_environmental_impact(clean_data)
    
    print("Analysis complete. All visualizations successfully generated.")
