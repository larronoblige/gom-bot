import gspread
gc = gspread.service_account('credentials.json')

# id only, if no sheet is specified it defaults to Sheet1
def getSheet(sheet, worksheet="Sheet1"):
    if sheet in nicknames:
        sheet = getNickname(sheet)
    sh = gc.open_by_key(sheet)
    ws = sh.worksheet(worksheet)
    return ws

# returns a list that contains dictionaries for each claimer
# keys are the headers of every column
def getRecords(ws):
    records = ws.get_all_records()
    return records

# anything (e.g., sheets) you want to alias
# good for giving to your claimers for the !paid command
nicknames = {
    "": "",
}
# accessor
def getNickname(nickname):
    sheet = nicknames[nickname]
    return sheet