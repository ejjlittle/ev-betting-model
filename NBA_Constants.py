#--NBA STATS REQUEST CONSTANTS--#
URL = "https://stats.nba.com/stats/leaguegamelog"
HEADERS = {
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
COOKIES = {
    "ak_bmsc": "21C8041BB838B730ED2E84B4B5513B8D~000000000000000000000000000000~YAAQT6TAFzaGl4yUAQAAn8PSoBoibCVVCKwtV7IWYFAwc2scEiKACm8oOSFklv25m8Un5aBROxVbuyHQK7o1ulKiGsR5xA4B3FHVOP9WFSLWCSZW+bZixdqNGv/f9ZZf1o1/TeGuVduVVUuZiht6r9ctTONYOjh3H+KSsQd0XG3xb5YZrW0/2sX4Q02ViwhHUIgjwdKZBdwOd1Xa9lBvLvsNIg7xmIqqjN1cN9A+DafvQA10CfZqmXUFEfunSv/7PhdfUnW3Kd/Wi1u56rOonM16/K6b3CUDV0z2lN4/V//YftCYaZuTV7Mm2u6LYIl4ejlTlsr3y3XGkCPnh1JdUnMcwyyk05KwkASZN52lhi9iHQxuH4eg0AZ7wqF2rw=="
}
PARAMS = {
    "Counter": "1000",
    "DateFrom": "01/25/2025",
    "DateTo": "01/25/2025",
    "Direction": "DESC",
    "ISTRound": "",
    "LeagueID": "00",
    "PlayerOrTeam": "P",
    "Season": "2024-25",
    "SeasonType": "Regular Season",
    "Sorter": "DATE"
}