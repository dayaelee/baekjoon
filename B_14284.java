import java.io.*;
import java.util.*;

public class Main {
    public static int N, M, S, T;

    static class Node{
        int index;
        int cost;

        public Node(int index, int cost){
            this.index = index;
            this.cost = cost;
        }

        // @Override
        // public int compareTo(Node o){
        //     return Integer.compare(this.cost, o.cost);
        // }
    }

    public static boolean[] check;
    public static int[] dist; // 값 갱신
    public static int INF = Integer.MAX_VALUE;
    public static ArrayList<Node>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        check = new boolean[N+1];
        dist = new int[N+1];
        Arrays.fill(dist, INF);

        graph = new ArrayList[N+1];


        for(int i = 0; i<N+1; i++){
            graph[i] = new ArrayList<>();
        }


        for (int i = 0; i<M; i++){
            str = br.readLine();
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph[a].add(new Node(b, cost));
            graph[b].add(new Node(a, cost));
        }
        str = br.readLine();
        st = new StringTokenizer(str);
        S = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        dijkstra(S, T);

        System.out.println(dist[T]);

    }
    
    public static void dijkstra(int a, int b){

        dist[a]=0;

        PriorityQueue<Node> pq = new PriorityQueue<Node>
            ((o1, o2) -> Integer.compare(o1.cost, o2.cost));

        pq.offer(new Node(a, 0));
        while(!pq.isEmpty()){
            // System.out.println("????");
            Node node = pq.poll();
            int newNode = node.index;
            int newCost = node.cost;

            // System.out.println("???!!! newNode: "+ newNode + " newCost: " + newCost);
            if (check[newNode]){
                continue;
            }else{
                check[newNode]=true;
            }

            for (Node target: graph[newNode]){
                // System.out.println("??? index: "+ target.index + " cost: " + target.cost);
                if (target.cost+newCost<=dist[target.index]){
                    dist[target.index] = target.cost+newCost;
                    // System.out.println(Arrays.toString(dist));
                    pq.offer(new Node(target.index, dist[target.index]));
                }

            }
        }
    }
}
