
import { useParams } from "react-router-dom";
import Words from "./Words";
import { useEffect, useState } from "react";
import api from "../components/api/axios";

const Group = () => {
  const { id } = useParams<{ id: string }>();

  const [group, setGroup] = useState(null); // Start with null

  useEffect(() => {
    const fetchGroup = async () => {
      try {
        const response = await api.get(`/groups/${id}`);
        setGroup(response.data); // Expect an object
        console.log(response.data);
      } catch (error) {
        console.error("Error fetching word:", error);
      }
    };

    fetchGroup();
  }, [id]); // Dependency array prevents infinite re-renders

  if (!group) {
    return <p>Loading...</p>; // Prevent rendering before data loads
  }

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">{group.name}</h1>
      <Words />
    </div>
  );
};

export default Group;
