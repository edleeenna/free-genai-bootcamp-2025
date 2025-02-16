
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

const groups = [
  {
    id: 1,
    name: "Core Verbs",
    wordCount: 50,
  },
  {
    id: 2,
    name: "Basic Adjectives",
    wordCount: 30,
  },
];

const Groups = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = 1;

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Word Groups</h1>
      
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Group Name</TableHead>
              <TableHead className="text-right">Words</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {groups.map((group) => (
              <TableRow key={group.id}>
                <TableCell>
                  <Link
                    to={`/groups/${group.id}`}
                    className="hover:text-japanese-600"
                  >
                    {group.name}
                  </Link>
                </TableCell>
                <TableCell className="text-right">{group.wordCount}</TableCell>
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
