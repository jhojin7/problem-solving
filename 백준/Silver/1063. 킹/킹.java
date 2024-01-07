import java.io.*;
import java.util.*;

public class Main {
    public static int[] move(String op, int x, int y){
        int nx=x;int ny=y;
        if (op.equals("R")) ny+=1;
        else if (op.equals("L")) ny-=1;
        else if (op.equals("B")) nx+=1;
        else if (op.equals("T")) nx-=1;
        else if (op.equals("RT")){ny+=1;nx-=1;}
        else if (op.equals("LT")){ny-=1;nx-=1;}
        else if (op.equals("RB")){ny+=1;nx+=1;}
        else if (op.equals("LB")){ny-=1;nx+=1;}
        // System.out.println(op+" "+nx+""+ny);
        if (!(0<=nx && nx<8 && 0<=ny && ny<8)){
            isOut = true;
            return new int[]{x,y};
        }
        return new int[]{nx,ny};
    }

    public static boolean isOut;
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // StringTokenizer st = new StringTokenizer(br.readLine());
        String[] tmp = br.readLine().split(" ");
        int kx = 7-(tmp[0].charAt(1)-'1');
        int rx = 7-(tmp[1].charAt(1)-'1');
        int ky = (tmp[0].charAt(0)-'A');
        int ry = (tmp[1].charAt(0)-'A');
        int N = Integer.parseInt(tmp[2]);
        // System.out.println(kx+""+ky);
        // System.out.println(rx+""+ry);
        for (int i=0;i<N;i++){
            isOut= false;
            String op = br.readLine();
            int[] knxy = move(op,kx,ky);
            if (isOut) continue;
            if (knxy[0]==rx && knxy[1]==ry){
                int[] rnxy = move(op,rx,ry);
                if (isOut) continue;
                rx = rnxy[0];
                ry = rnxy[1];
            }
            kx = knxy[0];
            ky = knxy[1];
        }

        // System.out.println(kx+""+ky);
        // System.out.println(rx+""+ry);
        System.out.println((char)(ky+'A')+""+(char)('1'-(kx-7)));
        System.out.println((char)(ry+'A')+""+(char)('1'-(rx-7)));

    }
}
    