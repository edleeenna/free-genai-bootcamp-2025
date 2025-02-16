
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ExternalLink, Eye } from "lucide-react";

const activities = [
  {
    id: 1,
    title: "Adventure MUD",
    thumbnail: "/placeholder.svg",
    description: "Interactive text-based Japanese learning game",
  },
  {
    id: 2,
    title: "Typing Tutor",
    thumbnail: "/placeholder.svg",
    description: "Practice typing Japanese characters",
  },
];

const StudyActivities = () => {
  const handleLaunch = (id: number) => {
    window.open(`http://localhost:8081?group_id=${id}`, '_blank');
  };

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Study Activities</h1>
      
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {activities.map((activity) => (
          <Card key={activity.id} className="animate-slide-in card-hover">
            <CardHeader>
              <img
                src={activity.thumbnail}
                alt={activity.title}
                className="rounded-lg mb-4 h-40 w-full object-cover"
              />
              <CardTitle>{activity.title}</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <p className="text-sm text-muted-foreground">
                {activity.description}
              </p>
              <div className="flex gap-2">
                <Button
                  onClick={() => handleLaunch(activity.id)}
                  className="flex-1"
                >
                  <ExternalLink className="mr-2 h-4 w-4" />
                  Launch
                </Button>
                <Button
                  variant="outline"
                  onClick={() => window.location.href = `/study-activities/${activity.id}`}
                >
                  <Eye className="mr-2 h-4 w-4" />
                  View
                </Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default StudyActivities;
