import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/api/person/")
      .then((res) => res.json())
      .then((res) => setData(res));
  }, []);

  return (
    <div className="App">
      <pre>{data && JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default App;
