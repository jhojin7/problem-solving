import java.io.*;
import java.util.*;

public class Main {
    public static int[][] arr;
    public static int N, M;
    public static int[] dx = new int[]{-1,0,1,0};
    public static int[] dy = new int[]{0,-1,0,1};

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String s1 = br.readLine();
        String s2 = br.readLine();
        int N = s1.length();
        int M = s2.length();
        int[][] dp = new int[N+1][M+1];
        int ans = 0;

        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                if (s1.charAt(i)==s2.charAt(j)){
                    if (i==0 || j==0)
                        dp[i][j] = 1;
                    else 
                        dp[i][j] = dp[i-1][j-1]+1;
                }
                ans = Math.max(ans, dp[i][j]);
            }
        }
        // for(int i=0;i<N;i++)
        //     System.out.println(Arrays.toString(dp[i]));
        System.out.println(ans);
    }
}