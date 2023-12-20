import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split("-");
        int ans = 0;
        for (int i = 0; i < s.length; i++) {
            String ss = s[i];
            int tmp = 0;
            for (String num : ss.split("\\+")) {
                tmp += Integer.parseInt(num);
            }
            if (i == 0)
                ans += tmp;
            else
                ans -= tmp;
        }
        System.out.println(ans);
    }
}