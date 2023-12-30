export function score(x: number, y: number): number {
  // x**2 + y**2 = radius**2
  const pointsSquared: number = x * x + y * y;
  // return from the inside out so we can use the less than argument
  if (pointsSquared <= 1) {
    return 10;
  } else if (pointsSquared <= 25) {
    return 5;
  } else if (pointsSquared <= 100) {
    return 1;
  } else {
    return 0;
  }
}
