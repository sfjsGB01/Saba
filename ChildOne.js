import React from "react";

import GrandChildOne from "./GrandChildOne";
import GrandChildTwo from "./GrandChildTwo";

const ChildOne = () => {
  return (
    <div className="child">
      <GrandChildOne />

      <GrandChildTwo />
    </div>
  );
};

export default ChildOne;
