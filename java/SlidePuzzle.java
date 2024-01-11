package java;

import javax.swing.*;


public class SlidePuzzle {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new SlideBoard());
    }
}