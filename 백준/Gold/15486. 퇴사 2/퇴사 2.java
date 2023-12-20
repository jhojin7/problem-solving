import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] T = new int[N + 10];
        int[] P = new int[N + 10];
        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            int ti = Integer.parseInt(s[0]);
            int pi = Integer.parseInt(s[1]);
            T[i] = ti;
            P[i] = pi;
        }

        int[] dp = new int[N + 2];
        int curmax = 0;
        for (int i = 0; i < N + 2; i++) {
            curmax = Math.max(curmax, dp[i]);
            // System.out.println(Arrays.toString(arr[i]));
            if (i + T[i] > N + 1)
                continue;
            dp[i + T[i]] = Math.max(dp[i + T[i]], curmax + P[i]);
        }
        // Arrays.sort(dp);
        // System.out.println(Arrays.toString(dp));
        System.out.println(dp[N]);
    }
}