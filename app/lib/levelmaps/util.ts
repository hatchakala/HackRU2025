export const getFillColor = (noiseLevel: number) => {
  switch (noiseLevel) {
    case 0:
      return "blue";
    case 1:
      return "yellow";
    case 2:
      return "orange";
    case 3:
      return "red";
    default:
      break;
  }
};
