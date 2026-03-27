import java.io.*;
import java.util.*;

public class Main {

    static class Node{
        int y, x;
        Node(int y, int x){
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws IOException  {
        // 이 부분을 추가하면 콘솔 입력 대신 input.txt 파일을 읽습니다.
        // 제출할 때는 이 줄만 주석 처리하거나 지우면 됩니다!
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        str = br.readLine();
        st = new StringTokenizer(str);

        int k = Integer.parseInt(st.nextToken());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        char[][] cArr = new char[n][m];
        int[][] nArr = new int[n][m];


        for(int i = 0; i<n; i++){
            str = br.readLine();
            for(int j = 0; j<m; j++){
                cArr[i][j]=str.charAt(j);
            }
        }

        //----------------여기까지가 입력
        // 구간합 만들기 
        while(t-- >0){

            // 구간합 만들기
            int[][] s = new int[n+1][m+1];
            for(int i = 1; i<=n; i++){
                for(int j = 1; j<=m; j++){
                    int val;
                    if (cArr[i-1][j-1]=='*') val=1;
                    else val=0;
                    s[i][j]=-s[i-1][j-1]+ s[i][j-1]+ s[i-1][j]+val;
                }
            }

            // nArr 생성 
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int r1= i-k, r2=i+k;
                    int c1= j-k, c2=j+k;

                    if(r1<0) r1 = 0;
                    if(r2>=n) r2=n-1;
                    if(c1<0) c1 = 0;
                    if(c2>=m) c2=m-1;

                    int cnt = s[r2+1][c2+1] -s[r1][c2+1]-s[r2+1][c1]+s[r1][c1];
                    if(cArr[i][j]=='*') cnt--;

                    nArr[i][j]=cnt;
                }
            }


        
            // 조건체크해서 다음에 어떻게 할건지 정해주기 
            ArrayList<Node> stay = new ArrayList<>();
            ArrayList<Node> kill = new ArrayList<>();
            ArrayList<Node> birth = new ArrayList<>();

            for(int i = 0; i<n; i++){
                for(int j = 0; j<m; j++){
                    if(cArr[i][j]=='*'){
                        if(nArr[i][j]>=a && nArr[i][j]<=b){
                            // 살아남음 
                            stay.add(new Node(i, j));
                        } else if(nArr[i][j]<a || nArr[i][j]>b){
                            // 죽음 
                            kill.add(new Node(i, j));
                        } 
                    } else{
                        if(nArr[i][j]>a && nArr[i][j]<=b){
                            // 생명 탄생 
                            birth.add(new Node(i, j));
                        }
                    }
                }
            }

            // 갱신 

            char[][] nextCArr = new char[n][m];
            for(int i = 0; i<n; i++){
                Arrays.fill(nextCArr[i], '.');
            }

            // 살아남음

            for(int i=0; i<stay.size(); i++){
                Node node =stay.get(i);
                int y = node.y;
                int x = node.x;
                nextCArr[y][x]='*';
            }

            // 죽음
            for(int i=0; i<kill.size(); i++){
                Node node =kill.get(i);
                int y = node.y;
                int x = node.x;
                nextCArr[y][x]='.';
            }

            //생명 탄생

            for(int i=0; i<birth.size(); i++){
                Node node =birth.get(i);
                int y = node.y;
                int x = node.x;
                nextCArr[y][x]='*';
            }

            cArr= nextCArr;

        }

        for(int i = 0; i<n; i++){
            // bw.write(cArr[i]+"\n");
            System.out.println((cArr[i]));
        }

        // bw.flush();
        // bw.close();


        // T번 반복 
        

        // for(int i = 0; i<n; i++){
        //     System.out.println((cArr[i]));
        // }
    
        
        
    }
}
    

