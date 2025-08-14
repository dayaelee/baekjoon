import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

                    public class Main {
                        public static void main(String[] args) throws IOException {
                            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
                            String str = br.readLine();

                            int n = Integer.parseInt(str);

                            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

                            for (int i = 0; i < n; i++) {
                                str = br.readLine();
                                StringTokenizer st = new StringTokenizer(str);
                                int check = Integer.parseInt(st.nextToken());
                                if (check == 0){
                                    if (pq.isEmpty()){
                                        System.out.println(-1);
                                    }else{
                                        System.out.println(pq.poll());
                                    }
                                }else{
                                    for (int j = 0; j < check; j++) {
                                        int v = Integer.parseInt(st.nextToken());
                                        pq.add(v);
                                    }
                                }


                            }

                        }
                    }

/*
*
*
*
*
* 5 = n
0
2 3 2
0
0
0
*
* */