import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int ans;
    static int[][] W;

    static void backtrack(int x, int[] vis, int dist, int cnt){
        if (cnt==N-1){
            if (W[x][0]==0) return;
            ans = Math.min(ans,dist+W[x][0]);
            return;
        }
        // System.out.println(x+" "+vis+" "+ dist+" "+ cnt);
        for (int i=1;i<N;i++){
            int d = W[x][i];
            if (d==0) continue;
            if (vis[i]==1) continue;
            vis[x] = 1;
            backtrack(i, vis, dist+d, cnt+1);
            vis[x] = 0;
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        W = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                W[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        ans = 99999999;
        backtrack(0,new int[N],0,0);
        System.out.println(ans);


    }
}
