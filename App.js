import { Routes, Route } from "react-router-dom";

import Login from "./landing/Login";
import Register from "./landing/Register";
import Home from "./home/Home";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/home/*" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;
