function solution(m, n, board) {
    const dx = [1, 0, 1];
    const dy = [0, 1, 1];
    board = board.map((_board) => _board.split(''));
    const isSquare = (x, y) => {
        const character = board[x][y];
        
        for (let i = 0; i < 3; i += 1) {
            const nx = x + dx[i];
            const ny = y + dy[i];
            
            if (nx < 0 || nx >= m || ny < 0 || ny >= n || board[nx][ny] !== character) {
                return false;
            }
        }
        
        return true;
    }
    
    const removeSqure = (removeList) => {
        removeList.forEach(([x, y]) => {
            board[x][y] = 'a';
            for (let i = 0; i < 3; i += 1) {
                const nx = x + dx[i];
                const ny = y + dy[i];

                board[nx][ny] = 'a';
            }
        })
    }

    const updateEmptyArea = () => {
        for (let i = m - 1; i >= 0; i -= 1) {
            if (!board[i].some((_board) => _board === 'a')) {
                continue;
            }
            
            for (let j = 0; j < n; j += 1) {
                if (board[i][j] !== 'a') continue;
                for (let k = i - 1; k >= 0; k -= 1) {
                    if (board[k][j] !== 'a') {
                        board[i][j] = board[k][j];
                        board[k][j] = 'a';
                        break;
                    }
                }
            }
        }
    }
    
    while (true) {
        const removeList = [];
        for (let i = 0; i < m; i += 1) {
            for (let j = 0; j < n; j += 1) {
                if (board[i][j] !== 'a' && isSquare(i, j)) {
                    removeList.push([i, j]);
                }
            }
        }
        if (removeList.length === 0) break;
        removeSqure(removeList);
        updateEmptyArea();
    }
    
    let count = 0;
    board.forEach((_board) => {
        let index = _board.indexOf('a');
        while (index !== -1) {
            count += 1;
            index = _board.indexOf('a', index + 1);
        }
    })
    
    return count;
}
