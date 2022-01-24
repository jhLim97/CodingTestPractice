function solution(places) {
    const isInBoundary = (x, y) => {
        return x >=0 && x < 5 && y >= 0 && y < 5;
    }
    
    const isPerson = (arr, x, y) => {
        return arr[x][y] === 'P';
    }
    
    const isEmpty = (arr, x, y) => {
        return arr[x][y] === 'O';
    }
    
    const check = (arr, x, y) => {
        if (isInBoundary(x + 1, y)) {
            if (isPerson(arr, x + 1, y)) {
                return false;
            }
            if (isEmpty(arr, x + 1, y)) {
                if (isInBoundary(x + 2, y) && isPerson(arr, x + 2, y)) {
                    return false;
                }
                if (isInBoundary(x + 1, y + 1) && isPerson(arr, x + 1, y + 1)) {
                    return false;
                }
                if (isInBoundary(x + 1, y - 1) && isPerson(arr, x + 1, y - 1)) {
                    return false;
                }   
            }
        }
        if (isInBoundary(x - 1, y)) {
            if (isPerson(arr, x - 1, y)) {
                return false;
            }
            if (isEmpty(arr, x - 1, y)) {
                if (isInBoundary(x - 2, y) && isPerson(arr, x - 2, y)) {
                    return false;
                }
                if (isInBoundary(x - 1, y + 1) && isPerson(arr, x - 1, y + 1)) {
                    return false;
                }
                if (isInBoundary(x - 1, y - 1) && isPerson(arr, x - 1, y - 1)) {
                    return false;
                }   
            }
        }
        if (isInBoundary(x, y + 1)) {
            if (isPerson(arr, x, y + 1)) {
                return false;
            }
            if (isEmpty(arr, x, y + 1)) {
                if (isInBoundary(x, y + 2) && isPerson(arr, x, y + 2)) {
                    return false;
                }
            }
        }
        if (isInBoundary(x, y - 1)) {
            if (isPerson(arr, x, y - 1)) {
                return false;
            }
            if (isEmpty(arr, x, y - 1)) {
                if (isInBoundary(x, y - 2) && isPerson(arr, x, y - 2)) {
                    return false;
                }
            }
        }
        return true;
    }  
    
    const proceed = (arr) => {
        for (let i = 0; i < 5; i+=1) {
            for (let j = 0; j < 5; j+=1) {
                if (isPerson(arr, i, j)) {
                    if (!check(arr, i, j)) {
                        return false;   
                    }
                } 
            }
        }
        return true;
    }
    
    const result = [];
    for (let i = 0; i < 5; i+=1) {
        if (proceed(places[i])) {
            result.push(1);
            continue;
        }
        result.push(0);
    }
    
    return result;
}
