import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.*;

public class CodeQuality {
    public static List<Map<String, Object>> processUserData(List<Map<String, Object>> data) {
        List<Map<String, Object>> result = new ArrayList<>();
        for (Map<String, Object> d : data) {
            if ((boolean) d.getOrDefault("active", false)) {
                Map<String, Object> temp = new HashMap<>();
                temp.put("name", d.get("name"));
                temp.put("email", d.get("email"));
                temp.put("lastLogin", d.get("lastLogin"));
                temp.put("score", calculateScore(d));
                temp.put("status", determineStatus((String) d.get("lastLogin")));
                result.add(temp);
            }
        }
        return result;
    }

    public static double calculateScore(Map<String, Object> user) {
        int clicks = (int) user.getOrDefault("clicks", 0);
        int shares = (int) user.getOrDefault("shares", 0);
        return Math.round(((clicks * 2 + shares * 3) / 5.0) * 100.0) / 100.0;
    }

    public static String determineStatus(String lastLogin) {
        if (lastLogin == null || lastLogin.isEmpty()) return "unknown";
        LocalDate loginDate = LocalDate.parse(lastLogin);
        long daysInactive = ChronoUnit.DAYS.between(loginDate, LocalDate.now());
        return daysInactive > 30 ? "inactive" : "active";
    }
}
