import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
import { UNIT_SIZE } from "./constants"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function calcUnits(usd: number){
  return Math.round(usd / UNIT_SIZE * 100) / 100 //round two decimals
}

export function calcROI(wagered: number, profit: number){
  return Math.round(profit / wagered * 100 * 100) / 100 //round two decimals as percentage
}

export function formatNumber(num: number): string {
  if (num >= 1_000_000_000) {
      return (num / 1_000_000_000).toFixed(2) + "B"; // Billion
  } else if (num >= 1_000_000) {
      return (num / 1_000_000).toFixed(2) + "M"; // Million
  } else if (num >= 1_000) {
      return (num / 1_000).toFixed(2) + "K"; // Thousand
  } else {
      return num.toFixed(2); // Keep 2 decimal places for small numbers
  }
}