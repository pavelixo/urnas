/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      // vue
      "./src/**/*.{vue,js,ts,jsx,tsx}",
  
      // django
      "./public/templates/**/*.{html,js}",
      "./public/static/**/*.{js,css}",
  
      // ignore
      "!./node_modules",
    ],
    theme: {
      extend: {},
    },
    plugins: [],
}