import ProfitChart from "@/components/ProfitChart"
import ProfitCard from "./components/ProfitCard"
import BetTable from "./components/BetTable"
import AboutCard from "./components/AboutCard"
import { ArrowRight } from 'lucide-react';

function App() {

  return (
    <div>
      <div className="bg-card pt-10 pl-5 pb-10 border-b border-border">
        <h1 className="text-4xl font-bold text-primary pb-6">
          <span className="text-positive">+ev </span>
          betting model
        </h1>
        <p className="text-primary text-lg pb-4">
          In-depth statistics for an open source NBA player prop betting model based <br/> solely on 
          positive expected value.
        </p>
        <div className="flex items-center space-x-0.5">
          <a className="text-primary text-sm font-semibold hover:underline" href="https://github.com/ejjlittle/ev-betting-model">
            Check it out on GitHub
          </a>
          <ArrowRight className="text-primary w-4 h-4"/>
        </div>
      </div>
      <div className="p-5 pt-7 space-y-5 bg-background h-screen">
        <div className="flex flex-row justify-between space-x-5">
          <ProfitCard/>
          <ProfitChart/>
        </div>
        <BetTable/>
        <AboutCard/>
      </div>
    </div>
  )
}

export default App
