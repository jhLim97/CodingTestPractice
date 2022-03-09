function solution(cacheSize, cities) {
    let time = 0;
    let cache = [];
    
    if (cacheSize === 0) {
        return cities.length * 5;
    }
    
    cities = cities.map((city) => city.toLowerCase());
    
    cities.forEach((city) => {
        const index = cache.indexOf(city);
        if (index !== -1) {
            cache = [city].concat(cache.slice(0, index), cache.slice(index + 1));
            time += 1;
        } else {
            if (cache.length < cacheSize) {
                cache.unshift(city);
            } else {
                cache = [city].concat(cache.slice(0, -1));
            }
            time += 5;
        }
    });
    
    return time;
}
