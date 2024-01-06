import java.io.*;
import java.util.*;

public class Main {
    public static int[] dice;
    public static int top = 1;
    public static int east = 3;
    public static int x,y,N,M;
    public static int[] opposite = {-9999999,6,5,4,3,2,1};
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N][M];
        dice = new int[]{9999,0,0,0,0,0,0};
        for (int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<M;j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()){
            int dir = Integer.parseInt(st.nextToken());
            // System.out.println(top+" "+east+" "+dir);
            if (roll(dir)==-1) continue;
            if (arr[x][y]==0) arr[x][y] = dice[opposite[top]];
            else {
                dice[opposite[top]] = arr[x][y];
                arr[x][y] = 0;
            }
            System.out.println(dice[top]);
        }
    }

    public static int north(int top, int east) {
        String op = top + "" + east;
        if (op.equals("12")) return 4;
        if (op.equals("13")) return 2;
        if (op.equals("14")) return 5;
        if (op.equals("15")) return 3;
                      
        if (op.equals("21")) return 3;
        if (op.equals("23")) return 6;
        if (op.equals("24")) return 1;
        if (op.equals("26")) return 4;
                      
        if (op.equals("31")) return 5;
        if (op.equals("32")) return 1;
        if (op.equals("35")) return 6;
        if (op.equals("36")) return 2;
                      
        if (op.equals("41"))return 2;
        if (op.equals("42"))return 6;
        if (op.equals("45"))return 1;
        if (op.equals("46"))return 5;
                      
        if (op.equals("51"))return 4;
        if (op.equals("53"))return 1;
        if (op.equals("54"))return 6;
        if (op.equals("56"))return 3;
                      
        if (op.equals("62"))return 3;
        if (op.equals("63"))return 5;
        if (op.equals("64"))return 2;
        if (op.equals("65"))return 4;
        // System.out.println("haha"+op);
        return -9999;
    }

    public static int roll(int dir){
        // 1e 2w 3n 4s
        if (dir==1){
            if (y==M-1) return -1;
            y++;
            int tmp = top;
            top = opposite[east];
            east = tmp;
        }
        else if (dir==2){
            if (y==0) return -1;
            y--;
            int tmp = top;
            top = east;
            east = opposite[tmp];
        }
        else if (dir==3){
            if (x==0) return -1;
            x--;
            top = opposite[north(top,east)];
            // east = east;
        }
        else if (dir==4){
            if (x==N-1) return -1;
            x=x+1;
            top = north(top,east);
            // east = east;
        }
        return 0;
    }
}
