var gulp = require('gulp');
var browserSync = require('browser-sync');
var rename = require('gulp-rename');
var reload = browserSync.reload;
var exec = require('child_process').exec;

//Run Flask server
gulp.task('runserver', function() {
    var proc = exec('pipenv run python ../run.py');
});

gulp.task('browser-sync', gulp.parallel('runserver', function() {
  browserSync({
    notify: false,
    proxy: "localhost:5000",
    host: "localhost",
    port: "5000"
  });
}));

gulp.task('watch', function() {
    gulp.watch(["templates/**/*.html", "static/**/*.js", "scss/**/*.scss", "*.py"]).on('change', reload);
});

gulp.task('default',  gulp.parallel('watch', 'browser-sync'));