# Project 1 - An Analysis on the Canadian Cannabis Industry 
## __Overview__
5 topics for this Canadian Cannabis Industry EDA project were identified and included the analysis of market trends, product trends, and changes in cannabis use amongst different demographics during different time periods. 

## __Topics Covered__
- Topic 1: Cannabis Recreational Store Growth Analysis in Canada
- Topic 2: Retail vs Medical Stores Growth
- Topic 3: Cannabis Market Share by Product Type
- Topic 4: Yearly Cannabis Use Change by Gender: 2017 to 2022
- Topic 5: Topic 5: Cannabis Use Change during First Wave of the Covid Pandemic Analyzed by Age Group, Ethnicity, and Income Level (May 2020 to March 2021)

## __Data__
- Topics 1, 2, and 3 use the same dataset, which consists of 327 observations and is obtained from the Government of Canada. Observation collected from late 2019 to 2023.
- The Topic 4 dataset consists of a merged database of several Canadian Cannabis Survey responses from 2017 to 2022. Due to the significant amount of information in these reports, Table 1 from each report was extracted and merged into a single data table for the analysis of cannabis use by gender. 
    - Limitations:  

            - Population was rounded to the nearest 1000, so numbers may be slightly off.

            - As survey responses were voluntary, not all users/non-users are being accurately represented by the sample.

            - 2023 survey data not available yet.

- The Topic 5 dataset consists of the approximately 6000+ survey responses collected in the “Alcohol and cannabis use during the COVID-19 pandemic” survey by BMC Public Health. The dataset has been filtered for only the cannabis-use related columns. Please note that this dataset contains qualitative responses regarding changes in cannabis use, which is subjective and may not accurately portrait just how cannabis use has increased or decreased during the pandemic.
    - Limitations:  
    
            - Survey responses composed of qualitative data that was subjective, which may not be entirely accurate and consistent amongst respondents.

            - More responses were received from younger age groups, which is not representative of the entire population.

            - Other factors such as daily habit changes and stress factors were not considered in the data collection.



## __Repo Contents__
- *Individual Code Files*
    - This folder contains each individual code file that was used to analyze the different topics/questions outlined in this Canadian Cannabis Industry EDA project. 
- *Resources*
    - This folder contains the csv files used for each of the analyzes, as well as the original data sources for the datasets. 
- *Project1_ConsolidatedFinalAnalysis*
    - This is the final consolidated code file containing everyone's code, analysis, and conclusions. 
- *README*
    - This README file provides an overview on this project and helps to instruct individuals on how to replicable the analysis for their on exploration. 


## __Requirements and Dependencies__
- *Language*
    - Python
- *Libraries and dependencies*
    - Pandas
    - Seaborn
    - Pathlib
    - Matplotlib.pyplot 
    - Numpy
    - Pandas.api.types 

## __Replication Instructions__
- Download any dependencies you are missing before running to ensure the code can run successfully. 
- Run the Jupyter notebook to replicate the analysis or modify it for further exploration. 

## __Code Contents__
- *Data Import and Cleaning*
    - File paths are defined and the datasets are imported and cleaning for the analysis. This entails addressing missing values, converting data types, and filtering for only the columns necessary for the analysis.
- *Data Visualizations* 
    - Line, bar, pie, and donut charts were generated to visualize various trends regarding inventory, revenue, product sales, and changes in cannabis use. 
- *Analysis and Conclusions*
    - Observations of any trends in the visuals were recorded and analyzed to understand the state of the current cannabis market and to forecast how these trends will change in the future. 

__Presentation Slides:__ Link to our Google Slides can be found here: https://docs.google.com/presentation/d/1hPuJYQMzc5No5I1QY2sbJITpJs06i0Ucr8U8OEDyDyk/edit?usp=sharing
