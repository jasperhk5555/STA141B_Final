# STA141B_Final - Jasper Cheng & Jose Lopez
## Analysis on Top 200 Spotify Charts from 2017 to 2020 in the Americas
### Project Description
For our project we wanted to investigate the characteristics of songs in the Top 200 Charts of Spotfiy for all countries in the Americas. By using the Spotify API and manipulating every Top Chart's data, we were able to extract the data needed for our analysis. We focused on the genre, danceability, energy, and acousticness of a song. We analyzed the  danceability, energy, and acousticness of Top 200 Chart songs of all countries with three separate plots of the correlation between song feature and chart rank to find the trends in song features over time. We also plotted the top five genre streams over time to see the rise and fall in popularity of Top 200 Chart songs genres. Lastly, we conducted Rank Biased Overlap (RBO) to measure similarity of Top 200 Charts between teo countries through the dates 2017-2020. We chose to analyze the RBO of United States and Canada as well as United States and Mexico to view the difference in Top 200 charts of neighboring countries. We created an interactive plot to visualize the popularity of Song, Genre, and Artist among the Top 200 Charts of all countries through all dates between 2017 and 2020. The user is able to select the date as well as frequency (weekly, monthly, yearly) of the top Song, Genre, or Artist.

### Flies
#### data directory
Our data directory contains all of our necessary data for the analysis. The following is a list of all the csv files with a brief description.
- artistsdata: all unique artists 2017-2020 and their respective genre.
- genredata: streams of each unique genre 2017-2020
- countriesdata: the unique countries and their region code
- correlationsdata: the correlation between song feature and song rank 2017-2020 for all countries
- topYYYYMMDD-YYYMMDD: Top 200 Chart data for respective date 
- songsdata: all unique songs and respective features from Top 200 Charts 2017-2020
- top200data: all songs and ranks of Top 200 Charts for all countries 2017-2020
#### notebooks directory
Our notebook directory contains all notebooks used for analysis as well as our Report notebook. The  following is a list of all notebooks ad their descriptions.
- Artists : used to find the unique artists and their respective genres from Spotify API
- Dash : used to create interactive plot
- Report : contains our final report of our project along with necessary graphs.
- StaticPlots : contains the the code used to create all static plots
- Songs: used to obtain all song data as well as song features
- top200data: used to obtain al Top 200 charts for all countries
#### code directory
The code directory contains a file named functions.py that contains the functions we used for the coding in our analysis.
