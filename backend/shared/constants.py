#--BETTING MODEL CONSTANTS--#
MINIMUM_EV_PERCENTAGE = 7
MAXIMUM_EV_PERCENTAGE = 40
LEAGUES = ["NBA"]
BOOKS = ["FanDuel", "DraftKings", "BetMGM"]
MINIMUM_BOOK_COUNT = 5
UNIT_SIZE = 50
PLAYER_NAMES = {
    "Carlton Carrington": "Bub Carrington"
}

#--CNO POST REQUEST CONSTANTS--#
CNO_URL = "https://crazyninjaodds.com/site/tools/positive-ev.aspx"
CNO_HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://crazyninjaodds.com",
    "priority": "u=1, i",
    "referer": "https://crazyninjaodds.com/site/tools/positive-ev.aspx",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "x-microsoftajax": "Delta=true",
    "x-requested-with": "XMLHttpRequest"
}
CNO_DATA = {
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$ScriptManager1": "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$UpdatePanelGridView|ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$ButtonUpdate",
    "ContentPlaceHolderMain_ContentPlaceHolderRight_TabContainerPopupCalc_ClientState": '{"ActiveTabIndex":0,"TabEnabledState":[true,true],"TabWasLoadedOnceState":[true,false]}',
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterPositiveEVSportsbookSite$DropDownListSportsbookSite_All": "0",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterSport$DropDownListSport": "0",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterLeague$DropDownListLeague": "0",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterMinimumOdds$TextBoxMinimumOdds": "",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterMaximumOdds$TextBoxMaximumOdds": "",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterMaximumDateHours$TextBoxMaximumDateHours": "",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$TextBoxMinimumEVPercentage": "0%",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterEventNameContains$TextBoxEventNameContains": "",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterMarketNameContains$TextBoxMarketNameContains": "",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterMaximumResultCount$TextBoxMaximumResultCount": "",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterDevigMethod$DropDownListDevigMethod": "0",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterSubMarketSideCount$TextBoxMinimumSubMarketSideCount": "2",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterSubMarketSideCount$TextBoxMaximumSubMarketSideCount": "",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterSubMarketSideCount$CheckBoxRequireACompleteSportsbook": "on",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$WebUserControl_FilterOddsProviderCount$TextBoxMinimumOddsProviderCount": "3",
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__VIEWSTATE": "", #updated dynamically
    "__VIEWSTATEGENERATOR": "B6071BA7",
    "__EVENTVALIDATION": "", #updated dynamically
    "__ASYNCPOST": "true",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$ButtonUpdate": "Update"
}

#--NBA STATS REQUEST CONSTANTS--#
NBA_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "stats.nba.com",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
    "Sec-CH-UA": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}