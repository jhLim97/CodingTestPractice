import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        Arrays.sort(numbers);
        List<Integer> numberList = new ArrayList<>();
        for (int number : numbers) {
            numberList.add(number);
        }

        numberList.sort((a, b) -> {
            String left = String.valueOf(a);
            String right = String.valueOf(b);
            return -Integer.compare(Integer.parseInt(left + right), Integer.parseInt(right + left));
        });

        StringBuilder stringBuilder = new StringBuilder();
        for (Integer number : numberList) {
            stringBuilder.append(number);
        }
        answer = stringBuilder.toString();
        if(answer.charAt(0) == '0') {
            return "0";
        }
        return answer;
    }
}
