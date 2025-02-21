import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
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

const Groups = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [wordGroups, setGroups] = useState([]);
  const itemsPerPage = 10; // Can adjust if needed

  useEffect(() => {
    const fetchGroups = async () => {
      try {
        const response = await api.get(`/groups`, {
          params: {
            page: currentPage, // Correct pagination parameter
            items_per_page: itemsPerPage, // Ensure items per page is set
          },
        });
        setGroups(response.data.items); // Directly set the data
        console.log(response.data.pagination.total_pages)
        setTotalPages(1); // Change if backend has pagination
      } catch (error) {
        console.error("Error fetching groups:", error);
      }
    };

    fetchGroups();
  }, [currentPage]);

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Word Groups</h1>

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Group Name</TableHead>
              <TableHead>Word Count</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {wordGroups.map((group) => (
              <TableRow key={group.group_id}>

                <TableCell>  <Link
                    to={`/groups/${group.id}`}
                    className="hover:text-japanese-600"
                  >{group.name}</Link></TableCell>
                <TableCell>
                
                    {group.word_count}
                
                </TableCell>
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

export default Groups;
