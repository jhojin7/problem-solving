import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        int N = Integer.parseInt(str[0]);
        int M = Integer.parseInt(str[1]);


        char[][] esm = new char[N][M];
        for (int i = 0; i < N; i++) {
            char[] tmp = br.readLine().toCharArray();
            for (int j = 0; j < M; j++) {
                esm[i][j] = tmp[j];
            }
        }

        // e0 s1 m2
        long mod = (long)Math.pow(10,9)+7;
        long[][][] dp = new long[N + 1][M + 1][3];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= M; j++) {
                dp[i][j][0] = (dp[i-1][j][0] - dp[i-1][j-1][0]+mod)%mod + dp[i][j-1][0];
                dp[i][j][0] %= mod;
                if (esm[i - 1][j - 1] == 'E')
                    dp[i][j][0]++;
                dp[i][j][0] %= mod;

                dp[i][j][1] = (dp[i-1][j][1] - dp[i-1][j-1][1]+mod)%mod + dp[i][j-1][1];
                dp[i][j][1] %= mod;
                if (esm[i - 1][j - 1] == 'S')
                    dp[i][j][1] += dp[i][j][0];
                dp[i][j][1] %= mod;

                dp[i][j][2] = (dp[i-1][j][2] - dp[i-1][j-1][2]+mod)%mod + dp[i][j-1][2];
                dp[i][j][2] %= mod;
                if (esm[i - 1][j - 1] == 'M')
                    dp[i][j][2] += dp[i][j][1];
                dp[i][j][2] %= mod;
            }
        }

        System.out.println((dp[N][M][2]) % mod);
    }
}