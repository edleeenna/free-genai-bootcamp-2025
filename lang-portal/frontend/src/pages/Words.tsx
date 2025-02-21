import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Volume, ChevronLeft, ChevronRight } from "lucide-react";
import api from "../components/api/axios";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const Words = ({ studySessionId = null, groupId = null }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [words, setWords] = useState([]);
  const [loading, setLoading] = useState(true); // Loading state
  const [error, setError] = useState(null); // Error state
  const itemsPerPage = 10;

  useEffect(() => {
    const fetchWords = async () => {
      setLoading(true);
      setError(null);
      try {
        let endpoint = "/words";
        if (studySessionId) {
          endpoint = `/study-sessions/${studySessionId}/words`;
        } else if (groupId) {
          endpoint = `/groups/${groupId}/words`;
        }
  
        console.log(`Fetching from ${endpoint} for page ${currentPage}`);
  
        const response = await api.get(endpoint, {
          params: {
            page: currentPage,
            items_per_page: itemsPerPage,
          },
        });
  
        console.log("API Response Data:", response.data);
  
        // Directly use response.data if it's an array of words
             // Handle response data for study sessions and groups
      let wordsData = [];
      if (Array.isArray(response.data)) {
        wordsData = response.data; // for study-sessions/:id/words, response is an array
      } else if (Array.isArray(response.data.items)) {
        wordsData = response.data.items; // for groups/:id/words, items is an array
      }
        
// Ensure we are using the array data
        const pagination = response.data.pagination || { total_pages: 1 };
  
        setWords(wordsData);
        setTotalPages(pagination.total_pages);
  
        if (wordsData.length === 0 && currentPage > 1) {
          setCurrentPage(1); // Reset to page 1 if no words are found
        }
      } catch (error) {
        console.error("Error fetching words:", error);
        setError("Failed to load words. Please try again later.");
      } finally {
        setLoading(false);
      }
    };
  
    fetchWords();
  }, [currentPage, studySessionId, groupId]);
  
  
  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Words</h1>
  
      {loading ? (
        <div>Loading...</div> // Display loading message
      ) : error ? (
        <div className="text-red-600">{error}</div> // Display error message
      ) : (
        <>
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
                {words.length > 0 ? (
                  words.map((word) => (
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
                      <TableCell className="text-right text-green-600">{word.correct_count}</TableCell>
                      <TableCell className="text-right text-red-600">{word.wrong_count}</TableCell>
                    </TableRow>
                  ))
                ) : (
                  <TableRow>
                    <TableCell colSpan={5} className="text-center">
                      No words available.
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </div>
  
          <div className="flex items-center justify-center space-x-4 mt-4">
            <Button
              variant="outline"
              size="icon"
              disabled={currentPage === 1 || words.length === 0} // Disable if no words available
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
              disabled={currentPage === totalPages || words.length === 0} // Disable if no words available
              onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
            >
              <ChevronRight className="h-4 w-4" />
            </Button>
          </div>
        </>
      )}
    </div>
  );
}  

export default Words;
