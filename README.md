# df-capstone

# Overview

- This project aims to load in the dataset of every player in MLB history and allow the end user to select which Hall-of-Famer they want to view the details for
- The dataset was sourced from Sean Lahman's research [^1]
- I aimed to analyse the teams that the players played on, as well as voting trends over time for them
- I found that players who reached the HoF and had long careers usually spent most of their time on one team
- I also found that there were in general two types of voting pattern, either getting in right at the start of eligibility or just getting in after years of heartache

# Setup & Running

## 1
- Create a virtual python environment
## 2
- Run the following command:
```python
pip install -r requirements.txt
```
## 3
- In your bash terminal, run the following:
```bash
streamlit run src/stapp.py
```
## If a new update to the database is here
## 1 
- Download the new files to `data/raw`
## 2
- Open `main.py` in your ide
## 3
- Run `main.py` as a python file

# User Stories

## 1
- As a user, I want to select a player that has been considered for the HoF and see their biographical information.
- [x] Create Selection Box
- [x] Be able to select player
- [x] Do it by name
- [x] See bio info
## 2
- As a user, I want to see the teams that a HoF player has played for.
- [x] See all the teams
- [x] See the years that they were on the teams
## 3
- As a user, I want to see the voting progression for each player.
- [x] See the number of votes the person got each year
- [x] See that number compared to the amount needed
- [x] See the vote share for the player
- [ ] See the information for non-traditionally voted players
# Stages

1.  Copied the initial-project setup from etl-project-demo [^2]
2. Imported raw data from the internet [^1]
3. Set up `main.py` with streamlit
4. Set up extraction
5. Started initial transformation
6. Wrote the column manager
7. Found that appearances was needed
8. Added appearances
9. Set up transform to merge everything
10. Called the transformation in main
11. Found that since Baseball-Reference does not store their pictures in a nice format, bbrefID was not needed, so dropped it
12. Wrote a row manager to cull extraneous records
13. Wrote the loader
14. Set up `stapp.py` to actually run streamlit and removed it from main
15. Ran the etl-process successfully for the first time
16. Implemented basic person selection
17. Made a function to write the birth and death days of the person selected
18. Wrote a function to write metrics to the app
19. Found that having everything in one csv caused far too much duplication
20. Therefore unmerged the dataframes
21. Made it so that you can choose the names rather than the playerID
22. Found that the teams csv was necessary to get the names of the teams for better functionality down-the-line
23. Extracted it and added it throughout the etl process
24. Output new transformed CSVs
25. Found that it needed to be merged with apps in the transformation stage
26. Implemented that
27. Another new CSV
28. Wrote the first HoF tracker, showing the amount of votes v the amount needed
29. Decided to include the vote share
30. Wrote a function to add it as a calculated column in HoF
31. Updated and ran the etl process to include it
32. Created a second chart next to the first one showing the fluctuation in vote share over time
33. Created the team chart, showing the teams a player was on each year
34. Finished documenting the code

# Other features not-yet developed

- Ideally, the team chart would show the continuous time on a team as a single block
- I would like to have been able to better handle those who did not play or have traditional votes to get in
- Would like to be able to get the etl process to run automatically on update or even from console
- Pictures, generally
- Specifically, of the player, their HoF plaque and the team logos
- There's more metrics that could be shown, such as birthplace
- The big undertaking, definitely outside the scope of a 2-week project would be to include the players stats
- In those stats, the ultimate goal would be to create the rough stats of an average HoFer depending on era

# Future Issues

- If the dataset grew much larger, I would properly utilise indexing
- I have used try:except as my error handling. If I had more time I would further implement logging. As it is, there is pseudo-logging with the exceptions telling you what function is causing the error, and in the case of particularly tricky functions, where in that function it's breaking
- I do not believe there to be any security or privacy issues
- This could be converted to the cloud using S3 to store the data. The dataset updates yearly, so no streaming is necessary. AWS Glue jobs could be used to do the ETL process. AWS App Runner would be the obvious choice to make this run on a large-scale

[^1]: Sean Lahman et al, http://www.seanlahman.com/ 

[^2]: Ed Wright, https://github.com/de-2502-a/etl-project-demo
