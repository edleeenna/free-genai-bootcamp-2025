import { createOpenAI as createGroq } from "@ai-sdk/openai"
import { generateText } from "ai"

const groq =  createGroq({
  baseURL: "https://api.groq.com/openai/v1",
  apiKey: process.env.GROQ_API_KEY,
})

export async function POST(req: Request) {
  try {
    const { theme } = await req.json()

    const prompt = `Generate a Japanese vocabulary list for the theme "${theme}". 
    Return the response as a JSON array where each item has the following structure:
    {
      "kanji": "漢字",
      "romaji": "romaji reading",
      "english": "english translation",
      "parts": [
        {
          "kanji": "individual kanji character",
          "romaji": ["possible readings"]
        }
      ]
    }
    Include 5 vocabulary items related to the theme and send back raw json and nothing else.
    
    There is an exmaple of bad output

   {
    "kanji": "晴れ",
    "romaji": "hare",
    "english": "sunny",
    "parts": [
      {
        "kanji": "晴",
        "romaji": [
          "seki",
          "haru"
        ]
      }
    
      The reason this is bad is because the parts of romaji that are shown do not represent the word.
      Instead of listing out seki haru, it should just say ha because is what the kanji is representing for that word hare.
      Another reason why the output is bad is because it is missing the other part. There should be two parts, one for ha and the other for re.

      Here is an examples of good output:

   {
    "kanji": "良い",
    "romaji": "yoi",
    "english": "good",
    "parts": [
      { "kanji": "良", "romaji": ["yo"] },
      { "kanji": "い", "romaji": ["i"] }
    ]
  },
  {
    "kanji": "古い",
    "romaji": "furui",
    "english": "old",
    "parts": [
      { "kanji": "古", "romaji": ["fu", "ru"] },
      { "kanji": "い", "romaji": ["i"] }
    ]
  },
  {
    "kanji": "忙しい",
    "romaji": "isogashii",
    "english": "busy",
    "parts": [
      { "kanji": "忙", "romaji": ["i","so","ga"] },
      { "kanji": "し", "romaji": ["shi"] },
      { "kanji": "い", "romaji": ["i"] }
    ]
  },
  {
    "kanji": "新しい",
    "romaji": "atarashii",
    "english": "new",
    "parts": [
      { "kanji": "新", "romaji": ["a","ta","ra"] },
      { "kanji": "し", "romaji": ["shi"] },
      { "kanji": "い", "romaji": ["i"] }
    ]
  },
  {
    "kanji": "悪い",
    "romaji": "warui",
    "english": "bad",
    "parts": [
      { "kanji": "悪", "romaji": ["wa","ru"] },
      { "kanji": "い", "romaji": ["i"] }
    ]
  },
  {
    "kanji": "悲しい",
    "romaji": "kanashii",
    "english": "sad",
    "parts": [
      { "kanji": "悲", "romaji": ["ka","na"] },
      { "kanji": "し", "romaji": ["shi"] },
      { "kanji": "い", "romaji": ["i"] }
    ]
  },

        this is a good output because the word represents all the kanji and kana characters shown in the word.
    `

    const { text } = await generateText({
      model: groq("gemma2-9b-it"),
      prompt,
    })

    // Parse the response to ensure it's valid JSON
    const vocabularyList = JSON.parse(text)

    return Response.json(vocabularyList)
  } catch (error) {
    console.error("Error generating vocabulary:", error)
    return Response.json({ error: "Failed to generate vocabulary" }, { status: 500 })
  }
}

