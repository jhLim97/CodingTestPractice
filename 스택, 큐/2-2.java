import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Progress {
    int progress;
    int speeds;

    public Progress(int progress, int speed) {
        this.progress = progress;
        this.speeds = speed;
    }

    public boolean isFinish(int day) {
        return 100 <= progress + day * speeds;
    }
}

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();

        Queue<Progress> queue = new LinkedList<>();
        for (int i = 0; i < progresses.length; i++) {
            queue.add(new Progress(progresses[i], speeds[i]));
        }

        int day = 1;
        int count = 0;
        while (!queue.isEmpty()) {
            Progress progress = queue.peek();
            if (progress.isFinish(day)) {
                queue.poll();
                count++;
                continue;
            }
            if (count >= 1) {
                answer.add(count);
                count = 0;
            }
            day++;
        }
        if (count != 0) {
            answer.add(count);
        }
        return answer;
    }
}
