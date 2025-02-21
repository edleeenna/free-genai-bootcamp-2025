
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { ArrowUpRight, Brain, Clock, Star } from "lucide-react";
import { format } from "date-fns";


import { useEffect, useState } from "react";
import api from "../components/api/axios";

const Dashboard = () => {
  
    const [study_session, setStudySession] = useState(null); // Start with null
    const [study_progress, setStudyProgress] = useState(null);
    const [quick_stats, setQuickStats] = useState(null);

    useEffect(() => {
      const fetchDashboard = async () => {
        try {
          const study_response = await api.get(`/dashboard/last-study-session`);
          setStudySession(study_response.data); // Expect an object
          const study_progress_response = await api.get(`/dashboard/study-progress`);
          setStudyProgress(study_progress_response.data); // Expect an object
          const quick_stats_response = await api.get(`/dashboard/quick-stats`);
          setQuickStats(quick_stats_response.data); // Expect an object
        } catch (error) {
          console.error("Error fetching word:", error);
        }
      };
  
      fetchDashboard();
    }, ); // Dependency array prevents infinite re-renders
    if (!study_session || !study_progress || !quick_stats) {
    return <p>Loading...</p>; // Prevent rendering before data loads
  }

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
            <div className="text-2xl font-bold">{quick_stats.words_learned}</div>
            <div className="text-xs text-muted-foreground">
              +12 from last week
            </div>
          </CardContent>
        </Card>

        <Card className="animate-slide-in [animation-delay:400ms]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Words in progress
            </CardTitle>
            <Clock className="h-4 w-4 text-japanese-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{quick_stats.words_in_progress}</div>
            <div className="text-xs text-muted-foreground">
              This week
            </div>
          </CardContent>
        </Card>

        <Card className="animate-slide-in [animation-delay:200ms]">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Success Rate
            </CardTitle>
            <Star className="h-4 w-4 text-japanese-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{quick_stats.success_rate.toFixed(2)} %</div>
            <Progress value={quick_stats.success_rate.toFixed(2)} className="h-2" />
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
            <div className="text-2xl font-bold">{quick_stats.study_streak}</div>
            <div className="text-xs text-muted-foreground">
              Keep it up!
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
                  {study_session.group_name}
                </p>
              </div>
              <div className="text-right">
                <p className="text-sm font-medium">Start time</p>
                <p className="text-sm text-japanese-500">
                {}
                {format(new Date(study_session.start_time), "do MMMM yyyy, h:mm a")}
                </p>
              </div>
              <div className="text-right">
                <p className="text-sm font-medium">End time</p>
                <p className="text-sm text-japanese-500">
                {format(new Date(study_session.end_time), " do MMMM yyyy, h:mm a")}
                </p>
              </div>
              <div className="text-right">
                <p className="text-sm font-medium">Items Reviewed</p>
                <p className="text-sm text-japanese-500">
                {study_session.review_items_count}
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
