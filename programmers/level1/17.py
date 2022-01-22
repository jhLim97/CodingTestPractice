function solution(id_list, report, k) {
    const ids = {};
    for (const id of id_list) {
        ids[id] = { targeted: new Set(), exited: [] };
    }

    for (const _report of report) {
        const [id, target] = _report.split(' ');
        ids[target].targeted.add(id);
    }

    for (const id in ids) {
        const targetedList = ids[id].targeted;
        if (targetedList.size >= k) {
            for (const _id of [...targetedList]) {
                ids[_id].exited.push(id);
            }
        }
    }

    const result = [];
    for (const id in ids) {
        const exitedList = ids[id].exited;
        result.push(exitedList.length);
    }
    return result;
}
