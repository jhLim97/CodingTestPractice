import java.util.Stack;

class Solution {
    public String solution(String p) {
        if (p.isEmpty()) {
            return p;
        }
        String[] strings = splitTwo(p);
        assert strings != null;
        if (isCorrect(strings[0])) {
            return strings[0] + solution(strings[1]);
        } else {
            return '(' + solution(strings[1]) + ')' + reverse(strings[0]);
        }
    }

    private String reverse(String s) {
        String temp = s.substring(1, s.length() - 1);
        temp = temp.replace('(', '*');
        temp = temp.replace(')', '(');
        temp = temp.replace('*', ')');
        return temp;
    }

    private String[] splitTwo(String p) {
        int left = 0;
        int right = 0;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                return new String[]{p.substring(0, i + 1), p.substring(i + 1)};
            }
        }
        return null;
    }

    private boolean isCorrect(String s) {
        if (s.isEmpty()) {
            return true;
        }
        Stack<Character> stack = new Stack<>();
        stack.push(s.charAt(0));
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push('(');
                continue;
            }
            if (stack.isEmpty()) {
                return false;
            }
            Character lastInput = stack.pop();
            if (lastInput == ')') {
                return false;
            }
        }
        return stack.isEmpty();
    }
}
