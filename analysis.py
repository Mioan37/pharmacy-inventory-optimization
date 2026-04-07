import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load the pharmacy inventory dataset from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None

def perform_analysis(df):
    """Perform core inventory analysis: top sellers and reorder needs."""
    # Identify the top 5 products based on sales volume
    top_selling = df.nlargest(5, 'sales')
    
    # Identify products where stock is critically low (e.g., less than 20 units)
    # This helps in preventing stockouts for essential medication
    to_reorder = df[df['stock_level'] < 20]
    
    return top_selling, to_reorder

def plot_sales_by_category(df):
    """Generate and save a bar chart showing total sales per category."""
    plt.figure(figsize=(10, 6))
    df.groupby('category')['sales'].sum().sort_values(ascending=False).plot(kind='bar', color='skyblue')
    
    plt.title('Total Sales Volume by Pharmaceutical Category')
    plt.xlabel('Category')
    plt.ylabel('Units Sold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot as an image to be used in the README.md
    plt.savefig('sales_distribution.png')
    print("Chart saved as 'sales_distribution.png'")
    plt.show()

if __name__ == "__main__":
    # Define the data source
    DATA_FILE = 'pharmacy_inventory_sample.csv'
    
    # Load and process data
    inventory_df = load_data(DATA_FILE)
    
    if inventory_df is not None:
        # Run analysis
        top_5, reorder_list = perform_analysis(inventory_df)
        
        # Display insights in the console
        print("--- Top 5 Best-Selling Products ---")
        print(top_5[['product', 'category', 'sales']])
        
        print("\n--- Critical Stock Levels (Need Reorder) ---")
        if reorder_list.empty:
            print("All stock levels are sufficient.")
        else:
            print(reorder_list[['product', 'stock_level', 'supplier']])
        
        # Visualize the results
        plot_sales_by_category(inventory_df)