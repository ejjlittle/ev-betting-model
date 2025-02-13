import { useState, useEffect } from 'react';
import { calcROI, calcUnits } from '@/lib/utils';
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import fetchStats from "@/api/statsApi"
import { DailyStats } from '@/lib/models';

export default function ProfitCard() {
    const [stats, setStats] = useState<any>(null); //stats data
    const [loading, setLoading] = useState<boolean>(true); //loading state
    const [error, setError] = useState<string | null>(null); //error state
    const [timeRange, setTimeRange] = useState("1d"); //filtering state

    useEffect(() => {
        const getStats = async () => {
            try {
                setLoading(true);
                const statsData = await fetchStats();
                setStats(statsData);
            } catch (err) {
                setError('Failed to fetch stats');
            } finally {
                setLoading(false);
            }
        };

        getStats(); //call fetch on mount
    }, []); //only once when the component mounts

    if (loading) {
        return <p className="text-7xl font-bold text-muted">Loading...</p>;
    }

    if (error) {
        return <p className="text-6xl font-bold text-muted">Error {error}</p>;
    }

    // If stats is null or empty, return nothing or a message
    if (!stats || stats.length === 0) {
        return <p className="text-6xl font-bold text-muted">No data available</p>;
    }

    console.log(stats)

    //filter data for only selected days
    const referenceDate = new Date() //today
    referenceDate.setHours(0, 0, 0, 0); //normalize to midnight

    const filteredData = stats.filter((item: DailyStats) => {
        const date = new Date(item.date) //already normalize (only stored as day)

        let daysToSubtract = 1
        if (timeRange === "7d") {
            daysToSubtract = 7
        } else if (timeRange === "30d") {
            daysToSubtract = 30
        } else if (timeRange === "90d") {
            daysToSubtract = 90
        } else if (timeRange === "365d") {
            daysToSubtract = 365
        }
        const startDate = new Date(referenceDate) //start from yesterday
        startDate.setDate(startDate.getDate() - daysToSubtract - 1) //go back x days
        return (date >= startDate) && (date != referenceDate) //exclude today because no profit
    })

    const profit = filteredData.reduce((accumulator: number, currentItem: DailyStats) => {
        return Math.round((accumulator + currentItem.profit) * 100) / 100;
    }, 0);

    return (
        <Card className="w-1/3">
            <CardHeader className="flex items-center gap-2 space-y-0 border-b border-border py-5 sm:flex-row">
                <div className="grid flex-1 gap-1 text-center sm:text-left">
                    <CardTitle>Profit</CardTitle>
                    <CardDescription>
                        Displays the profit over a period of time
                    </CardDescription>
                </div>
                <Select value={timeRange} onValueChange={setTimeRange}>
                    <SelectTrigger
                        className="w-[160px] rounded-xl sm:ml-auto bg-background"
                        aria-label="Select a value"
                    >
                        <SelectValue placeholder="yesterday" />
                    </SelectTrigger>
                    <SelectContent className="rounded-xl border-border bg-background">
                        <SelectItem value="1d" className="rounded-xl">
                            Yesterday
                        </SelectItem>
                        <SelectItem value="7d" className="rounded-xl">
                            Last 7 days
                        </SelectItem>
                        <SelectItem value="30d" className="rounded-xl">
                            Last 30 days
                        </SelectItem>
                        <SelectItem value="90d" className="rounded-xl">
                            Last 3 months
                        </SelectItem>
                        <SelectItem value="365d" className="rounded-xl">
                            Last 12 months
                        </SelectItem>
                    </SelectContent>
                </Select>
            </CardHeader>
            <CardContent>
                <div className="flex flex-row w-full justify-between pt-10">
                    <div className="flex flex-col justify-end">
                        {loading && <p className="text-7xl font-bold text-muted">Loading...</p>}
                        {error && <p className="text-6xl font-bold text-muted">Error fetching data</p>}
                        <p className={`text-7xl font-bold ${profit >= 0 ? 'text-positive' : 'text-negative'}`}>
                            {profit >= 0 ? `+$${profit}` : `-$${profit}`}
                        </p>
                    </div>
                    <div className="flex flex-col justify-end">
                        <p className="text-xl font-bold text-positive">+2.06u</p>
                        <p className="text-xl font-bold text-positive">+23.2% ROI</p>
                    </div>
                </div>
            </CardContent>
            <CardFooter>
                <div className="flex flex-row justify-end w-full">
                    <p className="text-right font-light text-lg text-muted-foreground">(14-10-2) across 26 bets</p>
                </div>
            </CardFooter>
        </Card>
    )
}
