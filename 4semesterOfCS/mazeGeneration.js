// depth-first traversal

const shuffle = array => {
  const shuffled = [...array];
  for (let i = shuffled.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
};

const getRandomDirections = () => shuffle(['n', 'e', 's', 'w']);

const getDeltas = cardinal => {
  if (cardinal === 'n') return [0, 1];
  if (cardinal === 's') return [0, -1];
  if (cardinal === 'e') return [1, 0];
  if (cardinal === 'w') return [-1, 0];
  throw Error('Invalid direction');
};

const getOpposite = cardinal => {
  if (cardinal === 'n') return 's';
  if (cardinal === 's') return 'n';
  if (cardinal === 'e') return 'w';
  if (cardinal === 'w') return 'e';
  throw Error('Invalid direction');
};

const nextNode = (x, y, maze) => {
  const node = maze[y][x];
  node.visited = true;
  getRandomDirections().forEach(d => {
    const [xDelta, yDelta] = getDeltas(d);

    // exists and not visited
    if (
      maze[y + yDelta] &&
      maze[y + yDelta][x + xDelta] &&
      !maze[y + yDelta][x + xDelta].visited
    ) {
      node[d] = false;
      maze[y + yDelta][x + xDelta][getOpposite(d)] = false;
      nextNode(x + xDelta, y + yDelta, maze);
    }
  });
};

const generateMaze = (maze, [xStart, yStart]) => {
  nextNode(xStart, yStart, maze);
  return maze;
};
