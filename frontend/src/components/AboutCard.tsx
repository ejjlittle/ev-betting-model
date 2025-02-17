import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"

export default function AboutCard(){
    return(
    <Card className="flex-1">
        <CardHeader className="flex items-center gap-2 space-y-0 border-b border-border py-5 flex-row">
            <div className="grid flex-1 gap-1 text-left">
                <CardTitle>About</CardTitle>
                <CardDescription>
                A short destription of the betting model
                </CardDescription>
            </div>
        </CardHeader>
        <CardContent>
            <p className="p-3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque efficitur, sapien vel fermentum pharetra, sapien nisl vehicula nulla, nec facilisis nulla felis in nunc. Integer suscipit, eros at gravida dignissim, arcu quam ullamcorper nulla, ut euismod est erat ut purus. Curabitur at fermentum elit. Vestibulum consectetur, felis id convallis feugiat, mauris augue lacinia purus, et scelerisque neque lectus a nisi.</p>
        </CardContent>
    </Card>
    )
}