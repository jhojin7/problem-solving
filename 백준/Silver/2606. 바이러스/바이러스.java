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
        int M = Integer.parseInt(br.readLine());
        graph = new boolean[N+1][N+1];
        vis = new boolean[N+1];
        for (int i=0;i<M;i++){
            String[] s = br.readLine().split(" ");
            int a = Integer.parseInt(s[0]);
            int b = Integer.parseInt(s[1]);
            graph[a][b] = true;
            graph[b][a] = true;
        }

        int ans =-1;
        Queue<Integer> q = new ArrayDeque<>();
        q.add(1);
        while (!q.isEmpty()){
            int x = q.poll();
            if (vis[x]) continue;
            vis[x] = true;
            ans +=1;
            for (int y=1;y<=N;y++){
                if (graph[x][y]) q.add(y);
            }
        }
        System.out.println(ans);

    }
}