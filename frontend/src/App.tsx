import ProfitChart from "@/components/ProfitChart"
import ProfitCard from "./components/ProfitCard"
import BetTable from "./components/BetTable"
import AboutCard from "./components/AboutCard"
import Header from "./components/Header"

function App() {

  return (
    <div className="bg-background">
      <Header />
      <div className="p-5 pt-7 space-y-5">
        <div className="flex flex-row justify-between space-x-5">
          <ProfitCard />
          <ProfitChart />
        </div>
        <BetTable />
        <AboutCard />
      </div>
    </div>
  )
}

export default App
