#! python 3


# TODO: do From xxx Import yyy to shrink the import size
import requests
import os
import bs4
import re
import logging
import openpyxl
from openpyxl.styles import PatternFill

##  INPUT
#webPageURL = 'https://www.amazon.com/Tribe-Homecoming-Belonging-Sebastian-Junger-ebook/dp/B01BCJDSNI/ref=sr_1_1?ie=UTF8&qid=1541727214&sr=8-1&keywords=junger'
CSS_Selector = 'td.a-color-price'
downLoadFile = 'KindlePage1'

cacheDir = 'K:\\@Tech\\Programming\\Python\\StringProcessing'
logging.basicConfig(filename='myLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)  # when you want to Turn off low level logging
logging.info('+ + + + + Program Started - Initialization Routine + + + + +')

# TODO:  Figure out how to determine where the downloaded web pages will get stored.  Make a subdir for this run.  Dir name s/b YYMMDD ...
os.chdir(cacheDir)

# ## FLOW ##
#   Initialization - establish global variables / values ...
#  STEP 1. Main Loop.  Open the File / DB with the list of items to price check and loop thru each entry
#  STEP 2. Save the WebPage to a local file
#  STEP 3. Extract the webpage section based on the CSS Selector Path
#  STEP 4. Download the WebPage (if needed)
#  STEP 5. Parse the "retrieved webpage section" to get the data
#  STEP 6. 


# ####
# #######  STEP 2.  - Download WebPage  #######
# #######  STEP 3.  - Extract the webpage section based on the CSS Selector Path  #######
# #######  STEP 4.  - Save WebPage Locally  #######
def getWebPage(webPageURL, CSS_Sel1, CSS_Sel2, bookname):
  # Use the Requests module method to retrieve a web page into memory.
  elems = []
  myResponse = requests.get(webPageURL)

  try:
    myResponse.raise_for_status()
    blFoundPage = True
  except Exception as exc:
    logging.error('WebPage %s had this error: %s' %(webPageURL, exc))
    blFoundPage = False

  if myResponse.status_code == 200:
    logging.info('FOUND website %s' %webPageURL)

  if blFoundPage:
    myParse = bs4.BeautifulSoup(myResponse.text, 'html.parser')   # Use the BeautifulSoup module to create first create the Search object, then to search it with the search string
    elems = myParse.select(CSS_Sel1)

    if elems != []:
      logging.info(len(elems) + ' Strings found on page.')
    else:
      logging.warning('There were no strings found when searching for %s in %s' %(CSS_Sel1, bookname))
      if (CSS_Sel1 != CSS_Sel2) and (not CSS_Sel2.isspace()):
        elems = myParse.select(CSS_Sel2)
        if elems != []:
          logging.warning('There were no strings found when searching for %s in %s' %(CSS_Sel2, bookname))

          # You failed to find 2 different CSS Selectors.  If config file specifies, here is where you save the downloaded file for debugging
          # TODO:  Figure out how you'll name the page and add config item for the Chunk size
          # savedFile = open(downLoadFile,'wb')
          # for myChunk in myResponse.iter_content(100000):
          #   savedFile.write(myChunk)
          # savedFile.close()


  # TODO: Pass back success / fail status on each CSS_Selector string
  return(elems)

# ####
# #######  STEP 5.  - Parse the "retrieved webpage section" to get the data  #######
def parseOutPrice(argLstUnformatLines):
  myRegObj = re.compile(r'\$(\d)+.\d\d')
  myMatch = myRegObj.search(argLstUnformatLines[0].text)
  myPrices = myMatch.group()
  return (myPrices)



# TODO:  Figure out what your input file will be.  CSV, XLS, TXT, DB ... .   Fix the For / While loop too
strBookList = 'BookList.xlsx'
# inputFile = open(filename = strBookList)
# lstBookItems = inputFile.readlines()

#try:
wb = openpyxl.load_workbook('BookList.xlsx')
sheet = wb['full']
logging.info('Input xls file opened.  There were ' + str(sheet.max_column) + ' columns and ' + str(sheet.max_row) + ' rows.')

x = 2
while x < sheet.max_row + 1:
  parmWebPageURL = sheet.cell(row = x, column = 7).value   #  get from input file
  parmCSS_Sel1 = sheet.cell(row = x, column = 8).value     #  get from input file.  Use default from config if null.
  if not parmCSS_Sel1:                                     #  see if parm value is null / empty
    parmCSS_Sel1 = CSS_Selector
  parmCSS_Sel2 = sheet.cell(row = x, column = 9).value     #  get from input file.
  wrkBookName = sheet.cell(row = x, column = 2).value     #  get book name from file or increment a counter.
  if len(wrkBookName) == 20:
    parmBookName = wrkBookName
  elif len(wrkBookName) > 20:
    parmBookName = wrkBookName[0:19]
  else:
    parmBookName = wrkBookName.ljust(20, '*')

  lstUnformattedPriceLines = getWebPage(parmWebPageURL, parmCSS_Sel1, parmCSS_Sel2, parmBookName)   # Pass web page and CSS search strings and get a list of the unformatted strings from webpage
  if lstUnformattedPriceLines != []:
    logging.info(str(len(lstUnformattedPriceLines)) + ' Strings found on page.')
    strBookPrice = parseOutPrice(lstUnformattedPriceLines)
    logging.info('*****  Price for %s is: %s' %(parmBookName, strBookPrice))

    # TODO: compare the parsed price to previous price on input file and do something ...
    # Here's some code to change the Fill color on excel cells
    # if True:
    #   fill = PatternFill(bgColor='92D050', fill_type = 'solid')   # Green
    # else:
    #   fill = PatternFill(bgColor='FF0000', fill_type = 'solid')   # Red
    # sheet['B2'].fill = fill


  # else:               # There were no results returned from getWebPage().  Could be web page not forund or Found page but scans found nothing
  x = x + 1
     
# except:
#   logging.error('Program failed.  Unable to open input file: ' + strBookList)

logging.info('+ + + + + Program Ended + + + + +')
