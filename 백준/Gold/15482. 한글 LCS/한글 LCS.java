import java.io.*;
import java.util.*;

public class Main {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer st = new StringTokenizer(br.readLine());

        String s1 = br.readLine();
        String s2 = br.readLine();
        int N = s1.length();
        int M = s2.length();
        int[][] dp = new int[N+1][M+1];
        for (int i=1;i<=N;i++){
            for (int j=1;j<=M;j++){
                if (s1.charAt(i-1)==s2.charAt(j-1))
                    dp[i][j] = dp[i-1][j-1]+1;
                else
                    dp[i][j] = Math.max(dp[i][j-1],dp[i-1][j]);

            }
        }
        
        System.out.println(dp[N][M]);

    }
}
    