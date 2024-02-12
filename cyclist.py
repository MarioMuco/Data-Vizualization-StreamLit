import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Lexo datasetin, low_memory=False nevojitet per datasete te medhaja
rideable_type = pd.read_csv('rideable_type_cyclistic_tripdata.csv', low_memory=False)

# Unifikimi i tipave të të dhënave për kolonën 'total_duration'
rideable_type['total_duration'] = pd.to_timedelta(rideable_type['total_duration']).dt.total_seconds() / 60  # Convert to minutes

# Zëvendëso vlerat NaN me 0 në 'total_duration'
rideable_type['total_duration'].fillna(0, inplace=True)

# Grupiso datasetin sipas rideable_type dhe llogarito mesataren e kohëzgjatjes së udhëtimit për secilin tip
avg_duration_by_type = rideable_type.groupby('rideable_type')['total_duration'].mean()

# Krijimi i Pie Chart
colors = ['#66c2a5', '#fc8d62', '#8da0cb']
fig, ax = plt.subplots()
ax.pie(avg_duration_by_type, labels=avg_duration_by_type.index, autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')  # Renditja e ekipeve të Pie Chart të jetë e drejta

# Shfaq titullin e Pie Chart në Streamlit
average_duration_title = 'Kohëzgjatja e udhëtimit për secilin tip biçiklete'
st.title(average_duration_title)

# Shfaq Pie Chart në Streamlit
st.pyplot(fig)






# Lexo CSV file-in 'member_casual_cyclistic_tripdata.csv'
file_path = 'member_casual_cyclistic_tripdata.csv'
new_df = pd.read_csv(file_path)

# Konverto total_duration në numër (minuta)
new_df['total_duration'] = pd.to_timedelta(new_df['total_duration']).dt.total_seconds() / 60

# Krijo histogramën për kohëzgjatjen e udhëtimit për secilin 'member_casual'
st.title('Kohëzgjatja e udhëtimeve për member dhe casual')
fig, ax = plt.subplots()

colors = ['skyblue' if x == 'member' else 'coral' for x in new_df['member_casual']]
ax.bar(new_df['member_casual'], new_df['total_duration'], color=colors)

ax.set_xlabel('Caual/Member')
ax.set_ylabel('Kohëzgjatja e Udhëtimit (minuta)')
st.pyplot(fig)






# Lexo datasetin
df = pd.read_csv('udhetimet_per_cdo_vit.csv')

# Krijo bar chart me tre ngjyra të ndryshme
fig, ax = plt.subplots()
colors = ['skyblue', 'lightgreen', 'lightcoral']  # Add more colors if needed
ax.bar(df['Viti'], df['Numri i Udhëtimeve'], color=colors)

# Vendos titullin dhe etiketat
st.title('Numri i Udhëtimeve për çdo vit')
ax.set_xlabel('Viti')
ax.set_ylabel('Numri i Udhëtimeve')

# Shfaq bar chart në Streamlit
st.pyplot(fig)



# Assuming 'data' is your DataFrame
data = pd.read_csv("member_casual_counts_per_year.csv")

# Create a color palette with better colors
colors = ['#66c2a5', '#fc8d62']

# Assuming 'data' is your DataFrame
fig, ax = plt.subplots()

# Side-by-side bar chart
data[['casual', 'member']].plot(kind='bar', color=colors, ax=ax, width=0.4, position=1, align='center')

# Set title and labels
st.title('Shpërndarja casual dhe member për çdo vit')
ax.set_xlabel('Viti')
ax.set_ylabel('Numri i Udhëtimeve')

# Set x-axis labels to be the 'year' values
ax.set_xticklabels(data['year'])

# Show the plot in Streamlit
st.pyplot(fig)






# Streamlit app
st.title('Ndryshimi i sasisë së udhetimeve në varësi të vitit')

# Plotting the Line Chart
fig, ax = plt.subplots()

# Plot line for 'casual' trips
ax.plot(data['year'], data['casual'], label='Casual', marker='o')

# Plot line for 'member' trips
ax.plot(data['year'], data['member'], label='Member', marker='o')

# Set title and labels
ax.set_xlabel('Viti')
ax.set_ylabel('Numri i Udhëtimeve')

# Set specific values on the x-axis
ax.set_xticks(data['year'])
ax.set_xticklabels(data['year'])

# Display legend
ax.legend()

# Show the plot in Streamlit
st.pyplot(fig)





# Calculate average duration in minutes
new_df['avg_duration_minutes'] = new_df['total_duration'] / new_df['num_trips']

# Reshape data for heatmap
heatmap_data = new_df.pivot(index='member_casual', columns='num_trips', values='avg_duration_minutes')

# Display the Heatmap using Streamlit
st.title('Heatmap e kohëzgjatjes mesatare së udhëtimeve sipas tipit')

# Plotting the Heatmap
fig, ax = plt.subplots()
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt=".2f", cbar_kws={'label': 'Koha mesatare e çco udhëtimi (minuta)'})

# Show the plot in Streamlit
st.pyplot(fig)





data = pd.read_csv("stacionet_numri.csv")
station_counts = pd.DataFrame(data)

# Sort stations by the number of trips in descending order and select the top 10
top_stations = station_counts.sort_values(by='num_of_trips', ascending=False).head(10)

# Create a bar chart
fig, ax = plt.subplots()
ax.bar(top_stations['start_station_name'], top_stations['num_of_trips'], color='skyblue')

# Set labels and title
ax.set_xlabel('Stacioni i Fillimit')
ax.set_ylabel('Numri i Udhëtimeve')
st.title('10 Stacionet me numrin më të madhë të udhëtimeve')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot in Streamlit
st.pyplot(fig)
