package gametheory.assignment2.students2022;

import java.util.Random;

import gametheory.assignment2.Player;

public class Strat implements Player {    private final String myEmail = "e.shaghaei@innopolis.university";
private Random random = new Random();
private int A = 1;
private int B = 2;
private int C = 3;
private int myLastMove=0;

/**
 * This method is called to reset the agent before the match
 * with another player containing several rounds
 */
@Override
public void reset() {
    this.random = new Random();
    myLastMove =0;
}

/**
 * This method returns the move of the player based on
 * the last move of the opponent and X values of all fields.
 * Initially, X for all fields is equal to 1 and last opponent
 * move is equal to 0
 *
 * @param opponentLastMove the last move of the opponent
 *                         varies from 0 to 3
 *                         (0 – if this is the first move)
 * @param xA               the argument X for a field A
 * @param xB               the argument X for a field B
 * @param xC               the argument X for a field C
 * @return the move of the player can be 1 for A, 2 for B
 * and 3 for C fields
 */
@Override
public int move(int opponentLastMove, int xA, int xB, int xC) {
    return this.randomAgentMove(opponentLastMove, xA, xB, xC);
}

// Random Agent Move
// * Does not utilize history of opponent/its' previous moves
// * Resets it's random system every round
// * At every request for move, it randomly chooses a field for movement.
// Score in https://moosegame.in.shadowy.space/ -> 131.184
public int randomAgentMove(int opponentLastMove, int xA, int xB, int xC) {
    return this.random.nextInt(3) + 1;
}

// Greedy Agent Move
// * Does not utilize history of opponent/its' previous moves
// * Resets it's random system every round
// * At every request for move, it chooses the field with maximum vegetation.
// Score in https://moosegame.in.shadowy.space/ -> 132.937
public int greedyAgentMove(int opponentLastMove, int xA, int xB, int xC) {
    int move = this.A;
    if (xA >= xB && xA >= xB) {
        // Here you determine that A has largest payoff than other feilds
        move = this.A;
    } else if (xB >= xA && xB >= xC) {
        // Here you determine that B has largest payoff than other feilds
        move = this.B;
    } else if (xC >= xB && xC >= xA) {
        // Here you determine that C has largest payoff than other feilds
        move = this.C;
    }
    return move;
}

// Copy-Cat Agent Move
// * Utilizes opponent previous move
// * Resets it's random system every round
// * Starts with a random move; And at every request for move,
// it chooses the opponents previous move if that move doesn't
// have zero vegetation.If the last move of the opponent has
// zero vegetation, It acts as a random agent for that particular move.
// Score in https://moosegame.in.shadowy.space/ -> 148.883
public int copyCatAgentMove(int opponentLastMove, int xA, int xB, int xC) {
    int move = opponentLastMove;
    // Initial random move
    if (opponentLastMove == 0) {
        move = randomAgentMove(opponentLastMove, xA, xB, xC);
    } else if (opponentLastMove == this.A) {
        // Checking if the opponent last move doesn't have zero payoff and then
        // copycapting for A
        if (xA == 0) {
            move = randomAgentMove(opponentLastMove, xA, xB, xC);
        } else {
            move = opponentLastMove;
        }
    } else if (opponentLastMove == this.B) {
        // Checking if the opponent last move doesn't have zero payoff and then
        // copycapting for B
        if (xB == 0) {
            move = randomAgentMove(opponentLastMove, xA, xB, xC);
        } else {
            move = opponentLastMove;
        }
    } else if (opponentLastMove == this.C) {
        // Checking if the opponent last move doesn't have zero payoff and then
        // copycapting for C
        if (xC == 0) {
            move = randomAgentMove(opponentLastMove, xA, xB, xC);
        } else {
            move = opponentLastMove;
        }
    }
    return move;
}

// GreedyCopycat Agent Move
// * Utilizes opponent previous move
// * Resets it's random system every round
// * Starts with a random move; at every request for move,
// it chooses the opponents previous move if that move
// doesn't have zero vegetation. If the last move of the
// opponent has zero vegetation, It acts as a greedy agent
// for that particular move.
// Score in https://moosegame.in.shadowy.space/ -> 149.773
public int greedyCopycatAgentMove(int opponentLastMove, int xA, int xB, int xC) {
    int move = opponentLastMove;
    // Initial random move
    if (opponentLastMove == 0) {
        move = randomAgentMove(opponentLastMove, xA, xB, xC);
    } else if (opponentLastMove == this.A) {
        // Checking if the opponent last move doesn't have zero payoff and then
        // copycapting for A otherwise greeding!
        if (xA == 0) {
            move = greedyAgentMove(opponentLastMove, xA, xB, xC);
        } else {
            move = opponentLastMove;
        }
    } else if (opponentLastMove == this.B) {
        // Checking if the opponent last move doesn't have zero payoff and then
        // copycapting for B otherwise greeding!
        if (xB == 0) {
            move = greedyAgentMove(opponentLastMove, xA, xB, xC);
        } else {
            move = opponentLastMove;
        }
    } else if (opponentLastMove == this.C) {
        // Checking if the opponent last move doesn't have zero payoff and then
        // copycapting for C otherwise greeding!
        if (xC == 0) {
            move = greedyAgentMove(opponentLastMove, xA, xB, xC);
        } else {
            move = opponentLastMove;
        }
    }
    return move;

}


/**
 * This method returns your IU email
 *
 * @return your email
 */
@Override
public String getEmail() {
    return this.myEmail;
}

}