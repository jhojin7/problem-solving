import java.io.*;
import java.util.*;

public class Main {
    static int M,N,K;
    static int[][] box;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int H = Integer.parseInt(s[0]);
        int Y = Integer.parseInt(s[1]);
        int[] dp = new int[100];
        dp[0] = H;
        for (int i=1;i<100;i+=1){
            dp[i] = (int)Math.max(dp[i-1]*1.05,dp[i]);
            if (i>=3) dp[i] = (int)Math.max(dp[i-3]*1.2,dp[i]);
            if (i>=5) dp[i] = (int)Math.max(dp[i-5]*1.35,dp[i]);
        }
        System.out.println(dp[Y]);
    }
}
        