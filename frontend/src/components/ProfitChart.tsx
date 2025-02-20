import { useState } from "react"
import { Area, AreaChart, CartesianGrid, XAxis } from "recharts"
import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import {
    ChartConfig,
    ChartContainer,
    ChartTooltip,
    ChartTooltipContent,
} from "@/components/ui/chart"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import { Stats } from '@/lib/models';


function getCumulativeStats(stats: Stats[] | null, timeRange: string) {
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

    let daysToSubtract = 7
    if (timeRange === "30d") {
        daysToSubtract = 30
    } else if (timeRange === "90d") {
        daysToSubtract = 90
    } else if (timeRange === "365d") {
        daysToSubtract = 365
    }

    //note: stats already excludes the current date
    const filteredData = stats.slice(-daysToSubtract);

    //cumulative totals
    return filteredData.reduce<Stats[]>((acc, current, index) => {
        const previous = index > 0 ? acc[index - 1] : {
            date: current.date,
            profit: 0,
            amountWagered: 0,
            numBets: 0,
            numWon: 0,
            numLost: 0,
        };

        const cumulativeStat = new Stats(
            current.date,
            previous.profit + current.profit,
            previous.amountWagered + current.amountWagered,
            previous.numBets + current.numBets,
            previous.numWon + current.numWon,
            previous.numLost + current.numLost
        );

        return [...acc, cumulativeStat];
    }, []);
}


const chartConfig = {
    profit: {
        label: "Profit",
    },
} satisfies ChartConfig

interface ProfitChartProps {
    stats: Stats[] | null;
    loading: boolean;
    error: string | null;
}


export default function ProfitChart({ stats, loading, error }: ProfitChartProps) {
    const [timeRange, setTimeRange] = useState("7d"); //filtering state
    const cumulativeStats = getCumulativeStats(stats, timeRange) as Stats[];
    const lastStat = cumulativeStats[cumulativeStats.length - 1]
    const chartColor = lastStat && lastStat.profit >= 0
        ? "hsl(var(--positive))"
        : "hsl(var(--negative))";

    return (
        <Card className="w-full">
            <CardHeader className="flex items-center gap-2 space-y-0 border-b border-border py-5 flex-row">
                <div className="grid flex-1 gap-1 text-left">
                    <CardTitle>Cumulative Profit</CardTitle>
                    <CardDescription>
                        Displays cumulative profit over a period of time
                    </CardDescription>
                </div>
                <Select value={timeRange} onValueChange={setTimeRange}>
                    <SelectTrigger
                        className="w-[160px] rounded-xl ml-auto bg-background"
                        aria-label="Select a value"
                    >
                        <SelectValue placeholder="Last 7 days" />
                    </SelectTrigger>
                    <SelectContent className="rounded-xl border-border bg-background">
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
                    <p className="text-center text-base font-normal pt-4">Fetching graph data...</p>
                ) : error ? (
                    <p className="text-center text-base font-normal pt-4">Error fetching graph data</p>
                ) : (
                    <ChartContainer
                        config={chartConfig}
                        className="aspect-auto h-[190px] w-full pt-4">

                        <AreaChart data={cumulativeStats}>
                            <defs>
                                <linearGradient id="fillProfit" x1="0" y1="0" x2="0" y2="1">
                                    <stop
                                        offset="20%"
                                        stopColor={chartColor}
                                        stopOpacity={1}
                                    />
                                    <stop
                                        offset="100%"
                                        stopColor={chartColor}
                                        stopOpacity={0}
                                    />
                                </linearGradient>
                            </defs>
                            <CartesianGrid vertical={false} />
                            <XAxis
                                dataKey="date"
                                tickLine={false}
                                axisLine={true}
                                tickMargin={12}
                                minTickGap={24}
                                tickFormatter={(value) => {
                                    const date = new Date(value)
                                    return date.toLocaleDateString("en-US", {
                                        month: "short",
                                        day: "numeric",
                                    })
                                }}
                            />
                            <ChartTooltip
                                cursor={true}
                                content={
                                    <ChartTooltipContent
                                        labelFormatter={(value) => {
                                            return new Date(value).toLocaleDateString("en-US", {
                                                month: "short",
                                                day: "numeric",
                                            })
                                        }}
                                        indicator="line"
                                    />
                                }
                            />
                            <Area
                                dataKey="profit"
                                type="monotone"
                                fill="url(#fillProfit)"
                                stroke={chartColor}
                                stackId="a"
                            />
                        </AreaChart>

                    </ChartContainer>
                )}
            </CardContent>
        </Card>
    )
}