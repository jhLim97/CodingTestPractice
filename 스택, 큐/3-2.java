import java.util.LinkedList;
import java.util.Queue;

class Priority {
    int priority;
    int index;

    public Priority(int priority, int index) {
        this.priority = priority;
        this.index = index;
    }

    public int getPriority() {
        return priority;
    }

    public int getIndex() {
        return index;
    }

    public boolean isBiggest(Queue<Priority> queue) {
        for (Priority p_ : queue) {
            if (p_.getPriority() > this.priority) {
                return false;
            }
        }
        return true;
    }

    public boolean isCoincide(int location) {
        return location == index;
    }
}

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;

        Queue<Priority> queue = new LinkedList<>();
        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new Priority(priorities[i], i));
        }

        int turn = 1;
        while (!queue.isEmpty()) {
            Priority priority = queue.poll();
            if (!priority.isBiggest(queue)) {
                queue.offer(priority);
                continue;
            }
            if (priority.isCoincide(location)) {
                return turn;
            }
            turn++;
        }

        return answer;
    }
}
