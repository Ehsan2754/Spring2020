package gametheory.assignment2.students2022;

import java.util.Random;
import gametheory.assignment2.Player;

public class EhsanShaghaeiTesting {
    private final static int MOVE = 100;
    private final static int MAX_VEG = 100 + 1;
    private final static String myEmail = "e.shaghaei@innopolis.university";
    private final static Random random = new Random();

    public static void main(String[] args) throws Exception {
        // Creating the plater instances
        System.out.println("### UNIT TEST STARTED ###");

        Player player = new EhsanShaghaeiCode();
        System.out.println(">CONSTRUCTOR TEST PASSED[NO EXCEPTION thrown]");

        test(isEmailCorrect(player.getEmail()), "INVALID EMAIL ADDRESS");
        System.out.println(">EMAIL ADDRESS TEST PASSED");
        
        test(isValidMove(player.move(0,
        random.nextInt(MAX_VEG),
        random.nextInt(MAX_VEG),
        random.nextInt(MAX_VEG))), "INVALID MOVE");
        for (int i = 1; i < MOVE; i++) {
            test(isValidMove(player.move(randomField(),
            random.nextInt(MAX_VEG),
            random.nextInt(MAX_VEG),
            random.nextInt(MAX_VEG))), "INVALID MOVE");
        }
        System.out.println(">MOVE TEST PASSED");

        player.reset();
        System.out.println(">NO EXCEPTION DURING PLAYER RESET TEST");

        System.out.println("$$$> UNIT TEST PASSED");
        
    }

    private static int randomField() {
        return random.nextInt(3) + 1;
    }

    // Evaluates a valid move
    private static boolean isValidMove(int x) {
        return x == 1 || x == 2 || x == 3;
    }

    // Evaluates if the given email is coorect
    private static boolean isEmailCorrect(String email) {
        return email == myEmail;
    }

    public static void test(boolean b, String message) throws Exception {
        if (!b) {
            throw new Exception(message);
        }
    }

}
