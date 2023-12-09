import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        ArrayList<String> arr = new ArrayList<String>();
        String l;
        while ((l = br.readLine()) != null) {
            arr.add(l);
        }

        String ans = "";
        int ansham = 0;
        for (int j = 0; j < M; j++) {
            int[] acgt = new int[] { 0, 0, 0, 0 };
            for (int i = 0; i < N; i++) {
                char x = arr.get(i).charAt(j);
                // System.out.println(x);
                switch (x) {
                    case 'A':
                        acgt[0] += 1;
                        break;
                    case 'C':
                        acgt[1] += 1;
                        break;
                    case 'G':
                        acgt[2] += 1;
                        break;
                    case 'T':
                        acgt[3] += 1;
                        break;
                    default:
                        break;
                }
            }

            // System.out.println(Arrays.toString(acgt));
            int max_ = 0;
            int mi = 0;
            for (int i = 0; i < 4; i++) {
                if (acgt[i] > max_) {
                    max_ = acgt[i];
                    mi = i;
                }
            }
            // System.out.println(N-max_);
            ansham += N - max_;
            // System.out.println("ACGT".charAt(mi));
            ans += "ACGT".charAt(mi);
        }

        int[] acgt = new int[] { 0, 0, 0, 0 };
        for (int i = 0; i < M; i++) {
            char x = ans.charAt(i);
            switch (x) {
                case 'A':
                    acgt[0] += 1;
                    break;
                case 'C':
                    acgt[1] += 1;
                    break;
                case 'G':
                    acgt[2] += 1;
                    break;
                case 'T':
                    acgt[3] += 1;
                    break;
                default:
                    break;
            }
        }
        System.out.println(ans);
        System.out.println(ansham);
    }
}