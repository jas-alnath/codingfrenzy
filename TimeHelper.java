public class TimeHelper {

    int seconds;

    public TimeHelper(int s){
        seconds = s;
    }

    public int inMinutes() {
        return seconds / 60;
        }

     public int inHours(){
        return seconds / 3600;
    }

    public String toString() {
        int hours = seconds / 3600;
        int minutes =  (seconds % 3600) / 60;
        int remainingSeconds = seconds % 60;
        return hours + (hours == 1 ? " hour " : " hours") + minutes + (minutes == 1 ? " minute " : " minutes ") + remainingSeconds + (remainingSeconds == 1 ? " second " : " seconds ");

    }




    }
