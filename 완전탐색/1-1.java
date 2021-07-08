import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Integer> solution(int[] answers) {
        int[] answer = {0, 0, 0};

        int[] method1 = {1, 2, 3, 4, 5};
        int[] method2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] method3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == method1[i % method1.length]) {
                answer[0] += 1;
            }
            if (answers[i] == method2[i % method2.length]) {
                answer[1] += 1;
            }
            if (answers[i] == method3[i % method3.length]) {
                answer[2] += 1;
            }
        }

        int max = Arrays.stream(answer)
                .max()
                .getAsInt();

        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < answer.length; i++) {
            if (answer[i] == max) {
                list.add(i + 1);
            }
        }
        return list;
    }
}
