Please save images that are larger than 1920 by 1080 here so we can down scale as appropriate.

To make bookmark highlights in GIMP:

Use the blank CK3 map and the province bitmap.
https://old.reddit.com/r/CrusaderKings/comments/ukp3pe/blank_ck3_map/

1). Select the applicable provinces in the province map
2). Paste into a new layer on the blank map
3). full the whole selection with the title color.

This gives us the initial outline to work with for each polity.

It may be useful to make the province map partly transparent and then overlay it on the blank map for
easier selection.

To complete a bookmark:

We want (as a result) 1920 by 1080 images, so it's best to zoom in on the region you want at a
higher resolution (like 2560 by 1440) then scale when complete.

Duplicate each layer as we're going to repeat this twice, but with different stroke colors for each.

1). Go to Layer with the polity highlight
2). Select by color
3). Convert selection to path
4). Stroke with solid black line of 5 px
5). Create Mask on the layer (white full opacity)
6). Create a Gradient fill, 100% opacity, Blend Color Space CIE lab, Shape Shaped (spherical or angular),
Euclidean Metric, no offset
7). Apply Mask to layer
8). Blur layer with default Gaussian blur.

Do this for each layer, swapping black for white on the second (and 70% opacity). This makes the polity
colorations for both the base map and the selection highlight. The black outline will be merged with the
base map, and the white outline is the polity highlight.

When all are done, export each separate layer as a dds with bc3/dxt5 compression, which matches the size of
Vanilla bookmarks.



This will make the colorations, then you can copy the layer and apply that layer to the map; the highlight
is similar, but is only the polity and uses white instead of black as the outline with
a Gaussian Blur at 50% opacity applied afterwards.

For Vassal Titles, I prefer to use 75% opacity instead of 50% opacity

For Tributaries, I apply striped fill to a mask (white full opacity), then redo the outline. The secondary
selection follows a similar as the original, but uses _very_ transparent overlay with around 90% opacity
and maybe spherical shaped.


