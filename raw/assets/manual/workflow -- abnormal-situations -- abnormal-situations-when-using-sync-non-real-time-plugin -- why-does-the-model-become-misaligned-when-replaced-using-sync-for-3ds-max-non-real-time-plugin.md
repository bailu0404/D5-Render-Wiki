# Why does the model become misaligned when replaced using Sync for 3ds Max (non-real-time plugin)?

****Background:**** No “sync coordinates” and “sync pivot” have been used, and changing the plugin's coordinate switch method does not resolve the issue.

****Temporary solution:****

1. Open the D5 old archive

2. Manually record the current model's XYZ axis coordinates

3. Link and replace (at this point, the model position should be misaligned)

4. Manually change the XYZ coordinates in the linked D5 file to the previously recorded coordinates, and the position will display correctly.