import VocabularyForm from "@/components/vocabulary-form"

export default function Home() {
  return (
    <main className="container mx-auto p-4 max-w-2xl min-h-screen py-12">
      <h1 className="text-3xl font-bold mb-8 text-center">Japanese Vocabulary Generator</h1>
      <VocabularyForm />
    </main>
  )
}

