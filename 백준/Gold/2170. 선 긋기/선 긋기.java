import java.util.*;
import java.io.*;

class Point {
    long x, y;

    Point(long x, long y) {
        this.x = x;
        this.y = y;
    }

}

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<Point> arr = new ArrayList<Point>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());
            arr.add(new Point(a, b));
        }
        arr.sort(new Comparator<Point>() {
            @Override
            public int compare(Point p1, Point p2) {
                if (p1.x > p2.x)
                    return 1;
                else if (p1.x == p2.x && p1.y > p2.y)
                    return 1;
                else
                    return -1;
            }
        });
        int dist = 0;
        Point ans = arr.get(0);
        for (Point p : arr) {
            if (ans.y < p.x) {
                dist += ans.y - ans.x;
                ans = p;
            } else {
                ans.y = Math.max(ans.y, p.y);
            }
        }
        dist += ans.y - ans.x;
        System.out.println(dist);
    }
}