import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int k = Integer.parseInt(s[1]);
        int[] coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(coins);

        int[] dp = new int[100001];
        for (int i = 1; i < 100001; i++) {
            dp[i] = 100001;
        }
        // System.out.println(Arrays.toString(dp));
        for (int i = 0; i <= k; i++) {
            // System.out.println(i+" "+dp[i]);
            for (int j = 0; j < n; j++) {
                // System.out.println(i+coins[j]+" "+dp[coins[1]]+" "+dp[coins[j]]);
                dp[i + coins[j]] = Math.min(dp[i + coins[j]], dp[i] + 1);
            }
        }
        // System.out.println(Arrays.toString(dp));
        if (dp[k] == 100001)
            System.out.println(-1);
        else
            System.out.println(dp[k]);
    }
}
