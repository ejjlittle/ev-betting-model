import { Stats } from "@/lib/models";
const API_URL = import.meta.env.VITE_BACKEND_API_URL;

//how data is stored in the json response
interface StatsByDate {
    [Date: string]: {
        Profit: string; //stored as string for precision
        AmountWagered: string; //stored as string for precision
        NumBets: number;
        NumWon: number;
        NumLost: number;
    };
}

export default async function fetchStats(): Promise<Stats[]> {
    const response = await fetch(`${API_URL}/api/stats`);

    if (!response.ok) {
        throw new Error("Failed to fetch stats");
    }

    const jsonResponse: StatsByDate = await response.json(); //convert response to StatsObjects json

    //map to array of DailyStats that include date as property (for easier data manipulation)
    const statsArray: Stats[] = Object.keys(jsonResponse).map(date => {
        const item = jsonResponse[date];
        return new Stats(date, item.Profit, item.AmountWagered, item.NumBets, item.NumWon, item.NumLost);
    });
    return statsArray;
}