# Flask App for Importing CSV with Mapping Facility

## Use case
Many time we need to upload cab file in Saif format for further analysis. We need to put a _template_ in place and ask user to follow same set of template while uploading data. This May leads to some preprocessing at user's end. 
To avoid this, such utility will help upload any template with differ column name or with differ t sequence, will ask user to map them in environment, and no preprocessing is required. 
It can be an API service in future given to app developer under MIT license. 

_The app is working as is, with hard coded data, but easy to understand. _

## ToDo
- Customize the env file to store the key items, this can be base of main app. As of now I've kept this as place holder
- Based in env file automatically update the program to run number of columns and selection
- Check required data type vs what actually fed in. 
 
