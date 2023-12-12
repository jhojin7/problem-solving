import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = 1000001;
        int[] dp = new int[M];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < M; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
            // System.out.println(dp[i]);
        }
        System.out.println(dp[N]);
    }
}