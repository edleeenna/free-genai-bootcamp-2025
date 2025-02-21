# Prompt for v0.dev

Give me please a vocabulary language imported where we have a text field that sllows us to import a thematic category for the generation of language vocabulary.

When submitting that text field, it should hit an api endpoint (api route in app router) to invoke an LLM chat completions in Groq (LLM) on the server-side and then pass that information back to the frontend

It has to create a structured json output:

[{"kanji": "良い",
      "romaji": "ii",
      "english": "good",
      "parts": [
        {
          "kanji": "良",
          "romaji": ["i"]
        },
        {
          "kanji": "い",
          "romaji": ["i"]
        }
      ]}]

The json that is outputted back to the frontend should be copyable, so it should be sent to an input field and there should be a copy button so that is can be copied to the clipboard and that should give an alert that it was copied to the users clipboard

The app should use app router and the latest version of next.js and the llm calls should run in an api route on the server side
