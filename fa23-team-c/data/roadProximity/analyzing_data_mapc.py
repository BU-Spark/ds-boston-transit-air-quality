import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Redirecting the standard output to a file
with open('../results/output.txt', 'w') as file:
    # Load the dataset
    data = pd.read_csv('/Users/matias/Documents/ds-boston-transit-air-quality/fa23-team-c/data/mapc.health_mapc_ppi_g250.csv')
    
    # Display a clean header for the top 5 rows
    print("\n======= Top 5 rows of the Dataset =======\n", file=file)
    print(data.head(), file=file)
    
    # Summary statistics
    print("\n======= Summary Statistics =======\n", file=file)
    # Rounding the describe output to 2 decimal places for better readability
    print(data.describe().round(2), file=file)
    
    # Display a clean message for saved images
    print("\nDistribution of Pollution Proximity Index will be saved as 'ppi_distribution.png'\n", file=file)
    
    # Visualize distribution of Pollution Proximity Index
    plt.figure()
    sns.histplot(data['ppi5'])
    plt.title('Distribution of Pollution Proximity Index')
    plt.savefig('ppi_distribution.png')  # Saving the plot as an image
    
    # Check average PPI based on commute type
    avg_ppi_by_commtype = data.groupby('commtype')['ppi5'].mean().round(2)
    print("\n======= Average PPI by Commute Type =======\n", file=file)
    print(avg_ppi_by_commtype, file=file)
    
    # Display a clean message for saved images
    print("\nAverage PPI by Commute Type will be saved as 'avg_ppi_by_commtype.png'\n", file=file)
    
    # Plot the above
    plt.figure()
    avg_ppi_by_commtype.plot(kind='bar')
    plt.title('Average PPI by Commute Type')
    plt.ylabel('Average PPI')
    plt.savefig('avg_ppi_by_commtype.png')  # Saving the plot as an image
