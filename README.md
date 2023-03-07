# Wordpress to Elementor post migration for Images
 This is a script that allows to selectively download all images in your current/dev site that reference the old/live website

# Installing the Required Packages

Before running the script, make sure that you have installed the necessary packages mentioned in the `requirements.txt` file. To do so, run the following command:

Use: 
`pip install -r requirements.txt`

This will install all the required packages with their specified versions.

## Running the Script

To run the script, open the command prompt or terminal and navigate to the directory where the script is saved. Then run the following command:

`python "Elementor Images Migrator.py"`

  
Note that you need to replace the values of `test_site` and `live_site` variables with your own URLs.

Also, the script requires an Excel file that contains a list of URLs to be crawled. You need to replace the value of  `excel_name`   with the name of your Excel file. The file should be placed in the same directory as the script.

Alternatively, you can modify the script to crawl URLs automatically instead of reading them from an Excel file.