import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[][] dp = new long[100001][4];
        dp[1][1] = 1;
        dp[2][2] = 1;
        dp[3][1] = 1;
        dp[3][2] = 1;
        dp[3][3] = 1;

        int m = 1000000009;
        for (int i=4;i<100001;i++){
            if (i-1>=0) dp[i][1] = (dp[i-1][2]+dp[i-1][3])%m;
            if (i-2>=0) dp[i][2] = (dp[i-2][1]+dp[i-2][3])%m;
            if (i-3>=0) dp[i][3] = (dp[i-3][1]+dp[i-3][2])%m;
        }

        int T = Integer.parseInt(br.readLine());
        for (int t=0;t<T;t++){
            int n = Integer.parseInt(br.readLine());
            System.out.println((dp[n][1]+dp[n][2]+dp[n][3])%m);
        }
    }
}