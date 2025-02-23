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
                    I created this simple website as a personal project to display the results of my open-source
                    +EV betting model, which "places" and tracks the results of NBA player props. You can{" "}
                    <a className="text-positive font-bold hover:underline"
                        href="https://github.com/ejjlittle/ev-betting-model"
                        target="_blank"
                        rel="noopener noreferrer">
                        check out the code on GitHub
                    </a>.

                    <br /><br />

                    <span className="font-bold">
                        Please note that this model does not automatically place bets with actual money,
                    </span>{" "}
                    as that would violate the terms of service of most sportsbooks. This model is intended as a
                    proof of concept for a specific betting strategy that requires tracking a large number of bets—too
                    many for a human to place manually.{" "}
                    <span className="font-bold">
                        It is not intended as an exact guide for placing bets.
                    </span>{" "}
                </p>

                <p>
                    The model works by identifying outlier lines on sportsbooks based on calculated{" "}
                    <a className="text-positive font-bold hover:underline"
                        href="https://en.wikipedia.org/wiki/Expected_value"
                        target="_blank"
                        rel="noopener noreferrer">
                        expected value
                    </a>
                    {" "} (EV). However, sportsbooks are aware of strategies like this and often adjust their lines
                    within minutes. In other words, by the time the bets appear on this website, the lines may have
                    already been corrected.
                </p>

                <p>
                    Instead, this model can be replicated on a smaller scale using sites like{" "}
                    <a className="text-positive font-bold hover:underline"
                        href="https://crazyninjaodds.com/site/tools/positive-ev.aspx"
                        target="_blank"
                        rel="noopener noreferrer">
                        CrazyNinjaOdds
                    </a>,
                    which provides live positive expected value bets. The model scans for bets every 5 minutes
                    and "places" any that meet all of the following criteria:
                </p>

                <ul className="list-disc pt-3 pb-3 pl-10">
                    <li>Expected value is above 7%</li>
                    <li>Gametime is on the same day</li>
                    <li>The player has not already been bet on today</li>
                    <li>The bet is quantifiable with an "over" or "under"</li>
                    <li>More than five sportsbooks are compared</li>
                    <li>The sportsbook is FanDuel, DraftKings, or BetMGM</li>
                </ul>

                <p>
                    The model sizes wagers based on the{" "}
                    <a className="text-positive font-bold hover:underline"
                        href="https://en.wikipedia.org/wiki/Kelly_criterion"
                        target="_blank"
                        rel="noopener noreferrer">
                        quarter Kelly criterion
                    </a>,
                    using a $5,000 bankroll ($50 units).
                </p>

                <p>
                    This strategy can be applied to any bankroll size, as indicated by the number followed by "u"
                    near the top of the page. Additionally, this approach works for any sport— I chose the NBA
                    for this model because it has more games, meaning more lines for sportsbooks to manage,
                    which leads to more outliers.
                </p>
            </CardContent>
        </Card>
    )
}