function solution(a, b) {
    const days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'];
    const dayInMonth = {
        1: 0,
        2: 31,
        3: 60,
        4: 91,
        5: 121,
        6: 152,
        7: 182,
        8: 213,
        9: 244,
        10: 274,
        11: 305,
        12: 335,
    }
    const countFromStart = dayInMonth[a] + b;
    const remain = (countFromStart - 1) % 7;
    
    return days[remain];
}
