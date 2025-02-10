import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"
const UNIT_SIZE = 50

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function calcUnits(usd: number){
  return Math.round(usd / UNIT_SIZE * 100) / 100
}