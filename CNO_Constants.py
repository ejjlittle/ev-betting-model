#--CNO POST REQUEST CONSTANTS--#
URL = "https://crazyninjaodds.com/site/tools/positive-ev.aspx"
HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://crazyninjaodds.com",
    "priority": "u=1, i",
    "referer": "https://crazyninjaodds.com/site/tools/positive-ev.aspx",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "x-microsoftajax": "Delta=true",
    "x-requested-with": "XMLHttpRequest"
}
COOKIES = {
    "ASP.NET_SessionId": "c4pdhsx03f2nhc3fe3wd3cqc",
    "BetaKelly": "KellyBankroll=1000&KellyMultiplier=0.25",
    "BetaSettings": "ExcludedSportsbooks=47gNHjPb3xG+WDnT72armcIZfs0moxsX6K5EStzHrQZYsDfT2dnKyRluTvtg+FwwQjqXyqqJp0E9rUra2tb2Zh/f/n6rqEk3QNefZH+zOiHsz5tmDrK4HHSSKxTexfBFrgJoCzpmDIdZ/m3/nOXObw==&ExcludedAffiliateLinks=XCFYicDA1el1bE352vBHM8dxp6/maxsRc6Xk7cYfJphLx7Moiq8CA5e+KDkMNTmcpq8O5j+DCCHSzG+ZtwzAnA==",
    "BetaState": "State=none",
    "BetaWarningLimits": "Read=1",
    "General": "KellyMultiplier=.25&KellyBankRoll=1000&DevigMethodIndex=4&WorstCaseDevigMethod_Multiplicative=True&WorstCaseDevigMethod_Additive=True&WorstCaseDevigMethod_Power=True&WorstCaseDevigMethod_Shin=True&MultiplicativeWeight=0&AdditiveWeight=0&PowerWeight=0&ShinWeight=0&ShowEVColorIndicator=False&ShowDetailedDevigInfo=False&CopyToClipboard_Reddit=False&CopyToClipboard_DevigURL=True&CopyToClipboard_Reddit_IncludeDevigURL=True&CopyToClipboard_Reddit_Mini=False&ShowHedgeDevigMethod=False&UseMultilineTextbox=False&StartWithEmptyFields=False"
    }
