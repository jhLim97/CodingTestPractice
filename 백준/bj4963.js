function test(w, h, graph) {
  const dx = [-1, 0, 1, 0, -1, -1, 1, 1];
  const dy = [0, 1, 0, -1, -1, 1, 1, -1];

  const proceed = (i, j) => {
    graph[i][j] = 0;

    for (let k = 0; k < 8; k += 1) {
      const nx = i + dx[k];
      const ny = j + dy[k];

      if (nx < 0 || nx >= h || ny < 0 || ny >= w || graph[nx][ny] !== 1) {
        continue;
      }

      proceed(nx, ny);
    }
  };

  let result = 0;
  for (let i = 0; i < h; i += 1) {
    for (let j = 0; j < w; j += 1) {
      if (graph[i][j] === 1) {
        proceed(i, j);
        result += 1;
      }
    }
  }

  return result;
}
