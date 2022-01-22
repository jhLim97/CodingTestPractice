function solution(n, arr1, arr2) {
    const datas = Array.from(Array(n), () => Array(n).fill(0));
    
    const convert = (value) => {
        let result = value.toString(2);
        return result.padStart(n, '0');
    }
    
    const changeDatas = (arr) => {
        let index = 0
        for (const value of arr) {
            const convertedValue = convert(value);
            for (let i = 0; i < n; i+=1) {
                const _value = convertedValue[i];
                if (_value === '1') {
                    datas[index][i] = 1;
                }
            }
            index += 1;
        }
    }
    
    changeDatas(arr1);
    changeDatas(arr2);
    
    for (let i = 0; i < n; i+=1) {
        datas[i] = datas[i].join('');
        datas[i] = datas[i].replace(/1/g, '#');
        datas[i] = datas[i].replace(/0/g, ' ');
    }
    return datas;
}
