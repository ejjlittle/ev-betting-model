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
        header: "Player",
        cell: ({ row }) => (
            <div className="font-bold">
                {row.getValue("player")}
            </div>
        )
    },
    {
        accessorKey: "bet",
        header: "Bet",
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
        header: "Game",
        cell: ({ getValue }) => {
            const game = getValue<string>().split("@");
            return (
              <span>
                {game[0]} <br /> <span className="font-light">@</span>{game[1]}
              </span>
            );
          }
    },
    {
        accessorKey: "book",
        header: "Book",
    },
    {
        accessorKey: "timePlaced",
        header: ({ column }) => {
            return (
              <Button
                variant="ghost"
                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
              >
                Time placed
                <ArrowUpDown className="ml-2 h-4 w-4" />
              </Button>
            )
          },
    },
    {
        accessorKey: "bookCount",
        header: ({ column }) => {
            return (
              <Button
                variant="ghost"
                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
              >
                Books compared
                <ArrowUpDown className="ml-2 h-4 w-4" />
              </Button>
            )
          },
    },
    {
        accessorKey: "wager",
        header: ({ column }) => {
            return (
              <Button
                variant="ghost"
                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
              >
                Wager
                <ArrowUpDown className="ml-2 h-4 w-4" />
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

            return <div>{formatted}</div>
        },
    },
    {
        accessorKey: "odds",
        header: ({ column }) => {
            return (
              <Button
                variant="ghost"
                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
              >
                Odds
                <ArrowUpDown className="ml-2 h-4 w-4" />
              </Button>
            )
          },
        cell: ({ row }) => {
            const odds = row.original.odds;
            return odds > 0 ? `+${odds}` : `${odds}`; //prepend + for positive odds
          },
    },
    {
        accessorKey: "fairOdds",
        header: ({ column }) => {
            return (
              <Button
                variant="ghost"
                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
              >
                Fair odds
                <ArrowUpDown className="ml-2 h-4 w-4" />
              </Button >
            )
          },
        cell: ({ row }) => {
            const fairOdds = row.original.fairOdds;
            return fairOdds > 0 ? `+${fairOdds}` : `${fairOdds}`; //prepend + for positive odds
          },
    },
    {
        accessorKey: "ev",
        header: ({ column }) => {
            return (
              <Button
                variant="ghost"
                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
              >
                EV%
                <ArrowUpDown className="ml-2 h-4 w-4" />
              </Button>
            )
          },
          //append '%'
          cell: ({ row }) => (
            <div className="font-bold">
                {row.original.ev}%
            </div>
        )
    },
    {
        accessorKey: "profit",
        header: ({ column }) => {
            return (
              <Button
                variant="ghost"
                onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
              >
                Profit
                <ArrowUpDown className="ml-2 h-4 w-4" />
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
                <div className={`font-bold ${
                    amount > 0 ? "text-positive" : amount < 0 ? "text-negative" : "text-primary"
                }`}>
                    {formatted}
                </div>
            );
        },
    }
]