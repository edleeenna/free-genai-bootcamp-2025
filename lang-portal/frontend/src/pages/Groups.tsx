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
  const [wordGroups, setWordGroups] = useState([]);

  useEffect(() => {
    const fetchWordGroups = async () => {
      try {
        const response = await api.get(`/word-groups`);
        setWordGroups(response.data); // Directly set the data
        console.log(response.data)
        setTotalPages(1); // Change if backend has pagination
      } catch (error) {
        console.error("Error fetching word groups:", error);
      }
    };

    fetchWordGroups();
  }, [currentPage]);

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Word Groups</h1>

      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Word ID</TableHead>
              <TableHead>Group ID</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {wordGroups.map((group) => (
              <TableRow key={group.word_id}>
                <TableCell>{group.word_id}</TableCell>
                <TableCell>
                  <Link
                    to={`/groups/${group.group_id}`}
                    className="hover:text-japanese-600"
                  >
                    {group.group_id}
                  </Link>
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
