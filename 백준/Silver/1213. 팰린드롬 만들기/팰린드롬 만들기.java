import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] s = br.readLine().toCharArray();
        int[] arr = new int[26];
        for (int i = 0; i < s.length; i++) {
            arr[s[i] - 'A'] += 1;
        }
        int isOdd = 0;
        int oddI = 0;
        for (int i = 0; i < 26; i++) {
            if (arr[i] % 2 == 1) {
                isOdd += 1;
                oddI = i;
            }
        }
        if (isOdd > 1) {
            System.out.println("I'm Sorry Hansoo");
            return;
        } else {

            StringBuilder ans = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < arr[i] / 2; j++) {
                    ans.append((char) ('A' + i));
                }
            }
            if (isOdd == 1)
                System.out.println(ans.toString() + (char) ('A' + oddI) + ans.reverse().toString());
            else
                System.out.println(ans.toString() + ans.reverse().toString());
        }
    }
}
