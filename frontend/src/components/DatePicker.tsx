import * as React from "react"
import { format } from "date-fns"
import { Calendar as CalendarIcon } from "lucide-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"

interface DatePickerProps {
  date: Date;
  setDate: React.Dispatch<React.SetStateAction<Date>>;
}

export default function DatePicker({ date, setDate }: DatePickerProps) {
  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          variant={"outline"}
          className={cn(
            "w-[200px] justify-start text-left font-normal rounded-xl bg-background",
            !date && "text-muted-foreground"
          )}
        >
          <CalendarIcon className="mr-2 h-4 w-4" />
          {date ? format(date, "PPP") : format(new Date(), "PPP")}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-auto p-0 rounded-xl">
        <Calendar
          mode="single"
          selected={date}
          onSelect={(day) => {
            if (day) setDate(day); //only update if not undefined
          }}
          initialFocus
        />
      </PopoverContent>
    </Popover>
  )
}