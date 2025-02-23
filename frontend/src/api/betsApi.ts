import { Bet } from "@/lib/models";
import { convertToEST } from "@/lib/utils"
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

function getEstDateString(date: Date): string {
    const estFormatter = new Intl.DateTimeFormat('en-US', {
        timeZone: 'America/New_York',
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
    });

    const parts = estFormatter.formatToParts(date);
    const year = parts.find(part => part.type === 'year')?.value || '';
    const month = parts.find(part => part.type === 'month')?.value || '';
    const day = parts.find(part => part.type === 'day')?.value || '';

    return `${year}-${month}-${day}`;
}

export default async function fetchBets(date: Date) {
    const today = convertToEST(new Date());

    //convert to YYYY-MM-DD  
    const formattedDate = getEstDateString(date)
    const formattedToday = getEstDateString(today)


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