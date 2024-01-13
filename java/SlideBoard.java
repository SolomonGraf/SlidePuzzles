package java;

import javax.swing.*;

public class SlideBoard extends JComponent {
    
    private SlideModel model;

    public SlideBoard() {
        this.model = new SlideModel(3);
    }

}
