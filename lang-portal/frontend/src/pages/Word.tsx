
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Volume } from "lucide-react";
import api from "../components/api/axios";

const Word = () => {
  const { id } = useParams<{ id: string }>();

  const [word, setWord] = useState(null); // Start with null

  useEffect(() => {
    const fetchWord = async () => {
      try {
        const response = await api.get(`/words/${id}`);
        setWord(response.data); // Expect an object
        console.log(response.data);
      } catch (error) {
        console.error("Error fetching word:", error);
      }
    };

    fetchWord();
  }, [id]); // Dependency array prevents infinite re-renders

  if (!word) {
    return <p>Loading...</p>; // Prevent rendering before data loads
  }

  return (
    <div className="animate-fade-in space-y-8">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Word Details</h1>

      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-4">
            <span className="text-2xl">{word.japanese}</span>
            <Button variant="outline" size="icon">
              <Volume className="h-4 w-4" />
            </Button>
          </CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <p className="text-sm font-medium text-muted-foreground">Romaji</p>
            <p className="text-lg">{word.romaji}</p>
          </div>
          <div>
            <p className="text-sm font-medium text-muted-foreground">English</p>
            <p className="text-lg">{word.english}</p>
          </div>
          <div className="flex gap-8">
            <div>
              <p className="text-sm font-medium text-muted-foreground">Correct</p>
              <p className="text-lg text-green-600">{word.correct_count}</p>
            </div>
            <div>
              <p className="text-sm font-medium text-muted-foreground">Wrong</p>
              <p className="text-lg text-red-600">{word.wrong_count}</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default Word;
