package boj_23_0327;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class B_1941_이경원 {
    static char[][] map = new char[5][5];
    static int count = 1, countS = 0;
    static boolean[] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[] ty = new int [25];
    static int[] tx = new int [25];
    static int answer = 0;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            String line = sc.nextLine();
            for (int j = 0; j < 5; j++) {
                map[i][j] = line.charAt(j);
            }
        }

//        for (int i = 0; i < 5; i++) {
//        	for (int j = 0; j < 5; j++) {
//        		System.out.print(map[i][j]);
//        	}
//        	System.out.println();
//        }
//        
        
        
        for(int i = 0; i < 25; i++) { //좌표화
            tx[i] = i%5;
            ty[i] = i/5;
        }
     
         combination(7,0,0,new int[7]); //7명 저장 위한 배열
     
        
        System.out.println(answer);
    }


    private static void combination(int left,int start, int depth , int[] a) {
        // TODO Auto-generated method stub
        if(left == 0) { //선택 7개 했으면 bfs
            bfs(a);
            return;
        }
        if(depth == 25) return;
        
        a[start] = depth;
        combination(left-1,start+1, depth+1, a); //선택한 경우(선택했으니까 남은 left가 -1되고 start인덱스 하나 늘림)
        combination(left, start, depth+1, a); //선택안한경우 (선택 안했으니까 left그대로 두고 depth만 +1)
        
    }


    public static void bfs(int[]a) {
        Queue<Integer> q = new LinkedList<>();
        visited = new boolean[7];
        visited[0] = true;
        
        q.add(a[0]);
       while (!q.isEmpty()){
           int cur = q.poll(); //맨 처음 요소 삭제 및 반환
          
           if(map[ty[cur]][tx[cur]] == 'S') countS++; //S일때 증가

           for(int i=0; i<4; i++){ //상하좌우
               for(int j=1; j<7; j++){

                   if(!visited[j] && tx[cur]+dx[i] == tx[a[j]] && ty[cur]+ dy[i] == ty[a[j]]){ //방문하지 않았고 조건에 부합하면
                       visited[j] = true; //방문 처리
                       q.add(a[j]);
                       count++; //명수에 추가
                   }

               }
           }

       } //7개를 뽑았고 s가 4명 이상이라면 
       if(count == 7){
           if(countS >= 4){
        	   answer++; //정답증가
           }
       }
   }
}