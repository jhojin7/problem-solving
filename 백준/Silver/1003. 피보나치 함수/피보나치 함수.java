import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(br.readLine());
        int[][] dp = new int[100000][2];
        dp[0][0] = 1;
        dp[0][1] = 0;
        dp[1][0] = 0;
        dp[1][1] = 1;
        dp[2][0] = 1;
        dp[2][1] = 1;
        for (int i = 3; i < 10000; i++) {
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0];
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1];
        }
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            System.out.print(dp[N][0]);
            System.out.print(' ');
            System.out.print(dp[N][1]);
            System.out.println();
        }
    }
}
