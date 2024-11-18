/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html' // For all HTML files in the templates folder,
  ],
  theme: {
    extend: {
      colors: {
          blue: {
          50: 'rgb(30 79 67)',
          100: 'rgb(30 79 67)',
          200: 'rgb(30 79 67)',
          300: 'rgb(30 79 67)',
          400: 'rgb(30 79 67)',
          500: 'rgb(30 79 67)',
          600: 'rgb(30 79 67)',
          700: 'rgb(30 79 67)',
          800: 'rgb(30 79 67)',
          900: 'rgb(30 79 67)',
        },
        'primary': 'rgb(210 209 207)', // Warm beige for accents and highlights
        'accent': '#FFC857', // Golden yellow for calls-to-action
        'secondary-accent': 'rgb(30 79 67)', // Muted teal for secondary buttons and links
        'muted': '#A9A9A9', // Muted gray for less important text
        'alert':"#e36d69",
      }
    }
  },
  plugins: [],
}
