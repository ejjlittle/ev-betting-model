const API_URL = process.env.BACKEND_API_URL;

export default async function fetchBets(date: Date) {
    const today = new Date();

    //convert to YYYY-MM-DD 
    //Note: do not need to worry about timezones because ISO is standardized to UTC
    //and dates are stored in DB as Date objects, which are also standardized to UTC  
    const formattedDate = date.toISOString().split("T")[0];
    const formattedToday = today.toISOString().split("T")[0];

    let response: Response;
    //different API endpoints are used for efficient caching of data
    if (formattedDate === formattedToday){ 
        response = await fetch(`${API_URL}/api/bets/today/${date}`); //getting live from same day
    } else if (date < today){
        response = await fetch(`${API_URL}/api/bets/historical/${date}`); //getting constant historical data
    } else {
        response = new Response(); //no bets for future days
    }

    if (!response.ok) {
        throw new Error("Failed to fetch stats");
    }

    return response.json();
}