DATA = {
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
    "__VIEWSTATE": "euhoQn0Y6t7Bz2Pul5xVPab4nfwAfL5lDysPF3nkZl0vPUgEDqG4O5212zGsZOVlz0FyX0afkM8SzFg7tTyJv1CUsiC5NSciWXqQADX5qa8mqdjYzRLy7gd7TRgjx2JhUrWuZFMK8t/sNEJRu7lE4uQ6NAzNCSZQXFrkCOhlrbi+vYUS8bzee0UzPy1j90130fYBnQNsK2q8bIENmojTRj/uu5LesMkNQNfmOU9Y+hjmUCz6ZEmJgC1w/HyZpxZM+PMRvXPtjYpvntNu7QFdcJi0BLVJbHVgcl7GJDFk5MjhdDdjjbpOndlgCGymvaYhuiOceoqII5F3Bua4To2Bmmw35JZX9uShdKhtgufPjyVevPFAVPFOo25f7v8PTH6+35IpPoO8MPZxtVjQAsX/eJYLA96soeMTNnMolsIFSSIPOaxLeKYejzmtPNRZ4J5xUmz1OGC1VVpUehJNxgt+wTzYthklqAAPhHkmISpdHHG/nlNLPgoyBtiuBF19QOiSHD87sMaDjmv6dIBM3NOmsanmk06H/KYnlMAM0BHHVE5ffAfS4BWXXrD5m+YUSVCTejYH0DwPRrFu2kUXyUbPnkcAR9BFFFbjkUEmtpStqYCu8WdvclVaixhimBYKPA5no2EzkbIXZnm17XPS+/fkUvb8J1bIxFRAnoK+WD0jUdkLZS9kLp3bXXMkpXDT2knkYmdeREEBdiF5E5sYjfkAr8yoIR2jG8zoi4jFD19uxKeSZyncbfpqVR8c3LvAE4rVAVAvKdbo7AJU19DUGAnci4jpYwSZs8Ovp0HidUAr5u5gxYUqg6sXi4/dI4BP+bGA/EVWyDw+Gv546MLJ75abzxnbVwTKMH5XfdEcVYzaAMBP983uElJJs6RS80mpSaCxbfZMZAHKTlPcQkt2Elm8FkkoHBefa7nkPiUzybm1fPelFx7L/JNUYMZXV7ZdtBVhHjGgr1LTSEf2pBPdIgnQ5LgMWxW09SdqkbVpQd0kBtzC68d24Rb0/tQXhpRoXtb5n4gr/YTslqFSrSzanvT04pT+xXLCLIv5cp+v6ninWy5zKlimZ3g17vJm65czzrcRxdmn5doNfkpGTdiATLaQPRzdh7VM1Wi9ef0FH3dy1S4rv/UpQ3OSRWiuLtWjnnlngP3fXGhgPM8bi4DPtXfbQaNKJNJw8a9wHBRGdHZNt/AjoMk+9lqbIcHKzOylOXC/aGuapl5PdDuCCCPeK4V/Llpzwp7QH9bZ7nMFLn8iPNx2OYGrLCOxroXK8EdfHibrJnU69YOC+zwVoNxqIxKU4N9bCvW4KNb7MPPRvgUGyH+SXfi052zv+mno1G8FM7NB45AzXwgYN+CJWNYlXocQzBnq15AldfNTGwVKMnoeahCGOLVYqgkSo4SN+U8TpeW3Xm6iJRGzUgjMBwCwgO7NUGn4Rs3wpeEhTRIW1G0UqEApeQ3Lzqk86wJun6tsI/AvM+twvUpT0Hukfv2HQpvATUmQh97bTCvo9QoHnNfNAOEIG6BQqRTffTCbVkMxCUCeqSIOn82v2JX2a7EoVTOhPWbxNZj+GNPTww1ytinKz4F+P3+KjNaSXnoQ8bKgupHZUPoC5hxUZSVp6DYO33+p44hWTfODoaQuvdQPIiwPZ8ND3hE+yXyX6gzRkDUj5YrRihlzz90I5WJJKCkWoflBSw==",
    "__VIEWSTATEGENERATOR": "B6071BA7",
    "__EVENTVALIDATION": "YCHYdd0VAfCWoHcR6Lf02lxKEtPxhWiHuOvX/GVRwviN6CuHbWq2oi2V2+CYieP8iHOvi7N4q/GE0SoYcLZjwlIHYLugPO4XuBiF86dOK4O7DqbZL7geDKO5aze9E+I/VjI04X1fLBbQyGeMSQ1+oF442m8FWUIK8Qq+BnCojkoP1m9uVGmdOPkREszc8V0Dfymc5eNCZ/wV2uA6Cj+fMlB94jNL3gOrlHy3mpdnLufniqZCHkM9VdY8Y5qkpOJSDCbWefhUUkRNYRq0FmnEatlz8We0yk1dnO6tnTMDJSdljZ8/U6yQdpSiDk9vevS4S1Akp9+jAO3n1XGmfTVleFaXiUCK3e4crsbeaX5M8xgNngF8oZIUQ4YYMxodyqujHnWnipskW4qO4vTRBmg4CsCXcswnoIEXVHqqSLRdcUcp+pAYTV48n4yWaTYT84BHobz6JbHs2x1lioWzitVoM77q4nSW8wpyZZqU++1rPBAWzEBlzrd6ELHUu6ViBHQDcJAy/8GQwgqi/DBuCeADmBBRbh0APF7T/bV99bewg/wvPulPn5+0eACwIkcCQFgy2CA4ubF6pA2Zp/4XIKKOo0Zscfvn5nrXXY47uapHnJCnZUHcReyJzMO4dGOnHW9+9VRaO2BO0fEZGISOsd191yYBQpDz3mBQxNJqoqeVne9n41KVOIVl+iev4gweHjp+ZielBkb9srT4AkjLCtThWSBs7BfMfyojGAk1wngas4nTHoW8C8Txwbho/ROiw8KF5/O01Y5P6lHaQ/gPbwfpxyBKrZPKKmr9UswuzFDTK67jt4IVHqkEtxOCom7l5LW9pN4GcT1EM9suKkoOB0GuL/1gCHmZqv4HIz1xsPe55rgRCdbC50hxbW7917G5x5sI6RZ5as0ZNZWG23rLSG+h7eLqY9RM4BwNIiP8fwNpzvOoyaoHD2AVPIWratX48wuOwnKiD63aeYCTpCgySPpHwA==",
    "__ASYNCPOST": "true",
    "ctl00$ctl00$ContentPlaceHolderMain$ContentPlaceHolderRight$ButtonUpdate": "Update"
}