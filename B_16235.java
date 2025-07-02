import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {
    public static class Pair<y, x, age>{
        int y, x, age;
        Pair (int y, int x, int age){
            this.y = y;
            this.x = x;
            this.age = age;
        }
    }

    public static int[] dy = {-1, -1, -1, 0, 0, 1, 1, 1};
    public static int[] dx = {-1, 0, 1, -1, 1, -1, 0, 1};
    public static List<List<ArrayDeque<Integer>>> trees;
    public static int[][] plus;
    public static int[][] foodStatus;
    public static int n, m, k;
    public static ArrayList<Pair> dead;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringTokenizer st = new StringTokenizer(str);
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        plus = new int[n][n]; // 각 칸에 추가되는 양분
        foodStatus = new int[n][n]; // 양분 상태

        for (int i = 0; i < n; i++) {
            String str2 = br.readLine();
            st = new StringTokenizer(str2);
            for (int j = 0; j < n; j++) {
                plus[i][j] = Integer.parseInt(st.nextToken());
                foodStatus[i][j] = 5; // 초기 양분 초기화
            }
        }

        trees = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            trees.add(new ArrayList<>(n));
            for (int j = 0; j < n; j++) {
                trees.get(i).add(new ArrayDeque<>());
            }
        }

        for (int i = 0; i < m; i++) {
            String str3 = br.readLine();
            st = new StringTokenizer(str3);
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            trees.get(y-1).get(x-1).add(z);
        }

        for (int i = 0; i < k; i++) {
            spring();
            summer();
            fall();
            winter();
        }
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer+=trees.get(i).get(j).size();
            }
        }
        System.out.println(answer);
    }

    public static ArrayList<Pair> spring(){
        // 칸의 나무를 오름차순으로 정렬한다.
        // 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
        // 양분이 다 떨어져 자신의 나이만큼 양분을 먹지 못한 나무는 즉시 죽음
        // 죽은 나무 (y, x)값 리스트 반환.
        dead = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!trees.get(i).get(j).isEmpty()){
                    int repeat = trees.get(i).get(j).size();
                    for (int l = 0; l < repeat; l++) {
                        int age = trees.get(i).get(j).pollFirst();
                        if (foodStatus[i][j] - age >= 0) {
                            foodStatus[i][j] -= age; // 양분 먹기
                            trees.get(i).get(j).addLast(age + 1);
                        } else {
                            // 죽음
                            dead.add(new Pair(i, j, age));
                        }
                    }
                }
            }
        }
        return dead;
    }

    public static void summer() {
        // 죽은 양분이 있다면
        if (!dead.isEmpty()){
            for (int i = 0; i < dead.size(); i++) {
                int y = dead.get(i).y;
                int x = dead.get(i).x;
                int age = dead.get(i).age;
                foodStatus[y][x]+= age/2; // 강제 형변환
            }
        }
        dead.clear();
    }

    public static void fall(){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!trees.get(i).get(j).isEmpty()) {
                    for (int tmp : trees.get(i).get(j)) {
                        if (tmp % 5 == 0 && tmp > 0) {
                            for (int o = 0; o < 8; o++) {
                                // 인접한 8개의 칸에 나이가 1인 나무가 생김
                                int ny = i + dy[o];
                                int nx = j + dx[o];
                                if (0 <= ny && ny < n && 0 <= nx && nx < n) {
                                    trees.get(ny).get(nx).addFirst(1);
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    public static void winter(){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                foodStatus[i][j]+=plus[i][j];
            }
        }
    }
}