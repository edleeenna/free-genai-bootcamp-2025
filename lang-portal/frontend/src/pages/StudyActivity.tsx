
import { useParams } from "react-router-dom";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ExternalLink } from "lucide-react";

const StudyActivity = () => {
  const { id } = useParams<{ id: string }>();

  const activity = {
    id: Number(id),
    title: "Adventure MUD",
    thumbnail: "/placeholder.svg",
    description: "Interactive text-based Japanese learning game where you can practice your language skills in a fun and engaging way.",
    sessions: [
      {
        id: 1,
        groupName: "Core Verbs",
        startTime: "2024-02-20 14:30",
        endTime: "2024-02-20 15:00",
        reviewItems: 25,
      },
    ],
  };

  return (
    <div className="animate-fade-in space-y-8">
      <div className="flex items-start justify-between">
        <div>
          <h1 className="text-4xl font-bold mb-2 text-japanese-800">
            {activity.title}
          </h1>
          <p className="text-muted-foreground">{activity.description}</p>
        </div>
        <Button onClick={() => window.open(`http://localhost:8081?group_id=${id}`, '_blank')}>
          <ExternalLink className="mr-2 h-4 w-4" />
          Launch Activity
        </Button>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Recent Sessions</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {activity.sessions.map((session) => (
              <div
                key={session.id}
                className="flex items-center justify-between border-b pb-4"
              >
                <div>
                  <p className="font-medium">{session.groupName}</p>
                  <p className="text-sm text-muted-foreground">
                    {session.startTime} - {session.endTime}
                  </p>
                </div>
                <div className="text-right">
                  <p className="text-sm font-medium">{session.reviewItems} items</p>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default StudyActivity;
