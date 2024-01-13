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

        String[] sss = br.readLine().split(" ");
        int N = Integer.parseInt(sss[0]);
        int M = Integer.parseInt(sss[1]);
        int K = Integer.parseInt(sss[2]);
        int[][] arr = new int[N][M];

        for (int i=0;i<N;i++){
            String s = br.readLine();
            for (int j=0;j<M;j++){
                arr[i][j] = s.charAt(j)-'0';
            }
        }

        boolean solved = false;
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][][] vis = new boolean[N][M][K+1];
        int ans = N*M;
        q.add(new int[]{0,0,0,1});
        while(!q.isEmpty()){
            int[] xy = q.poll();
            int x = xy[0];
            int y = xy[1];
            int k = xy[2];
            int dist = xy[3];
            // System.out.println(Arrays.toString(new int[]{x,y,k,dist}));
            if (vis[x][y][k]) continue;
            vis[x][y][k] = true;
            if (x==N-1 && y==M-1){
                System.out.println(dist);
                return;
            }
            for (int d=0;d<4;d++){
                int nx = x+dx[d];
                int ny = y+dy[d];
                if (!(0<=nx && nx<N && 0<=ny && ny<M)) continue;
                if (!(0<=k && k<=K)) continue;
                // System.out.println(nx+""+ny+" "+arr[nx][ny]+" "+k);

                if (arr[nx][ny]==0 && !vis[nx][ny][k]){
                    q.add(new int[]{nx,ny,k,dist+1});
                }
                if (k+1<=K && arr[nx][ny]==1 && !vis[nx][ny][k+1]){
                    q.add(new int[]{nx,ny,k+1,dist+1});
                }
            }
        }
        if (!solved)
            System.out.println((-1));

    }
}