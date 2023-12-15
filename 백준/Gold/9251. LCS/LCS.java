import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s1 = br.readLine();
        String s2 = br.readLine();
        int[][] dp = new int[1 + s1.length()][1 + s2.length()];
        for (int i = 1; i < 1 + s1.length(); i++) {
            for (int j = 1; j < 1 + s2.length(); j++) {
                char a = s1.charAt(i - 1);
                char b = s2.charAt(j - 1);
                if (a == b) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        System.out.println(dp[s1.length()][s2.length()]);
    }
}