function solution(expression) {
    const operations = ['*', '+', '-'];
    const operators = {
        '*': (left, right) => left * right,
        '+': (left, right) => left + right,
        '-': (left, right) => left - right,
    }
    
    const getPermutations = (arr, selectNumber) => {
        const results = [];
        if (selectNumber === 1) return arr.map((el) => [el]); 

        arr.forEach((fixed, index, origin) => {
          const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
          const permutations = getPermutations(rest, selectNumber - 1); 
          const attached = permutations.map((el) => [fixed, ...el]); 
          results.push(...attached); 
        });

        return results; 
    }
    
    const operationsInExpression = [];
    operations.forEach((operation) => {
        if (expression.indexOf(operation) !== -1) {
            operationsInExpression.push(operation);
        }
    })
    const permutations = getPermutations(operationsInExpression, operationsInExpression.length);
    
    const regex = /[\*\+\-]/;
    const values = expression.split(regex);
    
    const operationRegex = /[0-9]+/;
    const eachOperation = expression.split(operationRegex).slice(1, -1);
    
    let maxValue = 0;
    permutations.forEach((permutation) => {
        let newValues = values;
        let newOperations = eachOperation;
        for (const operation of permutation) {
            let operationIndex = newOperations.indexOf(operation);
            let count = 1;
            while (operationIndex !== -1) {
                const updateValue = operators[operation](parseInt(newValues[operationIndex]), parseInt(newValues[operationIndex + 1]));
                newValues = newValues.slice(0, operationIndex).concat([updateValue], newValues.slice(operationIndex + 2));
                newOperations = newOperations.slice(0, operationIndex).concat(newOperations.slice(operationIndex + 1));
                operationIndex = newOperations.indexOf(operation); 
            }
        }
        maxValue = Math.max(maxValue, Math.abs(newValues[0]));
    })
    
    return maxValue;
}
