/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
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
            olive: '#00321e',
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
