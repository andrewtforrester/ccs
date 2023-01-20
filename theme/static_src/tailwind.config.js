/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        '../../home/templates/home/*.html',
        '../../ccs/templates/*.html',
        '../../ccs/templates/_partials/*.html',
        '../../vue/src/**/*',
    ],
    theme: {
        colors: {
            transparent: 'transparent',
            white: 'white',
            black: 'black',
            navy: '#15182f',
            gray: '#d3d6d6',
            burgundy: '#51100d',
            olive: '#556b2f',
            rose: '#d38c95',
        },
        extend: {
            fontFamily: {
                'sans': ['Lato'],
                'serif':['EB Garamond'],
                'display':['Abril Fatface'],
            },
        }
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
