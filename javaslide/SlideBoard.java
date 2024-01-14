package javaslide;

import javax.swing.*;
import java.awt.*;
import java.awt.geom.Rectangle2D;
import java.io.File;

public class SlideBoard extends JComponent {
    
    private SlideModel model;

    private final static int BOARD_SIZE = 600;
    private final static int BAR_HEIGHT = 100;

    public SlideBoard() {
        this.model = new SlideModel(3);
        this.model.shuffle();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        int squareSize = BOARD_SIZE / model.getSize();
        int size = model.getSize();
        for (int row = 0; row < size; row++) {
            for (int column = 0; column < size; column++) {
                g.setColor(Color.DARK_GRAY);
                g.fillRect(squareSize*column, squareSize*row, squareSize, squareSize);
                g.setColor(Color.BLACK);
                Font boldFont = Font.getFont("Arial");
                try {
                    boldFont = Font.createFont(Font.TRUETYPE_FONT, new File("files/boldfont.ttf")).deriveFont(48f);
                } catch (Exception ignored) {}
                g.setFont(boldFont);
                String number = Integer.toString(this.model.value(column, row));
                Rectangle2D bounds = boldFont.getStringBounds(number, ((Graphics2D) g).getFontRenderContext());
                int textHeight = (int) bounds.getHeight();
                int textWidth = (int) bounds.getWidth();
                g.drawString(Integer.toString(size * row + column + 1), squareSize*column + squareSize/2 - textWidth/2, squareSize*row + squareSize/2 + textHeight/2);
            }
        }
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(BOARD_SIZE,BOARD_SIZE+BAR_HEIGHT);
    }

}
