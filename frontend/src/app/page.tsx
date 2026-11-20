export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="max-w-6xl mx-auto p-8">

        <h1 className="text-5xl font-bold mb-4">
          TEXT TO SQL
        </h1>

        <p className="text-slate-400 mb-8">
          AI-powered Text to SQL with schema understanding,
          relationship visualisation and self-correcting queries.
        </p>

        <div className="border border-slate-700 rounded-xl p-8">
          <h2 className="text-xl font-semibold mb-4">
            Upload SQL File
          </h2>

          <button
            className="
              px-4
              py-2
              bg-blue-600
              rounded-lg
              hover:bg-blue-500
            "
          >
            Choose File
          </button>
        </div>

      </div>
    </main>
  );
}