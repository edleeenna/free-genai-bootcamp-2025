
import { useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ChevronLeft, ChevronRight } from "lucide-react";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const sessions = [
  {
    id: 1,
    activityName: "Adventure MUD",
    groupName: "Core Verbs",
    startTime: "2024-02-20 14:30",
    endTime: "2024-02-20 15:00",
    reviewItems: 25,
  },
];

const Sessions = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = 1;

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Study Sessions</h1>
      
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Activity</TableHead>
              <TableHead>Group</TableHead>
              <TableHead>Start Time</TableHead>
              <TableHead>End Time</TableHead>
              <TableHead className="text-right">Review Items</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {sessions.map((session) => (
              <TableRow key={session.id}>
                <TableCell>{session.activityName}</TableCell>
                <TableCell>
                  <Link
                    to={`/groups/${session.id}`}
                    className="hover:text-japanese-600"
                  >
                    {session.groupName}
                  </Link>
                </TableCell>
                <TableCell>{session.startTime}</TableCell>
                <TableCell>{session.endTime}</TableCell>
                <TableCell className="text-right">{session.reviewItems}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

      <div className="flex items-center justify-center space-x-4 mt-4">
        <Button
          variant="outline"
          size="icon"
          disabled={currentPage === 1}
          onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
        >
          <ChevronLeft className="h-4 w-4" />
        </Button>
        <span className="text-sm">
          Page <strong>{currentPage}</strong> of {totalPages}
        </span>
        <Button
          variant="outline"
          size="icon"
          disabled={currentPage === totalPages}
          onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
        >
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
};

export default Sessions;
