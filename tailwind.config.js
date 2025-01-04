/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        'hubot': ['Hubot Sans', 'sans-serif'],
        'fraunces': ['Fraunces', 'serif']
      }
    },
  },
  plugins: [],
}

