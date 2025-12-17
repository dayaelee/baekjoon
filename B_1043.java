import java.io.*;
import java.util.*;

public class Main {
    public static int N, M;
    public static int T;
    public static int[] arrayT;
    public static ArrayList<ArrayList<Integer>> party;
    public static boolean[] allT;

    public static int[] parent;
    public static int root;
    public static int answer;

    static int find(int x){
        if (parent[x] == x){
            return x; 
        }else{
            return parent[x] = find(parent[x]);
        }
    }

    static void union(int a, int b){ // b의 부모를 a의 부모에 종속시키는 거임 
        a = find(a);
        b = find(b);
        if (a!=b) parent[b] = a;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        str = br.readLine(); 
        st = new StringTokenizer(str); 

        parent = new int[N+1]; // 모든 사람들의 부모자리 초기화 
        for(int i = 1; i<=N; i++){
            parent[i] = i; 
        }

        arrayT = new int[N+1];
        allT = new boolean[N+1];

        T = Integer.parseInt(st.nextToken());
        if(T!=0){ // 진실 그룹
            for (int i = 0; i<T; i++){
                arrayT[i]=Integer.parseInt(st.nextToken());
                int value = arrayT[i];
                if (i == 0){
                    root = value;
                }else{
                    union(root, value);
                }
                allT[value] = true;
            }
        } 
        
        if (T==0){
            answer = M;
            for(int i = 0; i<M; i++){
                str = br.readLine();
                st = new StringTokenizer(str);
                
                int p = Integer.parseInt(st.nextToken());
                for (int j = 0; j<p; j++){
                    int value = Integer.parseInt(st.nextToken());
                }
            }
        }else{
            party = new ArrayList<>();

            for(int i = 0; i<M; i++){
                party.add(new ArrayList<>());
                
                str = br.readLine();
                st = new StringTokenizer(str);

                int p = Integer.parseInt(st.nextToken());
                int check = 0; // 진실한 자들과 같이 있는 사람인가? 
                for (int j = 0; j<p; j++){
                    int value = Integer.parseInt(st.nextToken());
                    party.get(i).add(value);
                    // tmp[j]=value;
                    if (check == 0){
                        if (root == find(value)){
                            check =1;
                        }
                    }
                }
                if (check == 1){ // 진실한 사람들과 같이 있는 사람들. 이사람들한테는 거짓말 못함 
                    for (int k : party.get(i)){
                        allT[k]=true;
                        union(root, k);
                    }

                    for(int l = 0; l<=i; l++){
                        for (int v : party.get(l)){
                            if (root == find(v)){
                                union(root, v);
                            }
                        }
                    }
                }
            }
        
        // 그냥 진실을 아는 사람이 속한 곳에서는 못하는거임 
        // 진실을 말해야만 하는 그룹에 속한 사람들한테도 구라못침 
        // => 1. 진실한 자들의 진실 유니온에서 1등이 루트고, 나머지 자들은 진실 유니온 루트 밑으로 묶는다. 
        // => 2. 진실한 사람들이 속한 파티에 진실한자 외에 나머지 사람들도 진실 그룹에 유니온으로 묶는다. 
        // =>    == 이사람들의 부모는 루트(진실 유니온 1등)
        
        // => 3. 모든 파티를 다시 순회하며 파티 구성원이 진실유니온에 속하는지 find로 확인. 

            for(int q = 0; q<M; q++){
                for(int l = 0; l<M; l++){
                    int check = 0;
                    for (int v : party.get(l)){
                        if (root == find(v)){
                            check =1;
                            union(root, v);
                        }
                    }
                    if (check == 1){ // 진실한 사람들과 같이 있는 사람들. 이사람들한테는 거짓말 못함 
                        for (int k : party.get(l)){
                            allT[k]=true;
                            union(root, k);
                        }
                    }
                }
            }

            answer = 0;
            for(int i = 0; i<M; i++){
                int check = 0; // 진실된 자가 있는지?
                for (int v : party.get(i)){
                    if (root == find(v)){
                        check =1;
                    }
                }
                if (check == 0){
                    answer+=1;
                }
            }
        }
        System.out.println(answer);
    }
}
