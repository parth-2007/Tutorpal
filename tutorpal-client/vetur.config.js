module.exports = {
  settings: {
    'vetur.useWorkspaceDependencies': true,
    'vetur.experimental.templateInterpolationService': true,
  },
  projects: [
    {
      package: './package.json',
      jsconfig: './jsconfig.json',
      // globalComponents: ['./src/components/**/*.vue'],
    },
  ],
}
