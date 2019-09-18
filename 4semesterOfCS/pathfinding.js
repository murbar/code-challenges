const NO_ONE = 0;
const BY_A = 1;
const BY_B = 2;

const getNeighbors = (visited, x, y) => {
  const neighbors = [];

  if (y - 1 >= 0 && !visited[y - 1][x].closed) {
    // left
    neighbors.push(visited[y - 1][x]);
  }
  if (y + 1 < visited.length && !visited[y + 1][x].closed) {
    // right
    neighbors.push(visited[y + 1][x]);
  }
  if (x + 1 < visited[0].length && !visited[y][x + 1].closed) {
    // down
    neighbors.push(visited[y][x + 1]);
  }
  if (x - 1 >= 0 && !visited[y][x - 1].closed) {
    // up
    neighbors.push(visited[y][x - 1]);
  }
  return neighbors;
};

const findShortestPathLength = (maze, [xA, yA], [xB, yB]) => {
  const visited = maze.map((row, y) => {
    return row.map((point, x) => {
      return {
        closed: point === 1,
        length: 0,
        openedBy: NO_ONE,
        x,
        y
      };
    });
  });

  visited[yA][xA].openedBy = BY_A;
  visited[yB][xB].openedBy = BY_B;

  // BF traversals
  let aQueue = [visited[yA][xA]];
  let bQueue = [visited[yB][xB]];
  let iteration = 0;

  while (aQueue.length && bQueue.length) {
    iteration++;

    const aNeighbors = aQueue.reduce((result, neighbor) => {
      return [...result, ...getNeighbors(visited, neighbor.x, neighbor.y)];
    }, []);
    aQueue = [];
    for (let n of aNeighbors) {
      if (n.openedBy === BY_B) {
        return n.length + iteration;
      } else if (n.openedBy === NO_ONE) {
        n.length = iteration;
        n.openedBy = BY_A;
        aQueue.push(n);
      }
    }

    const bNeighbors = bQueue.reduce((result, neighbor) => {
      return [...result, ...getNeighbors(visited, neighbor.x, neighbor.y)];
    }, []);
    bQueue = [];
    for (let n of bNeighbors) {
      if (n.openedBy === BY_A) {
        return n.length + iteration;
      } else if (n.openedBy === NO_ONE) {
        n.length = iteration;
        n.openedBy = BY_B;
        bQueue.push(n);
      }
    }
  }

  // no path
  return -1;
};

const eightByEight = [
  [0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0],
  [0, 2, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 2]
];

console.assert(findShortestPathLength(eightByEight, [1, 7], [7, 7]) === 16, 'test 1');
