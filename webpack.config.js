const path = require('path');

const webpack = require('webpack');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const ManifestPlugin = require('webpack-manifest-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const TerserPlugin = require('terser-webpack-plugin');


module.exports = (env, argv) => {
  const prodMode = argv.mode === 'production';
  // 'chunkhash' does not work with hot reloading for some reason
  const baseName = argv.inline ? '[name]' : '[name].[chunkhash:4]';

  return {
    resolve: {
      modules: [
        path.resolve(__dirname, 'assets'),
        path.resolve(__dirname, 'node_modules'),
      ]
    },
    entry: {
      common: path.resolve(__dirname, 'assets/js/common.js'),
      helloworld: path.resolve(__dirname, 'assets/js/helloworld.js'),
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          loader: 'babel-loader',
        },
        {
          test: /\.(css|scss)$/,
          use: [
            {
              loader: MiniCssExtractPlugin.loader,
              options: {
                hmr: !prodMode,
              }
            },
            {
              loader: 'css-loader',
              options: {
                sourceMap: true,
              }
            },
            {
              loader: "sass-loader",
              options: {
                sourceMap: true,
              }
            },
          ],
        },
        {
          test: /\.(woff|woff2|eot|ttf|otf)$/,
          use: [
            'file-loader'
          ]
        },
        {
          test: /\.(png|svg|jpg|gif)$/,
          use: [
            'file-loader'
          ]
        },
      ],
    },
    output: {
      path: path.resolve(__dirname, 'static/dist'),
      publicPath: '/static/dist/',
      filename: `${baseName}.bundle.js`
    },
    devServer: {
      hot: true,
      writeToDisk: filePath => filePath.endsWith('/manifest.json'),
      overlay: {
        errors: true,
      },
      proxy: {
        '/': {
          target: process.env.PROXY_TARGET_URL || 'http://localhost:8000',
        }
      }
    },
    optimization: {
      minimizer: [
        new OptimizeCSSAssetsPlugin({}),
        new TerserPlugin(),  // default webpack JS minimizer
      ],
      splitChunks: {
        chunks: 'all'
      },
    },
    plugins: [
      new CleanWebpackPlugin(),
      new MiniCssExtractPlugin({
        filename: `${baseName}.bundle.css`,
      }),
      new ManifestPlugin(),
    ],
    devtool: 'source-map',
  }
};
