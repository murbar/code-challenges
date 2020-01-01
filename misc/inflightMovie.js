// interview cake
// You've built an inflight entertainment system with on-demand movie streaming.
// Users on longer flights like to start a second movie right when their first one ends,
// but they complain that the plane usually lands before they can see the ending. So
// you're building a feature for choosing two movies whose total runtimes will
// equal the exact flight length.

// Write a function that takes an integer flightLength (in minutes) and an array of
// integers movieLengths (in minutes) and returns a boolean indicating whether there are
// two numbers in movieLengths whose sum equals flightLength.
// When building your function:
// Assume your users will watch exactly two movies
// Don't make your users watch the same movie twice
// Optimize for runtime over memory

// Gotchas
// We can do this in O(n) time, where n is the length of movieLengths.
// Remember: your users shouldn't watch the same movie twice. Are you sure your function
// won’t give a false positive if the array has one element that is half flightLength?

function canWatchTwoMovies(movieLengths, flightLength) {
  const movieCache = new Set();

  for (const length of movieLengths) {
    const secondMovieLength = flightLength - length;
    if (movieCache.has(secondMovieLength)) return true;
    movieCache.add(length);
  }

  return false;
}
