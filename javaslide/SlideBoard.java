package javaslide;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.geom.Rectangle2D;
import java.io.File;

public class SlideBoard extends JComponent {
    
    private SlideModel model;

    private final static int BOARD_SIZE = 600;
    private final static int BAR_HEIGHT = 100;

    public SlideBoard() {
        this.model = new SlideModel(3);
        this.model.shuffle();
        this.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                handle(e);
            }
        });
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        int squareSize = BOARD_SIZE / model.getSize();
        int size = model.getSize();
        for (int row = 0; row < size; row++) {
            for (int column = 0; column < size; column++) {
                String number = Integer.toString(this.model.value(column, row));
                if (!number.equals("-1")) {
                    g.setColor(Color.GRAY);
                    g.fillRect(squareSize * column, squareSize * row, squareSize, squareSize);
                    g.setColor(Color.BLACK);
                    g.drawRect(squareSize * column, squareSize * row, squareSize, squareSize);
                    writeCenteredText(g, number, squareSize * column, squareSize * row, squareSize, squareSize);
                } else {
                    g.setColor(new Color(220,220,220));
                    g.fillRect(squareSize * column, squareSize * row, squareSize, squareSize);
                }
            }
        }
        for (int i = 3; i <= 5; i++) {
            g.setColor(new Color(50, 70, 132));
            int buttonWidth = 200;
            g.fillRect((i-3)*buttonWidth,BOARD_SIZE,buttonWidth,BAR_HEIGHT);
            g.setColor(new Color(40,60,80));
            writeCenteredText(g,Integer.toString(i),(i-3)*buttonWidth,BOARD_SIZE,buttonWidth,BAR_HEIGHT);
        }
        if (model.isCorrect()) {
            g.setColor(new Color(111, 142, 173));
            int winSquareSize = 400;
            g.fillRect(BOARD_SIZE/2 - winSquareSize/2, BOARD_SIZE/2 - winSquareSize/2, winSquareSize, winSquareSize);
            g.setColor(Color.BLACK);
            g.drawRect(BOARD_SIZE/2 - winSquareSize/2, BOARD_SIZE/2 - winSquareSize/2, winSquareSize, winSquareSize);
            writeCenteredText(g, "You Won!", BOARD_SIZE/2 - winSquareSize/2, BOARD_SIZE/2 - winSquareSize/2, winSquareSize, winSquareSize);
        }
    }

    private static void writeCenteredText(Graphics g, String text, int x, int y, int width, int height) {
        Font boldFont = Font.getFont("Arial");
        try {
            boldFont = Font.createFont(Font.TRUETYPE_FONT, new File("files/boldFont.ttf")).deriveFont(48f);
        } catch (Exception ignored) {
        }
        g.setFont(boldFont);
        Rectangle2D bounds = boldFont.getStringBounds(text, ((Graphics2D) g).getFontRenderContext());
        int textHeight = (int) bounds.getHeight();
        int textWidth = (int) bounds.getWidth();
        g.drawString(text, x + width / 2 - textWidth / 2, y + height / 2 + textHeight / 2);
    }

    public void handle(MouseEvent e) {
        if (e.getY() > 600) {
            handleButton(e);
        } else {
            handleBoard(e);
        }
        repaint();
    }

    private void handleBoard(MouseEvent e) {
        if (!model.isCorrect()) {
            int squareSize = BOARD_SIZE / model.getSize();
            int row = e.getY() / squareSize;
            int column = e.getX() / squareSize;
            Point clickedPoint = new Point(column, row);
            try {
                model.swap(clickedPoint, model.getCurrent());
                model.setCurrent(clickedPoint);
            } catch (IllegalArgumentException ignored) {
            }
        }
    }

    private void handleButton(MouseEvent e) {
        int buttonVal = 3 + (e.getX() / 200);
        this.model = new SlideModel(buttonVal);
        this.model.shuffle();
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(BOARD_SIZE,BOARD_SIZE+BAR_HEIGHT);
    }

}
