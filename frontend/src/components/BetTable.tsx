import DatePicker from "./DatePicker";
import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"

export default function BetTable(){
    return(
    <Card className="flex-1">
        <CardHeader className="flex items-center gap-2 space-y-0 border-b border-border py-5 sm:flex-row">
            <div className="grid flex-1 gap-1 text-center sm:text-left">
                <CardTitle>Bets Placed</CardTitle>
                <CardDescription>
                Displays the bets placed by the model on any given day
                </CardDescription>
            </div>
            <DatePicker/>
        </CardHeader>
        <CardContent>
        </CardContent>
    </Card>
    )
}
