export class Stats {
    date: string;
    profit: number;
    amountWagered: number;
    numBets: number;
    numWon: number;
    numLost: number;

    constructor(date: string, 
        profit: number | string, 
        amountWagered: number | string, 
        numBets: number, 
        numWon: number, 
        numLost: number
    ) {
        this.date = date
        this.numBets = numBets;
        this.numWon = numWon;
        this.numLost = numLost;
        this.profit = this.parseDollar(profit);
        this.amountWagered = this.parseDollar(amountWagered);
    }

    private parseDollar(value: number | string){
        if (typeof value === "string") {
            const parsed = parseFloat(value);
            return isNaN(parsed) ? 0 : Math.round(parsed * 100) / 100;
        }
        return value;
    }

    getTies() {
        return this.numBets - this.numLost - this.numWon
    }
}

export class Bet {
    player: string;
    bet: string;
    game: string;
    timePlaced: Date;
    book: string;
    bookCount: number;
    wager: number;
    odds: number;
    fairOdds: number;
    ev: number;
    profit: number;

    constructor(
        player: string,
        bet: string,
        game: string,
        timePlaced: Date,
        book: string,
        bookCount: number,
        wager: number | string,
        odds: number | string,
        fairOdds: number | string,
        ev: number,
        profit: number | string
    ) {
        this.player = player;
        this.bet = bet;
        this.game = game;
        this.timePlaced = timePlaced; //normalize all times to 2025-01-01
        this.book = book;
        this.bookCount = bookCount;
        this.wager = this.parseDollar(wager);
        this.odds = this.parseOdds(odds);
        this.fairOdds = this.parseOdds(fairOdds);
        this.ev = ev;
        this.profit = this.parseDollar(profit);
    }

    private parseDollar(value: number | string){
        if (typeof value === "string") {
            const parsed = parseFloat(value);
            return isNaN(parsed) ? 0 : Math.round(parsed * 100) / 100;
        }
        return value;
    }

    private parseOdds(value: number | string){
        if (typeof value === "string") {
            const parsed = parseInt(value);
            if (isNaN(parsed)) {
                return 0;
            }
        }
        return value as number;
    }
}