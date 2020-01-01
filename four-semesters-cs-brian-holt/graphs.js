// breadth-first traversal

const findMostCommonTitle = (myId, getUser, degreesOfSeparation) => {
  let queue = [myId];
  const seen = new Set();
  const jobs = {};

  for (let i = 0; i <= degreesOfSeparation; i++) {
    queue = queue
      .filter(id => !seen.has(id))
      .map(getUser)
      .map(user => {
        jobs[user.title] = jobs[user.title] ? jobs[user.title] + 1 : 1;
        seen.add(user.id);
        return user;
      })
      .map(user => user.connections)
      .reduce((acc, users) => [...acc, ...users], []);
  }

  return Object.entries(jobs).reduce((mostCommonJob, job) => {
    return job[1] > mostCommonJob[1] ? job : mostCommonJob;
  });
};
