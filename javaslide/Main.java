package javaslide;

import javax.swing.*;


public class Main {
    public static void main(String[] args) {
        SlidePuzzle puzzle = new SlidePuzzle();
        SwingUtilities.invokeLater(puzzle);
    }
}