# eburke090-inst414-final-project-Elle-Burke
LA Crime Data Analysis

# SETUP INSTRUCTIONS 
1) Clone the repository 
2) install dependecies using pip install -r requirenments.txt
3) run the whole project with ETL, analysis, and visualziaotn pipeline 

# BUSINESS PROBLEM
The LAPD aims to reduce response times and optimize the allocation of its patrol resources. THis project aims to build a model that can preduct and identify crime hotspots by location and time using previous crime reports


# DATA SETS USED
**Crime Data from 2020 to Present**  
    Source: data.gov (https://catalog.data.gov/dataset/crime-data-from-2020-to-present) 
    Format: CSV  
    Characteristics:
    - Structured tabular format
    - Grows over time
    - Contains fields like date, time, location, crime type, and more


# TECHNIQUES EMPLOYED 

**Data Engineering:**
    - VS Code with SQL Server extension to interact with the database

**Data Analysis & Modeling:**
    - Physical analysis (times of day)
    - Geogrpahical clustering (crime density by area)

# EXPECTED OUTPUTS

A product that:
    - Ingesets LAPD crime data
    - Cleans and stores it in a cloud SQL database
    - Allows for exploratory queries and futher analysis
    - Lays the foudnation for future predictive modeling 

# NOTES
Due to GitHub's 100MB file limit, raw datasets are not stored in the repo.
Please download the CSV manually from the [LAPD Crime Data Portal](https://catalog.data.gov/dataset/crime-data-from-2020-to-present) and save it in `data/raw/'