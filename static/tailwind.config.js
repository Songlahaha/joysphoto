/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html"],
  theme: {
    container: {
      center: true,
      screens: {
        md: "1120px",
        lg: "1120px",
        xl: "1120px",
        "2xl": "1120px",
      },
    },
    extend: {
      colors: {
        primary: "#967E76",
        secondary: "#D7C0AE",
        third: "#EEE3CB",
        four: "#B7C4CF",
      },
    },
  },
  plugins: [],
}
