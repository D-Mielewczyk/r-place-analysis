# r-place-analysis

Initially, I started this project to hone my *matplotlib* and *pandas* knowledge. The data turned out to be too large for *pandas* so I  converted all of the code to *dask*. Data is still too large for *dask* to handle.

In the future, I plan to convert the project to *Vaex* or a different big data solution, but I wanted to provide a sneak-peak of how the finished project will look like.

All that said please understand that some plots won't make as much sense as they should, because I only used 6.3% of the data.

Full resolution plots can be found in the **plots** folder or generated using **main.ipynb** notebook.

## Pixels per color

The first plot didn't suffer much from the lack of data. It showcases how much each color was used compared to the others.
![color_counts](plots\color_counts-1.png)

## Max pixels placed per user based on color

Similar to the plot above but this time we are looking at **maximum** number of **pixels** placed by **one user** based on **color**.
![color_user_counts](plots\color_user_counts-1.png)

## Top 10 users with maximum pixels placed

![top10_tiles_per_user](plots\top10_tiles_per_user-1.png)

## Heatmap of pixels

In this heatmap, we can see the traffic of each area on the canvas.
![pixels_heatmap](plots\pixels_heatmap-1.png)

## Activity based on time of the day

How many **pixels** were **placed** based on **hour** of the day [UTC]
![hourly_activity](plots\hourly_activity-1.png)

## Activity based on the day

How many **pixels** were **placed** based on the **day**.
![daily_activity](plots\daily_activity-1.png)

There will be more plots in the finished project.
