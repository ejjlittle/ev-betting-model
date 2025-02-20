import { Bet } from "@/lib/models";
const API_URL = import.meta.env.VITE_BACKEND_API_URL;

//how data is stored in the json response
interface BetDetails {
    [player: string]: {
        Wager: string; //stored as string for precision
        Profit: string; //stored as string for precision
        EV: number;
        Date: string;
        GameTime: string;
        TimePlaced: string;
        Sport: string;
        League: string;
        Game: string;
        Market: string;
        BetName: string;
        Odds: string;
        Book: string;
        FairOdds: string;
        BookCount: number;
    }
}

export default async function fetchBets(date: Date) {
    const today = new Date();

    //convert to YYYY-MM-DD 
    //Note: do not need to worry about timezones because ISO is standardized to UTC
    //and dates are stored in DB as Date objects, which are also standardized to UTC  
    const formattedDate = date.toISOString().split("T")[0];
    const formattedToday = today.toISOString().split("T")[0];

    let response: Response;
    //different API endpoints are used for efficient caching of data
    if (formattedDate === formattedToday) {
        response = await fetch(`${API_URL}/api/bets/today?date=${formattedToday}`); //getting live from same day
    } else if (date < today) {
        response = await fetch(`${API_URL}/api/bets/historical?date=${formattedDate}`); //getting constant historical data
    } else {
        response = new Response(); //no bets for future days
    }

    if (!response.ok) {
        throw new Error("Failed to fetch stats");
    }

    const jsonResponse: BetDetails = await response.json(); //convert response to StatsObjects json

    //map to array of DailyStats that include date as property (for easier data manipulation)
    const betsArray: Bet[] = Object.keys(jsonResponse).map(player => {
        const item = jsonResponse[player];
        return new Bet(player, 
            `${item.BetName} ${item.Market}`, 
            item.Game, 
            new Date(`2025-01-01 ${item.TimePlaced} EST`), //nomralize to 2025-1-1
            item.Book,
            item.BookCount,
            item.Wager,
            item.Odds,
            item.FairOdds,
            item.EV,
            item.Profit
        );
    });

    return betsArray;
}