var postcss = require('gulp-postcss');
var gulp = require('gulp');

gulp.task('css', function () {
    const postcss = require('gulp-postcss')
    const rename = require('gulp-rename');
    return gulp.src('./base.css')
      // ...
      .pipe(postcss([
        // ...
        require('tailwindcss'),
        require('autoprefixer'),
        // ...
      ]))
      .pipe(rename('style.css'))
      .pipe(gulp.dest('./'))
  })