import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import api from "../components/api/axios";
import Words from "./Words";

const Session = () => {
  const { id } = useParams<{ id: string }>(); // Get the session ID from the URL
  const [session, setSession] = useState(null); // Store the session data
  const [loading, setLoading] = useState(true); // Loading state
  const [error, setError] = useState<string | null>(null); // Error state

  useEffect(() => {
    const fetchSession = async () => {
      try {
        setLoading(true);
        const response = await api.get(`/study-sessions/${id}`); // Fetch a single session based on the ID
        setSession(response.data); // Set the session data
      } catch (error) {
        setError("Failed to fetch session data");
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    fetchSession();
  }, [id]); // Re-fetch when the session ID changes

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  if (!session) {
    return <div>No session found.</div>;
  }

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Study Session Details</h1>

      <div className="rounded-md border p-4">
        <div className="mb-4">
          <strong>Session ID:</strong> {session.id}
        </div>
        <div className="mb-4">
          <strong>Activity:</strong> {session.study_activity_name}
        </div>
        <div className="mb-4">
          <strong>Group:</strong> {session.group_name}
        </div>
        <div className="mb-4">
          <strong>Start Time:</strong> {session.start_time}
        </div>
        <div className="mb-4">
          <strong>End Time:</strong> {session.end_time}
        </div>
        <div className="mb-4">
          <strong>Review Items:</strong> {session.review_items_count}
        </div>
      </div>

      <Words studySessionId={id} />   {/* Pass in the study session Id */}

      <Link to="/sessions" className="mt-4 inline-block text-blue-600 hover:underline">
        Back to Sessions
      </Link>
    </div>
  );
};

export default Session;
