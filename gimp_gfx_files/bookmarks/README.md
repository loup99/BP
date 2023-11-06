Please save images that are larger than 1920 by 1080 here so we can down scale as appropriate.

To make bookmark highlights in GIMP:

Use the blank CK3 map and the province bitmap.
https://old.reddit.com/r/CrusaderKings/comments/ukp3pe/blank_ck3_map/

1). Select the applicable provinces in the province map
2). Paste into a new layer on the blank map
3). full the whole selection with the title color.

This gives us the initial outline to work with for each polity.

To complete a bookmark:

We want (as a result) 1920 by 1080 imagse, so it's best to zoom in on the region you want at a higher resolution (like 2560 by 1440) then scale when complete

1). Go to Layer with the polity highlight
2). Select by color
3). Convert selection to path
4). Stroke with solid black line of 5 px
5). Create Mask on the layer (white full opacity)
6). Create a Gradient fill, 50% opacity, Blend Color Space CIE lab, Shape Shaped (angular), Euclidean Metric, no offset

This will make the colorations, then you can copy the layer and apply that layer to the map (the highlight is similar, but is only the polity and uses white instead of black as the outline with a Gaussian Blur at 50% opacity applied afterwards.

When all are done, export each separate layer as a dds with bc3/dxt5 compression.