import java.io.*;
import java.util.*;
public class Main {
    //노드의 정보(노드 번호와 거리)를 쌍으로 저장할 클래스 생성
    private static class Node {
        int dest, cost;

        public Node(int dest, int cost){
            this.dest = dest;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException  {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        // 인접 리스트를 저장할 ArrayList 배열 초기화
        ArrayList<Node>[] adjList = new ArrayList[n+1];
        for(int i = 0; i < n+1; i++){
            adjList[i] = new ArrayList<>();
        }

        for(int i = 0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int time = Integer.parseInt(st.nextToken());
            adjList[start].add(new Node(end, time));
        }

        int[] dist = new int[n+1];
        // 모든 노드의 거리 값을 무한대로 초기화
        Arrays.fill(dist, Integer.MAX_VALUE);
        // 시작 노드의 거리 값은 0으로 초기화
        dist[x]=0;
        // 우선순위 큐를 생성하고 시작 노드를 삽입
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
        pq.add(new Node(x, 0));

        while (!pq.isEmpty()) {
            // 현재 가장 거리가 짧은 노드를 가져옴
            Node now = pq.poll();
            // 만약 현재 노드의 거리 값이 큐에서 가져온 거리 값보다 크면, 해당 노드는 이미 방문한 것이므로 무시
            if (dist[now.dest] < now.cost)
                continue;
            // 현재 노드와 인접한 노드들의 거리 값을 계산해서 업데이트
            for(Node next : adjList[now.dest]){
                // 기존에 발견했던 거리보다 더 짧은 거리를 발견하면 거리 값을 갱신하고 큐에 넣음
                if (dist[next.dest] > now.cost + next.cost) {
                    dist[next.dest] = now.cost + next.cost;
                    pq.add(new Node(next.dest, dist[next.dest]));
                }
            }
        }

        int[] distTotal = new int[n+1];
        int[] dist2 = new int[n + 1];
        for (int i = 1; i < n+1; i++) {
            if (i == x){
                continue;
            }

            // 모든 노드의 거리 값을 무한대로 초기화
            Arrays.fill(dist2, Integer.MAX_VALUE);

            dist2[i] = 0;
            // 우선순위 큐를 생성하고 시작 노드를 삽입
            PriorityQueue<Node> pq2 = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
            pq2.add(new Node(i, 0));

            while (!pq2.isEmpty()) {
                // 현재 가장 거리가 짧은 노드를 가져옴
                Node now = pq2.poll();

                // 만약 현재 노드의 거리 값이 큐에서 가져온 거리 값보다 크면, 해당 노드는 이미 방문한 것이므로 무시
                if (dist2[now.dest] < now.cost)
                    continue;

                // 현재 노드와 인접한 노드들의 거리 값을 계산해서 업데이트
                for (Node next : adjList[now.dest]) {
                    // 기존에 발견했던 거리보다 더 짧은 거리를 발견하면 거리 값을 갱신하고 큐에 넣음
                    if (dist2[next.dest] > now.cost + next.cost) {
                        dist2[next.dest] = now.cost + next.cost;
                        pq2.add(new Node(next.dest, dist2[next.dest]));
                    }
                }
            }
            distTotal[i]=dist[i]+dist2[x];
        }
        int max = distTotal[0];
        for(int i  = 1; i < n+1 ; i++){
            if (max<distTotal[i]){
                max = distTotal[i];
            }
        }
        System.out.println(max);
    }
}