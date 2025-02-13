export class Stats {
    date: string;
    profit: number;
    amountWagered: number;
    numBets: number;
    numWon: number;
    numLost: number;

    constructor(date: string, profit: number | string, amountWagered: number | string, numBets: number, numWon: number, numLost: number) {
        this.date = date
        this.numBets = numBets;
        this.numWon = numWon;
        this.numLost = numLost;
        this.profit = this.parseNumber(profit);
        this.amountWagered = this.parseNumber(amountWagered);
    }

    private parseNumber(value: number | string){
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