import { ColumnDef } from "@tanstack/react-table"
import { ArrowUp, ArrowDown, ArrowUpDown } from "lucide-react"
import { Button } from "@/components/ui/button"

export type Bet = {
    id: string
    player: string
    bet: string
    game: string
    timePlaced: string
    book: string
    bookCount: number
    wager: number
    odds: number
    fairOdds: number
    ev: number
    profit: number
}

export const columns: ColumnDef<Bet>[] = [
    {
        accessorKey: "player",
        header: () => (
            <div className="text-center">Player</div>
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
            <div className="text-center">Bet</div>
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
            <div className="text-center">Game</div>
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
            <div className="text-center">Book</div>
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
                Time placed
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
                Books
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
                Wager
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

            return <div className="text-center">{formatted}</div>
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
                Odds
                <ArrowUpDown className="h-4 w-4" />
              </Button>
            )
          },
        cell: ({ row }) => {
            const odds = row.original.odds;
            return <div className="text-center">{odds > 0 ? `+${odds}` : `${odds}`}</div>; //prepend + for positive odds
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
                Fair odds
                <ArrowUpDown className="h-4 w-4" />
              </Button >
            )
          },
        cell: ({ row }) => {
            const fairOdds = row.original.fairOdds;
            return <div className="text-center">{fairOdds > 0 ? `+${fairOdds}` : `${fairOdds}`}</div>; //prepend + for positive odds
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
                EV%
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
                Profit
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

            //add color for positive or negative
            return (
                <div className={`text-center font-extrabold ${
                    amount > 0 ? "text-positive" : amount < 0 ? "text-negative" : "text-primary"
                }`}>
                    {formatted}
                </div>
            );
        },
    }
]