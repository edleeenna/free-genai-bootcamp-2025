
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { ArrowUpRight, Brain, Clock, Star } from "lucide-react";

const Dashboard = () => {
  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Welcome Back!</h1>
      
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4 mb-8">
        <Card className="animate-slide-in [animation-delay:100ms]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Words Learned
            </CardTitle>
            <Brain className="h-4 w-4 text-japanese-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">127</div>
            <div className="text-xs text-muted-foreground">
              +12 from last week
            </div>
          </CardContent>
        </Card>

        <Card className="animate-slide-in [animation-delay:200ms]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Accuracy Rate
            </CardTitle>
            <Star className="h-4 w-4 text-japanese-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">92%</div>
            <Progress value={92} className="h-2" />
          </CardContent>
        </Card>

        <Card className="animate-slide-in [animation-delay:300ms]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Study Streak
            </CardTitle>
            <ArrowUpRight className="h-4 w-4 text-japanese-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">7 days</div>
            <div className="text-xs text-muted-foreground">
              Keep it up!
            </div>
          </CardContent>
        </Card>

        <Card className="animate-slide-in [animation-delay:400ms]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Study Time
            </CardTitle>
            <Clock className="h-4 w-4 text-japanese-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">5.2h</div>
            <div className="text-xs text-muted-foreground">
              This week
            </div>
          </CardContent>
        </Card>
      </div>

      <Card className="animate-slide-in [animation-delay:500ms]">
        <CardHeader>
          <CardTitle>Last Session</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium">Vocabulary Practice</p>
                <p className="text-sm text-muted-foreground">
                  Core Verbs Group
                </p>
              </div>
              <div className="text-right">
                <p className="text-sm font-medium">Today, 2:30 PM</p>
                <p className="text-sm text-japanese-500">
                  85% accuracy
                </p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;
