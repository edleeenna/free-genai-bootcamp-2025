"use client"

import type React from "react"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Copy, Loader2 } from "lucide-react"
import { useToast } from "@/components/ui/use-toast"

export default function VocabularyForm() {
  const [theme, setTheme] = useState("")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)
  const { toast } = useToast()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const response = await fetch("/api/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ theme }),
      })

      if (!response.ok) {
        throw new Error("Failed to generate vocabulary")
      }

      const data = await response.json()
      setResult(JSON.stringify(data, null, 2))
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to generate vocabulary. Please try again.",
        variant: "destructive",
      })
    } finally {
      setLoading(false)
    }
  }

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(result)
      toast({
        title: "Copied!",
        description: "The vocabulary data has been copied to your clipboard.",
      })
    } catch (error) {
      toast({
        title: "Error",
        description: "Failed to copy to clipboard. Please try again.",
        variant: "destructive",
      })
    }
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>Generate Vocabulary</CardTitle>
        <CardDescription>Enter a thematic category to generate Japanese vocabulary</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="space-y-2">
            <Label htmlFor="theme">Thematic Category</Label>
            <Input
              id="theme"
              placeholder="e.g., food, weather, emotions"
              value={theme}
              onChange={(e) => setTheme(e.target.value)}
              required
            />
          </div>
          <Button type="submit" disabled={loading} className="w-full">
            {loading && <Loader2 className="mr-2 h-4 w-4 animate-spin" />}
            Generate Vocabulary
          </Button>

          {result && (
            <div className="space-y-2">
              <div className="flex items-center justify-between">
                <Label>Generated Vocabulary</Label>
                <Button type="button" variant="outline" size="sm" onClick={handleCopy}>
                  <Copy className="h-4 w-4 mr-2" />
                  Copy
                </Button>
              </div>
              <Textarea value={result} readOnly className="font-mono h-[300px]" />
            </div>
          )}
        </form>
      </CardContent>
    </Card>
  )
}

