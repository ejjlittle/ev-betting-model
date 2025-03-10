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
CNO_COOKIES = {
    "ASP.NET_SessionId": "z5i0xh2dx4x3b4dkkvksqsyz",
    "BetaFilters": "DevigMethod=0&ProfitStrategy=1&SortBy=1&IsMain2=0&MinimumEVPercentage=0&MinimumOddsProviderCount=3&MinimumSubMarketSideCount=2&MaximumSubMarketSideCount=&RequireACompleteSportsbook=True",
    "BetaKelly": "KellyBankroll=1000&KellyMultiplier=0.25",
    "BetaSettings": "ExcludedSportsbooks=47gNHjPb3xG+WDnT72armcIZfs0moxsX6K5EStzHrQZYsDfT2dnKyRluTvtg+FwwQjqXyqqJp0E9rUra2tb2Zh/f/n6rqEk3QNefZH+zOiHsz5tmDrK4HHSSKxTexfBFrgJoCzpmDIdZ/m3/nOXObw==&ExcludedAffiliateLinks=XCFYicDA1el1bE352vBHM8dxp6/maxsRc6Xk7cYfJphLx7Moiq8CA5e+KDkMNTmcpq8O5j+DCCHSzG+ZtwzAnA==",
    "BetaState": "State=none",
    "BetaWarningLimits": "Read=1",
    "General": "KellyMultiplier=.25&KellyBankRoll=1000&DevigMethodIndex=4&WorstCaseDevigMethod_Multiplicative=True&WorstCaseDevigMethod_Additive=True&WorstCaseDevigMethod_Power=True&WorstCaseDevigMethod_Shin=True&MultiplicativeWeight=0&AdditiveWeight=0&PowerWeight=0&ShinWeight=0&ShowEVColorIndicator=False&ShowDetailedDevigInfo=False&CopyToClipboard_Reddit=False&CopyToClipboard_DevigURL=True&CopyToClipboard_Reddit_IncludeDevigURL=True&CopyToClipboard_Reddit_Mini=False&ShowHedgeDevigMethod=False&UseMultilineTextbox=False&StartWithEmptyFields=False"
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
    "__VIEWSTATE": "I/SAs/fnQJJjKtod8rT2bTq6MhQnavvr9SasmzeoBmgzNJCfuC2DVJ1tRuuuXmveUXT2BM4YOagCYCyUlyvW84f7OUyWLXQJYE81EChSZBxQxbzM0PmqU9u0lRzlaikklb7a+r2YqRlqMAjEZOD206sdZLK8+ERtVhJaD/QdQVjcQ/Jxyk1ABJgTgk8xvYHCDuRrjeDjuoXVdC5LP4HfIAFH7DWCQJED222Tan5cohLD93FE5A8Jb4u9xhhGxvbT4OCAL1E0JP4lMklFtLx/1JwiSi0Vqbbdg6llUsE63YpKMUOrPI6gPWtxdoOs7J2D4nAyzyPHPC1wSnPECKUu+RhPh2qJbFgq3Dljo1Ifb7zasc6tP9jRTAt0aOWeKXVv5PTTcR7oE1YnRGpd8gHgKWAtZXh8UPUe7jowa4LDY4rAeAIi9zYprBX0+B1Oi9fwYhQ8RojPKCbVR99ghnbzG7RbQBjnTQpUSNQpmyPV+dctJYzPTYJ0NfmwvcAuxJ1Sk/DC3/A/G4DjeLz7KRBe/Udfbw8s4vzAvTxkYpUweEZ/56/dm0VwbEBCX0Dyx2UiU967EUyobG4xe1c3uNCg4zRwJMkrutexXwUZy/m5DDdZdH5HOMJgkiYfseY+GyhAwuUeL9qRkxAWUgRO4SzgRVUKLG7w2zdWaj8/VQdUWJKvh9Aw713V2HsRVnRjqdgDUGm6vKOcucjtkHdoU8Ylvyp2+1nuxpUaVCBO759vXlUhi8UQulmBwsXvt8xtnRDIhha6Hq1JrdkJU/dSkhKafwjdYyCzZ5ew5uX5X7KU/+bonGtheAiCaU04xsGwwMKwBeUDppsAHoWWB1OoQnVfVGheouY+PLzmUtzUHWhkD8yka7iZO7G37wh8xOaGzsXs/Ha3sYTJk7z12PhYNuadZw5feqbOcSOvGlKh5Q5KS5PSmbSPSXbWLEIR7pYuuGcBd20Z7JlUzuOXt4CeEiC0tKtGYG5JrIINvjBzNSePcC/rqY7wwKsfK3kjECODxLXdogujPJxSSmk4YwOGsw6tbse8o8EuAnoNPQjCPUryoPI8OnXFpoirMRO+MaoJEVcULh/7O+iOZNUoV9Ftol0chheEogcjDlICRXPExgY7jsR4COuEL1XM8xTZaBiBySRw5nx4pYmk/tvST5rJtiEwUr482R2Swd3FHsq60c8dtUhtQKRrcRPr3hdSlXwzCPgSRMTUTzsgH6i98P1HKDz4IwoJrRTQH5ODioUoHvzKrp+F3ApAwlHx1KBtgqu3DPGdp/rh1ueqF+wQfdLF9Vor4EGNUtkfylrFozkh3IG6zpHtgQ+5V5+caQZAdRNvXrberzghkCIfTEPgdoh/YTeIhZ9LpRUMfF46Z1dfpwsVBZ/XmzC2sx4q+UOsb9fUKqFfhR5yVSLibOTn53yrcc21BxTTsFPwlNqCL0QfOs91FDUniEJCfQKR7FlBXLDEW3tosnQNGdr+4v5NgX7QKDEcQTaVv+EZwnbG66R/C0T6rT/M4fGEo8+E6cXO4oUj6AdDDxRKan+Pnbf2hnxvo9NFoMBDo5tPIstFIef7d8U/u0gOkB2Rcuq9970KPugA3/La3A5K3Fl8uqmGJbQQCbAs2ApwhBGRS3iiYbU0AIu1j4DO8Oq+/d+VWrcRxyT8Gamx",
    "__VIEWSTATEGENERATOR": "B6071BA7",
    "__EVENTVALIDATION": "HATcZCkw5iEINbR7wpoKsD7O4DEknsl1xSb+al7uR5dNUl8siaW9wbAh4qTZMNULlu8l7yjoislmSS3KuVE9YBe23q/mR+AOxjRqezGj7CWTKopXnoWBcnPrFRwcrlGOLb5aS7xafXHSZ1dhZTlds+1DUJq6QkLi6+P8TvGn8xiT/Njsr0QNOFkK4Sl7PRUxdRtBoqjRwG93h/Wrp3t1HeDqOR5NgXtCg5BrA1eMrjAfmM3JgRfDasXZ2I2gQJVWyXkasWEHH7ZvTToAkvoQleFOx+DRWzqmrprx3BFovXWg09bmL8n1tsU7EeV2hWuuKNIeEj1Fc30+klQk57YW9M0+k5IWLZHQ8+cwOlZ9pUbl8RisdJ++dL1bqW0iz0iNhgPwCUQeG+BG564/G+lr9uBQgkGRnrR802Uy9ewnx+h7gSBZ+LVhYnfeA/yljZJDRttB98ciCFMA9qjz96+XRVHepMMcT/QqYmn1kDhTmeNdbwA0nsEpCiFqSsY/BG6EX+nPxeBUNjJKEYBNSXNMOy89PC/XEqxpvo+dEP75c5K2gHq/zl9mqCIfnMviEg4QMmOx4gQjXOnfYURZd3G3zcSmy3X9PJRldYka5X42+8aNEmDj3m7PgZi/tJ27vfttqzEzUr91SK8vwvrJLnvE9uGTBIZhV7C+ditlESWxwwyB+ScCxf03kXRJyIqygaBSiXBF4eiSO1FFkQm+mkraR7JC0/B7aIbOqYFNkyDtHFA1OP/2wyTZeV2iUAkAVu8WWLu6G6iFNh3N0bKVtzcDtjB25j4I+PStLTt+MIp20/6wgdhr89Msg9XaND8Zf3TYr6Rj5OuNdOsx1WnsBXbDzMTCsP/Slx4vEppRI3cclZNt2Zu13ve2dTsx+FHS45cUYsSDQfQERHDb4j211g1nGVzfW9Mv9QKiHWbEr2Zk5qFYxM8ReIFIxiyiVtXKKvzRXvfG8G0qxAdxmLmIiNoy17caHp0IJERueOJrs/bGjAK1kaqbQiupueOjBRNrOT/n8T6cVi2N/HMvGjES3GJ1Uw==",
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