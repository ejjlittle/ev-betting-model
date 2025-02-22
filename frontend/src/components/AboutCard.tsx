import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"

export default function AboutCard() {
    return (
        <Card className="flex-1">
            <CardHeader className="flex items-center gap-2 space-y-0 border-b border-border py-5 flex-row">
                <div className="grid flex-1 gap-1 text-left">
                    <CardTitle>About</CardTitle>
                    <CardDescription>
                        A destription of the betting model
                    </CardDescription>
                </div>
            </CardHeader>
            <CardContent>
                <p className="p-3">
                    As a Computer Science and Applied Mathematics major at the University of Notre Dame,
                    I made this simple website as a personal project to display the results of my open source
                    +ev betting model, which “places” and tracks the results of NBA player props. You can {" "}
                    <a className="text-positive font-bold hover:underline" href="https://github.com/ejjlittle/ev-betting-model" target="_blank" rel="noopener noreferrer">
                        check out the code on GitHub
                    </a>.<br />
                    
                    <br />
                    <span className="font-bold">Please note that this model does not automatically place bets with actual money </span> 
                    as that is against most sportsbooks terms of service. The model is meant to be a proof of concept of a
                    certain betting strategy across a number of bets too large for a human to place by hand.{" "}
                    <span className="font-bold">The model is not meant to be used as an exact guide of bets to place. </span>
                    This is because the model works by finding outlier lines on sportsbooks based on calculated{" "}
                    <a className="text-positive font-bold hover:underline" href="https://en.wikipedia.org/wiki/Expected_value" target="_blank" rel="noopener noreferrer">
                        expected value
                    </a> 
                    {" "}(EV). 
                    The books, aware that betting strategies like this exist, fix these lines in mere minutes. In other words, there
                    is a good chance that the lines have already been adjusted by the time the bets appear on this website.<br />
                    <br />
                    Instead this model can be replicated on a smaller scale using sites like{" "}
                    <a className="text-positive font-bold hover:underline" href="https://crazyninjaodds.com/site/tools/positive-ev.aspx" target="_blank" rel="noopener noreferrer">
                        CrazyNinjaOdds
                    </a>,
                    which pulls live positive expected value bets. The model pulls these bets every 5 minutes,
                    “placing” any that fit all of the following criteria:
                    <ul className="list-disc pt-3 pb-3 pl-10">
                        <li>Above 7% expected value</li>
                        <li>Gametime is on the same day</li>
                        <li>Player has not already been bet on today</li>
                        <li>The bet is quantifiable with an “over” or “under"</li>
                        <li>There are more than 5 books compared</li>
                        <li>The book is FanDuel, DraftKings, or BetMGM</li>
                    </ul>
                    The model sizes the wagers based on the{" "}
                    <a className="text-positive font-bold hover:underline" href="https://en.wikipedia.org/wiki/Kelly_criterion" target="_blank" rel="noopener noreferrer">
                        quarter Kelly criterion
                    </a>, 
                    using a $5,000 bankroll ($50 units).
                    This strategy will still work with any unit amount or bankroll size, as indicated by the number
                    followed by the ‘u’ near the top of the page. Also note this this strategy will work with any sport.
                    I just chose NBA for the model because there are more games, and thus, more lines the books have
                    to maintain, leading to more outliers.
                </p>
            </CardContent>
        </Card>
    )
}