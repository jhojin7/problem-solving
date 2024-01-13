import java.io.*;
import java.util.*;

public class Main {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(br.readLine());
        String s = br.readLine().replace("long",".");
        N = s.length();

        int[] dp = new int[100];
        dp[0]=dp[1]=1;
        for (int i=2;i<100;i++)
            dp[i] = dp[i-1]+dp[i-2];

        int i=0;
        int ans=1;
        while (i<N){
            if (s.charAt(i)=='.'){
                List<Character> tmp = new ArrayList<>();
                while (i<N && s.charAt(i)=='.'){
                    tmp.add('.');
                    i++;
                }
                ans*=dp[tmp.size()];
            }
            i++;
        }
        System.out.println(ans);
    }
}