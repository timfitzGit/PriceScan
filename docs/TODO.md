To insert a date:  Press Ctrl + ','   then press 'd'

### Basic cleanup
- [] create package structure.   
    - [x] Folder structure 
    - [] Key files: __init__, setup, ...
- [] upgrade documentation
    - [] Update README.MD documentation file.
    - [] Update TODO.MD documentation file.
    - [] Update ABOUT.MD documentation file.
- [] Standardize initRoutine processing
    - [] develop Failure logic if config file found but critical elements missing or null
    - [x] process config file and return list with log messages / level along with Pass / Fail flag


### Improve the code and add functionality
- [] add relative file paths when working with directories or files.  \Data folder should have input and output
    - [] determine the relative path of this module and use this to set the cacheDir variable
    - [x] move input file BookList.xls to another folder and adjust code
    - [] move output file mylog.txt to \Data\Output folder and adjust code
- [] Improve Output Processing
    - [] add config.yaml control and logic to output results to Text file.
    - [x] add config.yaml control and logic to output results to Excel Input file.
    - [] add config.yaml control and logic to output results to a database used as Input file.
    - [] add logic to determine if price changed
    - [] add logic to send email with txt or excel file
- [] Improve Logging and Debug logic
    - [] change log msg on CSS Selector search.  INFO if not found on parm from input.  WARNING if not found on input AND defaault
    - [] add config setting and logic to save the web page locally if web page found but CSS_Selector search failed
- [] Modularize the getWebPage()
    - [] split the web page retrieval and CSS_Selector search into separate functions
    - [] capture failure to find webpage, pass result back to main routine and update input file
    - [] capture failure to find CSS_Selector search, pass result back to main routine and update input file
- [] check price parsed from web page against value from input file and process events:
    - [] append to a "Price Update" email
    - [] highligh cell on xls input file
    - [] write console message
- [] improve validation and error message processing
    - [] create functions that validate each edit and RETURN error message
    - [] call validation functions and add error messages to a list
    - [] process all edits (functions) and log all error messages captured in list


### Make this a Utility to use in more scenarios
- [] Build BAT file scheduled job to run regularly
- [] Add configurable functionality
    - [] Add differnt data sources (xls, txt, console) to be input data source
    - [] Add setting for Level to disable logging


