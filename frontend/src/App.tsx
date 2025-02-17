import { useState, useEffect } from "react"
import { Stats } from "./lib/models"
import fetchStats from "@/api/statsApi"
import ProfitChart from "@/components/ProfitChart"
import ProfitCard from "./components/ProfitCard"
import BetTable from "./components/BetTable"
import AboutCard from "./components/AboutCard"
import Header from "./components/Header"

function App() {
  const [stats, setStats] = useState<Stats[] | null>(null); //stats data
  const [loading, setLoading] = useState<boolean>(true); //loading state
  const [error, setError] = useState<string | null>(null); //error state

  useEffect(() => {
          const getStats = async () => {
              try {
                  setLoading(true);
                  const statsData = await fetchStats();
                  setStats(statsData);
              } catch (err) {
                  setError('Failed to fetch stats');
              } finally {
                  setLoading(false);
              }
          };
  
          getStats(); //call fetch on mount
      }, []); //only once when the component mounts

  return (
    <div className="bg-background">
      <Header />
      <div className="p-5 pt-7 space-y-5">
        <div className="flex flex-col space-x-0 space-y-5 lg:flex-row lg:space-x-5 lg:space-y-0">
          <ProfitCard stats={stats} loading={loading} error={error}/>
          <ProfitChart stats={stats} loading={loading} error={error}/>
        </div>
        <BetTable />
        <AboutCard />
      </div>
    </div>
  )
}

export default App
