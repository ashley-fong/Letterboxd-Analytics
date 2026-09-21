# Letterboxd Analytics: Exploring My Movie Data

### Summary 
In the summer of 2025, I set a goal for myself: watch 100 movies in 117 days. I thought this sounded easy - just watch 1 movie a day. But with full-time work, hanging out with friends, travelling home to see family, and enjoying the weather, it wasn't that simple. To my surpise, I ended up meeting my goal. 

I wanted to see what I could learn from the data behind this challenge. I was curious about how my ratings were distributed, which months I watched the most movies, how many movies I "liked," and what other patterns I could uncover. Luckily, I recorded it all on [Letterboxd](https://boxd.it/GNKdW), a website where people can log, rate, and review movies, create lists, and see what others are watching.

I decided to expand this idea and analyze all the movies I've reviewed and rated on my account. I compare viewing activity, ratings, and other metrics year over year to explore patterns in my movie watching habits, including whether I consistently watch more movies during certain months and whether my ratings have changed over time.

To take this one step further, I wanted to delve into my highest rated genres, actors, and directors as well as how my ratings compare to that of the general public. As Letterboxd exports do not provide this, I used the OMDb API to retrieve additional data for each movie logged on my account. I then joined this with my Letterboxd records, creating an enhanced dataset for further analysis and to uncover additional patterns.

### Questions I'm Exploring
- how have my ratings changed overtime?
    - is rating average increasing or decreasing? 
    - have I become a harsher critic? 
- do I consistently watch more movies in certain months? 
- do I watch more movies on a certain day of the week?
- how is my movie taste expanding overtime?   
    - in terms of: genre, decade, director, actors
- what receives the highest ratings / what are my favourites?
    - in terms of: genre, decade, director, actors
- how do my ratings compare with the general public?

### Methodology 

### Dashboard
This Power BI Dashboard cannot be shared to Microsoft Fabric / Report Server. You can access the downloadable version in **3_dashboard**. I am currently trying to learn Google Analytics and Looker Studio for a more accessible version for web and Tableau (again won't be available on Server or Cloud).

This dashboard utilizes dynamic slicers so the visualizations adjust to what has been selected. I split this up by year watched to compare year over year metrics like ratings, number of movies watched, and in theatre watches. 

There are / will be dedicated pages for Summer 2025 as this is where this idea started.

### Key Findings

