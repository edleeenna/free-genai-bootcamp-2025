
import { useParams } from "react-router-dom";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Volume } from "lucide-react";

const Word = () => {
  const { id } = useParams<{ id: string }>();

  const word = {
    id: Number(id),
    japanese: "食べる",
    romaji: "taberu",
    english: "to eat",
    correct: 15,
    wrong: 3,
  };

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
              <p className="text-lg text-green-600">{word.correct}</p>
            </div>
            <div>
              <p className="text-sm font-medium text-muted-foreground">Wrong</p>
              <p className="text-lg text-red-600">{word.wrong}</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default Word;
