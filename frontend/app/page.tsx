"use client";

import { useState } from "react";

export default function Home() {
  const [websiteUrl, setWebsiteUrl] = useState("");
  const [location, setLocation] = useState("US");
  const [monthlyBudget, setMonthlyBudget] = useState(5000);

  return (
    <main className="min-h-screen bg-slate-950 text-white p-10">
      <h1 className="text-4xl font-bold mb-6">ApexAds Autonomous AI Marketing OS</h1>
      <div className="grid gap-4 max-w-2xl">
        <input className="p-3 rounded bg-slate-900 border border-slate-700" placeholder="Website URL" value={websiteUrl} onChange={(e) => setWebsiteUrl(e.target.value)} />
        <input className="p-3 rounded bg-slate-900 border border-slate-700" placeholder="Location" value={location} onChange={(e) => setLocation(e.target.value)} />
        <input className="p-3 rounded bg-slate-900 border border-slate-700" type="number" placeholder="Monthly Budget" value={monthlyBudget} onChange={(e) => setMonthlyBudget(Number(e.target.value))} />
        <button className="bg-cyan-500 hover:bg-cyan-400 text-slate-900 font-semibold p-3 rounded">
          Generate Strategy
        </button>
      </div>
      <p className="mt-8 text-slate-300">Outputs include keyword strategy, campaign structure, generated ads, live metrics, and optimization suggestions.</p>
    </main>
  );
}
