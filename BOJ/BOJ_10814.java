import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class BOJ_10814 {
    public static class Member implements Comparable<Member> {
        private int x;
        private String y;
        private int z;

        Member(int x, String y, int z){
            this.x = x;
            this.y = y;
            this.z = z;
        }
        public int getx(){
            return x;
        }
        public String gety(){
            return y;
        }
        public int getz(){
            return z;
        }

        @Override
        public int compareTo(Member m) {
            if(this.x < m.getx()){
                return -1;
            }
            else if(this.x > m.getx()){
                return 1;
            }
            else{
                if(this.z < m.getz()){
                    return -1;
                }
                else if(this.z > m.getz()){
                    return 1;
                }
                else return 0;
            }
        }
    }
    public static void main(String[] args) throws NumberFormatException, IOException {
        ArrayList<Member> list = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        Member m = null;
        StringTokenizer st = null;
        int x, z;
        String y;
        for(int i = 0 ; i < n ; i++ ){
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = st.nextToken();
            z = i;
            m = new Member(x, y, z);
            list.add(m);
        }
        Collections.sort(list);
        for (Member member : list) {
            String s = Integer.toString(member.getx()) + " " + member.gety();
            bw.write(s + '\n');     
        }
        bw.flush();
        bw.close();
    }
}