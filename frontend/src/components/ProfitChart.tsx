import { useState, useEffect } from "react"
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
import fetchStats from "@/api/statsApi"

function getCumulativeStats(stats: Stats[], timeRange: string) {
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

    const referenceDate = new Date(); //today
    referenceDate.setHours(0, 0, 0, 0)

    const filteredData = stats.filter((item: Stats) => {
        const date = new Date(item.date);
        date.setHours(0, 0, 0, 0)

        let daysToSubtract = 7
        if (timeRange === "30d") {
            daysToSubtract = 30
        } else if (timeRange === "90d") {
            daysToSubtract = 90
        } else if (timeRange === "365d") {
            daysToSubtract = 365
        }
        const startDate = new Date(referenceDate)
        startDate.setDate(startDate.getDate() - daysToSubtract) //go back x + 1 days
        return date >= startDate && date < referenceDate //exclude today because no profit
    })

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
        color: "hsl(var(--positive))",
    },
} satisfies ChartConfig

export default function ProfitChart() {
    const [stats, setStats] = useState<any>(null); //stats data
    const [loading, setLoading] = useState<boolean>(true); //loading state
    const [error, setError] = useState<string | null>(null); //error state
    const [timeRange, setTimeRange] = useState("7d"); //filtering state

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

    const cumulativeStats = getCumulativeStats(stats, timeRange) as Stats[];


    return (
        <Card className="w-2/3">
            <CardHeader className="flex items-center gap-2 space-y-0 border-b border-border py-5 sm:flex-row">
                <div className="grid flex-1 gap-1 text-center sm:text-left">
                    <CardTitle>Cumulative Profit</CardTitle>
                    <CardDescription>
                        Displays cumulative profit over a period of time
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
            <CardContent className="px-2 pt-4 sm:px-6 sm:pt-6">
                <ChartContainer
                    config={chartConfig}
                    className="aspect-auto h-[190px] w-full">
                    {loading ? (
                        <p className="text-7xl font-bold text-muted">Loading...</p>
                    ) : error ? (
                        <p className="text-6xl font-bold text-muted">Error fetching data</p>
                    ) : (
                        <AreaChart data={cumulativeStats}>
                            <defs>
                                <linearGradient id="fillProfit" x1="0" y1="0" x2="0" y2="1">
                                    <stop
                                        offset="20%"
                                        stopColor="var(--color-profit)"
                                        stopOpacity={1}
                                    />
                                    <stop
                                        offset="100%"
                                        stopColor="var(--color-profit)"
                                        stopOpacity={0}
                                    />
                                </linearGradient>
                            </defs>
                            <CartesianGrid vertical={false} />
                            <XAxis
                                dataKey="date"
                                tickLine={false}
                                axisLine={false}
                                tickMargin={8}
                                minTickGap={32}
                                tickFormatter={(value) => {
                                    const date = new Date(value)
                                    return date.toLocaleDateString("en-US", {
                                        month: "short",
                                        day: "numeric",
                                    })
                                }}
                            />
                            <ChartTooltip
                                cursor={false}
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
                                type="natural"
                                fill="url(#fillProfit)"
                                stroke="var(--color-profit)"
                                stackId="a"
                            />
                        </AreaChart>
                    )}
                </ChartContainer>
            </CardContent>
        </Card>
    )
}