import java.util.*;
import java.io.*;
public class Main{
    static final long MOD = 1_000_000_007L;

    public static int N, M;
    public static int[] parent;
    public static int[] size;

    static int find(int x){
        if (parent[x]==x) return x;
        else return parent[x] = find(parent[x]);
    }

    static void union(int a, int b){
        a = find(a);
        b = find(b);
        if (a==b) return;
        if (size[a] < size[b]){ // 한쪽으로 몰기 위함 
            int t = a; a=b; b=t;
        }
        parent[b] = a;
        size[a] += size[b];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        parent = new int[N+1];
        size = new int[N+1];
        for(int i = 1; i<=N; i++){
            parent[i]=i;
            size[i]=1;
        }

        for(int i = 0; i<M; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            union(u, v);
        }

        long ans = 1L;
        for (int i = 1; i<=N; i++){
            if (find(i) == i) {
                ans = (ans * size[i]) % MOD;
            }
        }

        System.out.println(ans);
    }
}
