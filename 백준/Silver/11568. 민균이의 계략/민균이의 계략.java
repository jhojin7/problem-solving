import java.io.*;
import java.util.*;

public class Main {
    public static int[][] arr;
    public static boolean[][] graph;
    public static boolean[] vis;
    public static int N, M;
    public static int[] dx = new int[]{-1,0,1,0};
    public static int[] dy = new int[]{0,-1,0,1};


    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[1001];

        StringTokenizer st = new StringTokenizer(br.readLine());
        int i=0;
        while (st.hasMoreTokens())
            arr[i++] = Integer.parseInt(st.nextToken());
        // System.out.println(Arrays.toString(arr));

        int[] dp = new int[N+1];
        int ans = 0;
        for (int ii=0;ii<N;ii++){
            dp[ii] = 1;
            for (int j=0;j<ii;j++){
                if (arr[j]<arr[ii]){
                    dp[ii]=Math.max(dp[ii],dp[j]+1);
                }
            }
            ans = Math.max(ans, dp[ii]);
        }
        // System.out.println(Arrays.toString(dp));
        System.out.println(ans);
    }
}

