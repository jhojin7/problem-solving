import java.io.*;
import java.util.*;

public class Main {
    static int M,N,K;
    static int[][] box;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        if ((N%7==1) || (N%7==3))
            System.out.println("CY");
        else 
            System.out.println("SK");
        // int[] dp = new int[N+10];
        // // SK=0, CY=1
        // for(int i=0;i<=N;i++){
        //     if (dp[i]==0){
        //         dp[i+1] = 1;
        //         if (i+3<=N) dp[i+3] = 1;
        //         if (i+4<=N) dp[i+4] = 1;
        //     }
        //     else if (dp[i]==1){
        //         dp[i+1] = 0;
        //         if (i+3<=N) dp[i+3] = 0;
        //         if (i+4<=N) dp[i+4] = 0;
        //     }
        // }
        // if (dp[N-1]==0) System.out.println("CY");
        // else System.out.println("SK");
        // // System.out.println(Arrays.toString(dp));
    }
}