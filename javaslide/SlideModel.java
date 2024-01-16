package javaslide;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Random;

public class SlideModel {
    
    private final int[][] board;
    private final int size;
    private Point current;

    public SlideModel(int size){
        this.board = generateBoard(size);
        this.size = size;
        this.current = new Point(size - 1, size-1);
    }

    private int[][] generateBoard(int size){
        if (size > 5 || size < 3) {
            throw new IllegalArgumentException("Size must be between 3 and 5");
        }
        int[][] board = new int[size][size];
        for (int row = 0; row < size; row++) {
            for (int column = 0; column < size; column++) {
                board[row][column] = size * row + column + 1;
            }
        }
        board[size-1][size-1] = -1;
        return board;
    }

    private boolean isAdjacent(Point p1, Point p2) {
        return Math.abs(p1.x() - p2.x()) + Math.abs(p1.y()-p2.y()) == 1;
    }

    private boolean inRange(Point p) {
        int x = p.x();
        int y = p.y();
        return x >= 0 && x < size && y >= 0 && y < size;
    }

    public int value(int row, int column) {
        return board[column][row];
    }

    public Point getCurrent() {
        return this.current;
    }

    public void setCurrent(Point p) {
        current = p;
    }

    public int getSize() {
        return this.size;
    }

    public void swap(Point p1, Point p2) {
        int x1 = p1.x();
        int y1 = p1.y();
        int x2 = p2.x();
        int y2 = p2.y();

        if (!isAdjacent(p1, p2)) {
            throw new IllegalArgumentException("Boxes are not adjacent");
        }
        int temp = this.board[y1][x1];
        this.board[y1][x1] = this.board[y2][x2];
        this.board[y2][x2] = temp;
    }

    public boolean isCorrect() {
        int[][] expected = generateBoard(this.size);
        return Arrays.deepEquals(expected, this.board);
    }

    private List<Point> getNeighbors(Point point) {
        int x = point.x();
        int y = point.y();
        List<Point> neighbors = new LinkedList<>();
        neighbors.add(new Point(x+1,y));
        neighbors.add(new Point(x-1,y));
        neighbors.add(new Point(x,y+1));
        neighbors.add(new Point(x,y-1));
        neighbors = neighbors.stream().filter(this::inRange).toList();
        return neighbors;
    }

    public void shuffle() {
        for (int i = 0; i < 100; i++) {
            Random rand = new Random();
            List<Point> neighbors = getNeighbors(current);
            Point randomNeighbor = neighbors.get(rand.nextInt(neighbors.size()));
            swap(randomNeighbor, current);
            current = randomNeighbor;
        }
    }

}
