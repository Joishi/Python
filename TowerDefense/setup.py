from tower_defense.path import Path
from tower_defense.path import Point


def main():
    path = Path()
    path.addPoint(Point(2, 5))
    path.addPoint(Point(5, 4))
    path.addPoint(Point(7, 10))
    print(str(path.totalDistance()))


if __name__ == "__main__":
    main()
