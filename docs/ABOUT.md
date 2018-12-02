#About this file:
This code was developed by Tim Fitz

#Functionality:
A utility used to process an input list and retrieve a price from a web page.
Originally, developed for processing an xls with a list of Kindle books to determine their price.  Has been modified to scale for more generic use of the website price scanning.
Input / Output file is an xls with rows for each book to price scan.  Each row contains a book name, webURL, CSS Locator which is used to find the webpage and search it for the latest price.  The price is retrieved and updated on the xls.


#Coding Techniques:
- WebSites
    -[PriceScan.py] BeautifulSoup module - to parse text based on CSS Selector.  Creates a Search object, searches the html page for the a search string (CSS Selector which was on the input record)
- Work with Folders
    -[PriceScan.py] OS module
- YAML
    -[PriceScan.py] RUAMEL.YAML module for retrieving config data.  Imports Yaml file and retrieves section and elements with config data for processing.  Input Yaml only.  No updates.
- String processing
    -[PriceScan.py] RE module to build masks to search large strings.  Create search string for a price ex. (r'\$(\d)+.\d\d') and returns that string if found from the larger sting (ie. full webpage)
    -[PriceScan.py] Create multi-line strings with tabs and new lines.  Use string substitution and .format method to add formatting to percentage value 
- Logging
    -[PriceScan.py] LOGGING module to capture program events and messages.  Good example of loading the config parameters for job, any processing messages (at multiple Log Levels) and note job processing summary.
- Excel
    -[PriceScan.py] OPENPYXL module to open and work with xls.  Loop thru rows on a worksheet.  Retrieve and update cell values.
    -[PriceScan.py] OPENPYXL.STYLES
