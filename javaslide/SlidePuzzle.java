package javaslide;

import java.awt.BorderLayout;

import javax.swing.*;

public class SlidePuzzle implements Runnable {

    @Override
    public void run() {
        JFrame toplevel = new JFrame("Slide Puzzle - Java Edition");
        toplevel.setLocation(0, 0);

        final SlideBoard mb = new SlideBoard();

        toplevel.add(mb, BorderLayout.CENTER);
        toplevel.pack();
        toplevel.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        toplevel.setVisible(true);
        toplevel.setResizable(false);
    }
    
}
