import java.io.*;
import java.util.*;

public class Main {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer st = new StringTokenizer(br.readLine());
        char[][] map = new char[200][200];
        int N = Integer.parseInt(br.readLine());
        String op = br.readLine();
        int x=100; int y=100;
        int[] dx = {-1,0,1,0};
        int[] dy = {0,-1,0,1};
        int d = 2;
        for (int i=0;i<N;i++){
            char c = op.charAt(i);
            map[x][y] = '.';
            if (c=='F') {
                x=x+dx[d];
                y=y+dy[d];
            }
            else if (c=='R') d=(d-1+4)%4;
            else if (c=='L') d=(d+1+4)%4;
            map[x][y] = '.';
            // System.out.println(c+" "+x+""+y+""+d+""+map[x][y]);
        }
        int ax,bx,ay,by;
        ax=ay=1000;
        bx=by=0;
        for (int i=0;i<200;i++){
            for (int j=0;j<200;j++){
                if (map[i][j]=='.'){
                    ax=Math.min(ax,i);
                    bx=Math.max(bx,i);
                    ay=Math.min(ay,j);
                    by=Math.max(by,j);
                }
            }
        }
        for (int i=ax;i<=bx;i++){
            for (int j=ay;j<=by;j++){
                if (map[i][j]=='.')
                    System.out.print(map[i][j]);
                else
                    System.out.print('#');
            }
            System.out.println();
        }
    }
}