import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class WordState {
    String word;
    int level;

    public WordState(String word, int level) {
        this.word = word;
        this.level = level;
    }
}

class Solution {
    public int solution(String begin, String target, String[] words) {
        boolean contain = Arrays.asList(words).contains(target);
        if (!contain) {
            return 0;
        }

        Queue<WordState> queue = new LinkedList<>();
        queue.offer(new WordState(begin, 0));
        while (!queue.isEmpty()) {
            WordState wordState = queue.poll();
            if (wordState.level >= words.length) {
                continue;
            }

            if (wordState.word.equals(target)) {
                return wordState.level;
            }
            
            for (String word : words) {
                int count = notMatchedCount(wordState.word, word);
                if (count == 1) {
                    queue.offer(new WordState(word, wordState.level + 1));
                }
            }

        }
        return 0;
    }

    private int notMatchedCount(String now, String word) {
        int count = 0;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) != now.charAt(i)) {
                count++;
            }
        }
        return count;
    }
}
