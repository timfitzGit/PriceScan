To insert a date:  Press Ctrl + ','   then press 'd'

### Basic cleanup
- [] create package structure.   
    - [x] Folder structure 
    - [] Key files: __init__, setup, ...
- [] upgrade documentation
    - [] Update README.MD documentation file.
    - [] Update TODO.MD documentation file.
- [] Create config file (YAML or JSON) for settings
- [] Create a repository on GitHub


### Improve the code and add functionality
- [] change imports to from xxx import yyy to streamline
- [] add relative file paths when working with directories or files.  \Data folder should have input and output
    - [] move input file BookList.xls to \Data\Input folder and adjust code
    - [] move output file mylog.txt to \Data\Output folder and adjust code
- [] Improve Logging and Debug logic
    - [] adjust Log Level settings to limit DEBUG / INFO messages
    - [] change log msg on CSS Selector search.  INFO if not found on parm from input.  WARNING if not found on input AND defaault
    - [] add config setting and logic to save the web page locally if web page found but CSS_Selector search failed
- [] Modularize the getWebPage()
    - [] split the web page retrieval and CSS_Selector search into separate functions
    - [] capture failure to find webpage, pass result back to main routine and update input file
    - [] capture failure to find CSS_Selector search, pass result back to main routine and update input file
- [] check price parsed from web page against value from input file and process events:
    - [] append to a "Price Update" email
    - [] update xls input file
    - [] write console message


### Make this a Utility to use in more scenarios
- [] Update (YAML or JSON) config file to facilitate broader usage beyond Kindle 
- [] Build BAT file scheduled job to run regularly
- [] Add configurable functionality
    - [] Add differnt data sources (xls, txt, console) to be input data source
    - [] Add setting for Level to disable logging


