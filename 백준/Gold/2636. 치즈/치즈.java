import java.io.*;
import java.util.*;

public class Main {
    public static int[][] arr;
    public static int N, M;
    public static int bfs(int i, int j){
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] vis = new boolean[N][M];
        int[] dx = new int[]{-1,0,1,0};
        int[] dy = new int[]{0,-1,0,1};
        q.add(new int[]{i,j});
        while (!q.isEmpty()){
            int[] xy = q.poll();
            int x = xy[0];
            int y = xy[1];
            if (vis[x][y]) continue;
            vis[x][y] = true;
            for (int d=0;d<4;d++){
                int nx = x+dx[d];
                int ny = y+dy[d];
                if (nx==0 || ny==0) return -1; // c
                if (!(0<=nx && nx<N && 0<=ny && ny<M)) continue;
                if (arr[nx][ny]==0)
                    q.add(new int[]{nx,ny});
            }
        }
        return 0;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] s = br.readLine().split(" ");
        N = Integer.parseInt(s[0]);
        M = Integer.parseInt(s[1]);
        arr = new int[N][M];
        for (int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0;j<M;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int h = 0;
        int[] cc = new int[50];
        while (true){
            int c=0;
            for (int i=0;i<N;i++){
                for (int j=0;j<M;j++){
                    if (arr[i][j]==1){
                        int ret = bfs(i,j);
                        if (ret==-1){
                            c++;
                            arr[i][j] = -1;
                        }
                    }
                }
            }
            // System.out.println(h+" "+c);
            boolean isEmpty = true;
            for (int i=0;i<N;i++){
                for (int j=0;j<M;j++){
                    if (arr[i][j]==-1)
                        arr[i][j] = 0;
                    if (arr[i][j]==1)
                        isEmpty = false;
                }
            }
            cc[h] = c;
            h++;
            if (isEmpty) break;
        }
        System.out.println(h);
        System.out.println(cc[h-1]);


        
    }
}