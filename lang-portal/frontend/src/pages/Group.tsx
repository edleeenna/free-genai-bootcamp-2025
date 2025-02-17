
import { useParams } from "react-router-dom";
import Words from "./Words";

const Group = () => {
  const { id } = useParams<{ id: string }>();

  return (
    <div className="animate-fade-in">
      <h1 className="text-4xl font-bold mb-8 text-japanese-800">Core Verbs</h1>
      <Words />
    </div>
  );
};

export default Group;
