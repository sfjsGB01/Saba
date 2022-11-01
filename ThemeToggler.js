import React from "react";

import { useTheme } from "./hooks/useTheme";

const ThemeToggler = () => {
  const themeContext = useTheme();

  return (
    <div className="theme-toggler">
      <input
        type="button"
        onClick={themeContext?.toggleTheme}
        value="Toggle Theme"
      />
    </div>
  );
};

export default ThemeToggler;
