import { ColumnDef } from "@tanstack/react-table"
import { ArrowUp, ArrowDown, ArrowUpDown } from "lucide-react"
import { Button } from "@/components/ui/button"
import {
    HoverCard,
    HoverCardContent,
    HoverCardTrigger,
} from "@/components/ui/hover-card"
import { calcUnits } from "@/lib/utils"
import { Bet } from "@/lib/models"

export const columns: ColumnDef<Bet>[] = [
    {
        accessorKey: "player",
        header: () => (
            <div className="text-center">
                <HoverCard>
                    <HoverCardTrigger>Player</HoverCardTrigger>
                    <HoverCardContent>
                        Name of player
                    </HoverCardContent>
                </HoverCard>
            </div>
        ),
        cell: ({ row }) => (
            <div className="font-bold text-center">
                {row.getValue("player")}
            </div>
        )
    },
    {
        accessorKey: "bet",
        header: () => (
            <div className="text-center">
                <HoverCard>
                    <HoverCardTrigger>Bet</HoverCardTrigger>
                    <HoverCardContent>
                        The model currently supports <br />
                        quantitative player props only
                    </HoverCardContent>
                </HoverCard>
            </div>
        ),
        cell: ({ row }) => {
            const betText: string = row.original.bet;

            //extract over/under, amount, "player", and market name
            const match = betText.match(/(Over|Under) (\d+\.?\d*) ([^"]+) (.+)/);
            if (!match) return betText; //return unmodified if format not matched
            const [, overUnder, number, , market] = match;
            const ArrowIcon = overUnder === "Over" ? ArrowUp : ArrowDown;

            //add up or down arrow for over/under
            return (
                <div className="flex items-center space-x-1">
                    <ArrowIcon className="w-4 h-4 text-primary" />
                    <span>{number} {market}</span>
                </div>
            );
        },
    },
    {
        accessorKey: "game",
        header: () => (
            <div className="text-center">
                <HoverCard>
                    <HoverCardTrigger>Game</HoverCardTrigger>
                    <HoverCardContent>
                        Teams playing
                    </HoverCardContent>
                </HoverCard>
            </div>
        ),
        cell: ({ getValue }) => {
            const game = getValue<string>().split("@");
            return (
                <div className="text-center">
                    {game[0]}
                    <span className="text-muted-foreground">@</span> <br />
                    {game[1]}
                </div>
            );
        }
    },
    {
        accessorKey: "book",
        header: () => (
            <div className="text-center">
                <HoverCard>
                    <HoverCardTrigger>Sportsbook</HoverCardTrigger>
                    <HoverCardContent>
                        The model currently supports<br />
                        DraftKings, FanDuel, and BetMGM
                    </HoverCardContent>
                </HoverCard>
            </div>
        ),
        cell: ({ row }) => (
            <div className="text-center">{row.getValue("book")}</div>
        ),
    },
    {
        accessorKey: "timePlaced",
        header: ({ column }) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    className="flex items-center justify-center w-full rounded-xl"
                >
                    <HoverCard>
                        <HoverCardTrigger>Time placed</HoverCardTrigger>
                        <HoverCardContent>
                            All times are displayed <br />
                            in Eastern Standard Time
                        </HoverCardContent>
                    </HoverCard>
                    <ArrowUpDown className="h-4 w-4" />
                </Button>
            )
        },
        cell: ({ row }) => (
            <div className="text-center">{row.getValue("timePlaced")}</div>
        ),
    },
    {
        accessorKey: "bookCount",
        header: ({ column }) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    className="flex items-center justify-center w-full rounded-xl"
                >
                    <HoverCard>
                        <HoverCardTrigger>Books</HoverCardTrigger>
                        <HoverCardContent>
                            The number of sportsbooks<br />
                            averaged - more books means<br />
                            less variance in fair odds<br />
                        </HoverCardContent>
                    </HoverCard>
                    <ArrowUpDown className="h-4 w-4" />
                </Button>
            )
        },
        cell: ({ row }) => (
            <div className="text-center">{row.getValue("bookCount")}</div>
        ),
    },
    {
        accessorKey: "wager",
        header: ({ column }) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    className="flex items-center justify-center w-full rounded-xl"
                >
                    <HoverCard>
                        <HoverCardTrigger>Wager</HoverCardTrigger>
                        <HoverCardContent>
                            Wager sizes are calculated using<br />
                            the{" "}
                            <a className="text-primary font-bold hover:underline" href="https://en.wikipedia.org/wiki/Kelly_criterion" target="_blank" rel="noopener noreferrer">
                                quarter Kelly criterion
                            </a>
                        </HoverCardContent>
                    </HoverCard>
                    <ArrowUpDown className="h-4 w-4" />
                </Button>
            )
        },
        //format as currency
        cell: ({ row }) => {
            const amount = parseFloat(row.getValue("wager"))
            const formatted = new Intl.NumberFormat("en-US", {
                style: "currency",
                currency: "USD",
            }).format(amount)
            const units = calcUnits(amount)

            return <div className="text-center">{formatted} ({units}u)</div>
        },
    },
    {
        accessorKey: "odds",
        header: ({ column }) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    className="flex items-center justify-center w-full rounded-xl"
                >
                    <HoverCard>
                        <HoverCardTrigger>Odds</HoverCardTrigger>
                        <HoverCardContent>
                            American odds on the listed book<br />
                            at the time the model took the bet
                        </HoverCardContent>
                    </HoverCard>
                    <ArrowUpDown className="h-4 w-4" />
                </Button>
            )
        },
        cell: ({ row }) => {
            const odds = row.original.odds;
            return <div className="text-center">{odds > 0 ? `${odds}` : `${odds}`}</div>;
        },
    },
    {
        accessorKey: "fairOdds",
        header: ({ column }) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    className="flex items-center justify-center w-full rounded-xl"
                >
                    <HoverCard>
                        <HoverCardTrigger>Fair odds</HoverCardTrigger>
                        <HoverCardContent>
                            Calculated by averaging together<br />
                            the{" "}
                            <a className="text-primary font-bold hover:underline" href="https://en.wikipedia.org/wiki/Vigorish" target="_blank" rel="noopener noreferrer">
                                devigged
                            </a>
                            {" "}odds across<br />
                            multiple sportsbooks<br />
                        </HoverCardContent>
                    </HoverCard>
                    <ArrowUpDown className="h-4 w-4" />
                </Button >
            )
        },
        cell: ({ row }) => {
            const fairOdds = row.original.fairOdds;
            return <div className="text-center">{fairOdds > 0 ? `${fairOdds}` : `${fairOdds}`}</div>; //prepend + for positive odds
        },
    },
    {
        accessorKey: "ev",
        header: ({ column }) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    className="flex items-center justify-center w-full rounded-xl"
                >
                    <HoverCard>
                        <HoverCardTrigger>EV%</HoverCardTrigger>
                        <HoverCardContent>
                            Expected value percentage <br/>
                            calculated using the implied win<br />
                            probability of the fair odds
                        </HoverCardContent>
                    </HoverCard>
                    <ArrowUpDown className="h-4 w-4" />
                </Button>
            )
        },
        //append '%'
        cell: ({ row }) => (
            <div className="font-bold text-center">{row.original.ev}%</div>
        )
    },
    {
        accessorKey: "profit",
        header: ({ column }) => {
            return (
                <Button
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    className="flex items-center justify-center w-full rounded-xl"
                >
                    <HoverCard>
                        <HoverCardTrigger>Profit</HoverCardTrigger>
                        <HoverCardContent>
                            This model bets based on a $5,000  <br/>
                            fixed bankroll, or $50 units
                        </HoverCardContent>
                    </HoverCard>
                    <ArrowUpDown className="h-4 w-4" />
                </Button>
            )
        },
        cell: ({ row }) => {
            //format for currency
            const amount = parseFloat(row.getValue("profit"))
            const formatted = new Intl.NumberFormat("en-US", {
                style: "currency",
                currency: "USD",
            }).format(amount)
            const units = calcUnits(amount)

            //add color for positive or negative
            return (
                <div className={`text-center font-bold ${amount > 0 ? "text-positive" : amount < 0 ? "text-negative" : "text-primary"
                    }`}>
                    {formatted} <span className="font-normal">({units}u)</span>
                </div>
            );
        },
    }
]