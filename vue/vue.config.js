const path = require('path');

module.exports = {
    publicPath: '/vuefiles/static/src/vue/dist/',
    outputDir: path.resolve(__dirname, '../vuefiles/static/src/vue/dist/'),
    filenameHashing: false, 
    runtimeCompiler: true, 
    devServer: {
      devMiddleware: {
        writeToDisk: true, 
      }
    },
};