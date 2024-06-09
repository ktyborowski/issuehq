const defaultTheme = require('tailwindcss/defaultTheme');

/** @type {import('tailwindcss').Config} */
export default {
	darkMode: 'class',
	content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/preline/preline.js'],
	theme: {
		extend: {
			fontFamily: {
				sans: ['Inter Variable', ...defaultTheme.fontFamily.sans]
			}
		}
	},
	plugins: [require('preline/plugin'), require('@tailwindcss/forms')]
};
