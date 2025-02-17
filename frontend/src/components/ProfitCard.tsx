import { useState } from 'react';
import { calcROI, calcUnits } from '@/lib/utils';
import {
    Card,
    CardContent,
    CardDescription,
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
import { Stats } from '@/lib/models';
import Counter from './Counter';

function getFilteredStats(stats: Stats[] | null, timeRange: string) {
    //check for no stats
    if (!stats || stats.length === 0) {
        return {
            date: "Total",
            profit: 0,
            amountWagered: 0,
            numBets: 0,
            numWon: 0,
            numLost: 0
        };
    }

    const referenceDate = new Date() //today
    referenceDate.setHours(0, 0, 0, 0)

    const filteredData = stats.filter((item: Stats) => {
        const date = new Date(item.date)
        date.setHours(0, 0, 0, 0)

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
        const startDate = new Date(referenceDate)
        startDate.setDate(startDate.getDate() - daysToSubtract) //go back x + 1 days
        return date >= startDate && date < referenceDate; //exclude today because no profit
    })

    //aggregate totals
    return filteredData.reduce(
        (totals, item) =>
            new Stats(
                "Total",
                Math.round((totals.profit + item.profit) * 100) / 100,
                Math.round((totals.amountWagered + item.amountWagered) * 100) / 100,
                totals.numBets + item.numBets,
                totals.numWon + item.numWon,
                totals.numLost + item.numLost
            ),
        new Stats("Total", 0, 0, 0, 0, 0)
    );
}

interface ProfitCardProps {
    stats: Stats[] | null;
    loading: boolean;
    error: string | null;
  }

export default function ProfitCard({ stats, loading, error }: ProfitCardProps) {
    const [timeRange, setTimeRange] = useState("7d"); //filtering state (default last 7)
    const totalStats = getFilteredStats(stats, timeRange) as Stats;
    
    return (
        <Card>
            <CardHeader className="flex items-center gap-2 space-y-0 border-b border-border py-5 flex-row">
                <div className="grid flex-1 gap-1 text-left">
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
                        <SelectValue placeholder="Last 7 days" />
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
                {loading ? (
                    <p className="text-center pt-4 text-base font-normal">Fetching stats...</p>
                ) : error ? (
                    <p className="text-center pt-4 text-base font-normal">Error fetching stats</p>
                ) : (
                    <div>
                        <div className={`flex flex-row w-full gap-x-1 pt-10 sm:gap-x-5 ${totalStats.profit >= 0 ? 'text-positive' : 'text-negative'}`}>
                            <span className="flex items-center font-bold text-5xl sm:text-6xl md:text-7xl">
                                {totalStats.profit >= 0 ? "+$" : "-$"}
                                <Counter value={Math.abs(totalStats.profit)} />
                            </span>
                            <div className="flex flex-col justify-end font-bold whitespace-nowrap text-lg sm:text-xl">
                                <span className="flex flex-row">
                                    {totalStats.profit >= 0 ? "+" : "-"}
                                    <Counter value={calcUnits(Math.abs(totalStats.profit))} />u
                                </span>
                                <span className="flex flex-row">
                                    {totalStats.profit >= 0 ? "+" : "-"}
                                    <Counter value={calcROI(totalStats.amountWagered, Math.abs(totalStats.profit))} />% ROI
                                </span>
                            </div>
                        </div>
                        <div className="flex-row justify-end w-full pt-4">
                            <p className="text-right font-light text-lg text-muted-foreground">
                                ({totalStats.numWon}-{totalStats.numLost}-{totalStats.getTies()}) across {totalStats.numBets} bets placed                      </p>
                        </div>
                    </div>
                )}
            </CardContent>
        </Card>
    )
}
