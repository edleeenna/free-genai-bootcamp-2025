
import { useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Volume, ChevronLeft, ChevronRight } from "lucide-react";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const words = [
  {
    id: 1,
    japanese: "食べる",
    romaji: "taberu",
    english: "to eat",
    correct: 15,
    wrong: 3,
  },
  // Add more words as needed
];

const Words = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = 3;

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Words</h1>
      
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Japanese</TableHead>
              <TableHead>Romaji</TableHead>
              <TableHead>English</TableHead>
              <TableHead className="text-right">Correct</TableHead>
              <TableHead className="text-right">Wrong</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {words.map((word) => (
              <TableRow key={word.id}>
                <TableCell>
                  <div className="flex items-center space-x-2">
                    <Link to={`/words/${word.id}`} className="hover:text-japanese-600">
                      {word.japanese}
                    </Link>
                    <Button variant="ghost" size="icon" className="h-6 w-6">
                      <Volume className="h-4 w-4" />
                    </Button>
                  </div>
                </TableCell>
                <TableCell>{word.romaji}</TableCell>
                <TableCell>{word.english}</TableCell>
                <TableCell className="text-right text-green-600">{word.correct}</TableCell>
                <TableCell className="text-right text-red-600">{word.wrong}</TableCell>
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

export default Words;
