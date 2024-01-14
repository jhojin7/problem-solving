import java.io.*;
import java.util.*;

public class Main {
    public static int[][] arr;
    public static boolean[][] graph;
    public static boolean[][] vis;
    public static int N, M;
    public static int[] dx = new int[]{-1,0,1,0};
    public static int[] dy = new int[]{0,-1,0,1};

    public static int bfs(int i, int j){
        Queue<int[]> q = new ArrayDeque<>();
        vis = new boolean[N][M];
        q.add(new int[]{i,j,0});
        int maxdist = 0;
        while (!q.isEmpty()){
            int[] xy = q.poll();
            int x = xy[0];
            int y = xy[1];
            int dist = xy[2];
            if (vis[x][y]) continue;
            vis[x][y] = true;
            maxdist = Math.max(maxdist,dist);
            for (int d=0;d<4;d++){
                int nx = x+dx[d];
                int ny = y+dy[d];
                if (!(0<=nx && nx<N && 0<=ny && ny<M)) continue;
                if (arr[nx][ny]==0) continue;
                q.add(new int[]{nx,ny,dist+1});
            }
        }
        return maxdist;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);
        arr = new int[N][M];
        for (int i=0;i<N;i++){
            String ss = br.readLine();
            for (int j=0;j<M;j++){
                arr[i][j] = ss.charAt(j)=='W'?0:1;
            }
        }
        // for (int i=0;i<N;i++) System.out.println(Arrays.toString(arr[i]));

        int ans = 0;
        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                if (arr[i][j]==0) continue;
                ans = Math.max(ans,bfs(i,j));
            }
        }
        System.out.println(ans);

    }
}