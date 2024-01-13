package java;

public record Point(int x, int y) {
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
