import java.util.*;
import java.io.*;

public class Main {
    public static Integer N;
    public static int[] parent;

    static int find(int x){
        if (x==parent[x]) return x;
        return parent[x]=find(parent[x]);
    }

    static void union(int a, int b){
        a = find(a);
        b = find(b);
        if (a==b) return;
        if (a>b){
            int t=a; a=b; b=t;
        }
        parent[b]=a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        
        N = Integer.parseInt(str);
        parent = new int[N+1];
        for(int i = 1; i<N+1; i++){
            parent[i]=i;
        }

        for (int i = 0; i<N-2; i++){
            str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            union(u, v);
        }

        if (N==2){
            System.out.println("1 2");
        }else{

            for(int i = 1; i<N+1;i++){
                parent[i]=find(parent[i]);
            }

            int a=parent[1];

            int check2 = -1;
            for(int i = 1; i<N+1; i++){
                if (parent[i]!=a){
                    check2 = parent[i];
                    break;
                }
            }

            System.out.println(a+ " "+check2);
        }
    }
}
