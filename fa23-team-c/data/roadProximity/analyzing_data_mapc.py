import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Redirecting the standard output to a file
with open('../results/output.txt', 'w') as file:
    # Load the dataset
    data = pd.read_csv('/Users/matias/Documents/ds-boston-transit-air-quality/fa23-team-c/data/roadProximity/mapc.health_mapc_ppi_g250.csv')
    
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


        # Create a plain base map of Boston
    plain_map = folium.Map(location=[42.3601, -71.0589], zoom_start=12)  # Latitude and longitude for Boston

    # Save the plain map as an HTML
    plain_map.save("plain_boston_map.html")

    # Printing the location where the plain map is saved
    print("\nPlain map of Boston will be saved as 'plain_boston_map.html'\n", file=file)


    # Create a base map of Boston
    m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)  # Latitude and longitude for Boston

    # Extract the data we'll need for the heatmap
    heat_data = [[row['lat_10'], row['nhoth_10'], row['ppi5']] for index, row in data.iterrows()]

    # Adjusting the gradient for better visualization
    gradient = {0.1: 'blue', 0.3: 'green', 0.5: 'yellow', 0.7: 'orange', 1: 'red'}

    # Create and add the heatmap to our map
    # Adjusting the HeatMap parameters
    HeatMap(
        heat_data,
        radius=15,  # Adjust the radius (default is 25)
        blur=10,   # Adjust the blur (default is 15)
        max_zoom=13  # Adjust the max_zoom (default is 18)
    ).add_to(m)


    # Save the map as an HTML
    m.save("boston_heatmap.html")

    # Printing the location where the heatmap is saved
    print("\nHeatmap of Boston based on PPI will be saved as 'boston_heatmap.html'\n", file=file)
