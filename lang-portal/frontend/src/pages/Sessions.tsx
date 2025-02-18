
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ChevronLeft, ChevronRight } from "lucide-react";
import api from "../components/api/axios";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import Words from "./Words";


const Sessions = ({studySessionId}) => {
  const { id } = useParams<{ id: string }>(); // Get groupId from URL if it exists
  const effectiveGroupId = studySessionId || id; // Use groupId prop or fallback to URL param

  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [sessions, setSessions] = useState([]);
  const itemsPerPage = 10; // Can adjust if needed

  useEffect(() => {
    const fetchSessions = async () => {
      try {
        const endpoint = effectiveGroupId
          ? `/groups/${effectiveGroupId}/study-sessions`
          : `/study-sessions`; // If groupId exists, fetch words for that group, else fetch all words

        console.log(`Fetching data for group ${effectiveGroupId || "all sessions"} (page ${currentPage})`);
        const response = await api.get(endpoint, {
          params: {
            page: currentPage, // Correct pagination parameter
            items_per_page: itemsPerPage, // Ensure items per page is set
          },
        });
        console.log("API response:", response.data); // Log the full response to inspect pagination
        setSessions(response.data.items); // Update the words state
        setTotalPages(response.data.pagination.total_pages); // Update the total pages state
      } catch (error) {
        console.error("Error fetching sessions:", error);
      }
    };

    fetchSessions();
  }, [currentPage, effectiveGroupId,id]); // Re-fetch data when current page or effectiveGroupId changes


  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Study Sessions</h1>
      
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Session Id</TableHead>
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
                <TableCell>  
                  <Link
                    to={`/sessions/${session.id}`}
                    className="hover:text-japanese-600">
                    {session.id}
                  </Link>
                  </TableCell>
                <TableCell>{session.study_activity_name}</TableCell>
                <TableCell>
              
                    {session.group_name}
                 
                </TableCell>
                <TableCell>{session.start_time}</TableCell>
                <TableCell>{session.end_time}</TableCell>
                <TableCell className="text-right">{session.review_items_count}</TableCell>
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
