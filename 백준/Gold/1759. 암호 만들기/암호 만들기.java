import java.io.*;
import java.util.*;

public class Main {
    static void backtrack(int l, int idx, char[] chars, char[] ans) {
        if (idx == ans.length) {
            int vowelCnt = 0;
            for (int i = 0; i < ans.length; i++) {
                if ("aeiou".indexOf(ans[i]) != -1)
                    vowelCnt += 1;
            }
            // String s = Arrays.toString(ans);
            if (vowelCnt < 1
                    || ans.length - vowelCnt < 2) {
                return;
            }
            // String s = Arrays.toString(ans);
            String s = new String(ans);
            // System.out.println(ans.length - vowelCnt+ " "+ vowelCnt + " " + s);
            System.out.println(s);
            return;
        }

        for (int i = l; i < chars.length; i++) {
            ans[idx] = chars[i];
            backtrack(l + 1, idx + 1, chars, ans);
            l += 1;
        }
        return;
    }

    // [a, c, i, s, t, w]
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int L = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        char[] chars = new char[C];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            chars[i] = st.nextToken().toCharArray()[0];
        }
        Arrays.sort(chars);
        // System.out.println(Arrays.toString(chars));

        char[] ans = new char[L];
        Arrays.sort(chars);
        backtrack(0, 0, chars, ans);
    }

}