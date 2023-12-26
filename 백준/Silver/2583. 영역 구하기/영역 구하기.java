import java.io.*;
import java.util.*;

class P {
    int x;
    int y;
    P(int x, int y){
        this.x=x; this.y=y;
    }
}

public class Main {
    static int M,N,K;
    static int[][] box;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M=Integer.parseInt(st.nextToken());
        N=Integer.parseInt(st.nextToken());
        K=Integer.parseInt(st.nextToken());
        box = new int[N][M];
        for (int i=0;i<K;i++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            for (int x=x1;x<x2;x++){
                for (int y=y1;y<y2;y++){
                    box[x][y] = 1;
                }
            }
        }

        List<Integer> ans = new ArrayList<>();
        for (int x=0;x<N;x++){
            for (int y=0;y<M;y++){
                int tmp = bfs(x,y);
                if (tmp >0) ans.add(tmp);
            }
        }
        ans.sort(Comparator.naturalOrder());
        System.out.println(ans.size());
        for (Integer i:ans){
            System.out.print(i+" ");
        }
    }

    static int bfs(int x, int y){
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};
        Queue<P> q = new LinkedList<>();
        int cnt=0;
        q.offer(new P(x,y));
        while (!q.isEmpty()){
            P p = q.poll();
            if (box[p.x][p.y] == 1 || box[p.x][p.y] == -1)
                continue;
            box[p.x][p.y] = -1;
            cnt+=1;
            for (int i=0;i<4;i++){
                int nx=p.x+dx[i];
                int ny=p.y+dy[i];
                if (!((0<=nx && nx<N) && (0<=ny && ny<M)))
                    continue;
                if (box[nx][ny]==0)
                    q.offer(new P(nx,ny));
            }
        }
        return cnt;
    }
}