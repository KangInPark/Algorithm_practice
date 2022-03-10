import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(String[] lines) {
        int answer = -1;
        log[] l = new log[lines.length];
        List<Double> tlist = new ArrayList<>();
        for (int i = 0; i < lines.length; i++) {
            l[i] = new log(lines[i]);
            tlist.add(l[i].getStart());
            tlist.add(l[i].getEnd());
        }
        for (Double time : tlist) {
            int cnt = 0;
            for (log lg : l) {
                if ((lg.getStart() >= time && lg.getStart() < time + 1)
                        || (lg.getEnd() >= time && lg.getEnd() < time + 1) ||
                        (lg.getStart() < time && lg.getEnd() >= time + 1))
                    cnt += 1;
            }
            answer = answer >= cnt ? answer : cnt;
            cnt = 0;
            for (log lg : l) {
                if ((lg.getStart() > time - 1 && lg.getStart() <= time)
                        || (lg.getEnd() > time - 1 && lg.getEnd() <= time) ||
                        (lg.getStart() <= time - 1 && lg.getEnd() > time))
                    cnt += 1;
            }
            answer = answer >= cnt ? answer : cnt;
        }
        return answer;
    }

    public class log {
        private double start;
        private double end;

        public log(String s) {
            String[] line = s.split(" ");
            end = convert(line[1]);
            double interval = Double.parseDouble(line[2].substring(0, line[2].length() - 1));
            start = end - interval + 0.001;
        }

        public double getStart() {
            return start;
        }

        public double getEnd() {
            return end;
        }

        public double convert(String s) {
            String[] tmp = s.split(":");
            double ret = 0;
            ret += Double.parseDouble(tmp[0]) * 60 * 60;
            ret += Double.parseDouble(tmp[1]) * 60;
            ret += Double.parseDouble(tmp[2]);
            return ret;
        }
    }
}