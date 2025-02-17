import { useEffect, useState } from "react";
import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { columns } from "./bets/columns"
import { DataTable } from "./bets/data-table"
import fetchBets from "@/api/betsApi";
import DatePicker from "./DatePicker";


export default function BetTable() {
    const [data, setData] = useState<any>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    const [selectedDate, setSelectedDate] = useState<Date>(new Date()); //default date is today

    useEffect(() => {
        const getBets = async () => {
            try {
                setLoading(true);
                const betData = await fetchBets(selectedDate);
                setData(betData);
            } catch (err) {
                setError('Failed to fetch stats');
            } finally {
                setLoading(false);
            }
        };

        getBets();
    }, [selectedDate]); //fetch bets when date changes

    return (
        <Card className="flex-1">
            <CardHeader className="flex items-center gap-2 space-y-0 border-b border-border py-5 sm:flex-row">
                <div className="grid flex-1 gap-1 text-center sm:text-left">
                    <CardTitle>Bets Placed</CardTitle>
                    <CardDescription>
                        Displays the bets placed by the model on any given day <br />
                        Hover over each header for more info
                    </CardDescription>
                </div>
                <DatePicker date={selectedDate} setDate={setSelectedDate} />
            </CardHeader>
            <CardContent>
                {loading ? (
                    <p className="text-center pt-4 text-base">Fetching bets...</p>
                ) : error ? (
                    <p className="text-center pt-4 text-base">Error fetching bets</p>
                ) : (
                    <DataTable columns={columns} data={data} />
                )}
            </CardContent>
        </Card>
    );
}