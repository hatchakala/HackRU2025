import Svg, { Path } from "react-native-svg";
import { LoungeStatus } from "~/types";
import { getFillColor } from "./util";

interface LevelMap {
  loungeStatus: LoungeStatus[];
}

const Level3Map: React.FC<LevelMap> = ({ loungeStatus }) => {
  const [l1, l2, l3] = loungeStatus;
  return (
    <Svg
      width="322"
      height="226"
      viewBox="0 0 322 226"
      fill="none"
      //   xmlns="http://www.w3.org/2000/svg"
    >
      <Path
        d="M13.2912 213.453L41.4164 208.936L43.0588 218.174L63.3828 214.274L61.7405 205.241L90.2763 199.903L80.4222 155.97H83.7069V139.136H79.8063V82.8858H85.3493V81.4487V80.8329L87.8128 79.3958V74.4688L85.3493 72.4158V71.7999V69.9523H74.0581V66.0517H120.044H131.746L221.048 82.4752L224.949 70.1576L245.068 74.0582L238.293 96.8458V160.487H234.598V176.5H238.293V212.837H274.014V209.347H282.637V212.221H283.868V223.512H316.715V213.453H320V32.7941H284.895V31.1517L264.776 30.7411V33.6153H254.717L253.69 37.1053L236.035 32.9994L239.525 20.2712L145.911 2.61588L145.09 5.90058L133.388 3.64235V2H53.1181V4.87411H46.3434V2L19.6553 2.41059L19.0394 49.0123H7.95352V51.4758H6.31117V72.2105H12.2647V81.2434H2V155.56L13.2912 213.453Z"
        stroke="white"
        stroke-width="3"
        fill="#4B4B4B"
      />
      <Path
        d="M13.2927 71.5945H44.0868V82.6803H13.2927V71.5945Z"
        stroke="white"
        stroke-width="3"
        fill={getFillColor(l1.noiseLevel)}
      />
      <Path
        d="M235.008 35.2573L224.333 68.1044L246.504 72.2103L257.18 40.8003L235.008 35.2573Z"
        stroke="white"
        stroke-width="3"
        fill={getFillColor(l2.noiseLevel)}
      />
      <Path
        d="M318.156 198.26H285.925V221.664H315.282V211.399H318.156V198.26Z"
        stroke="white"
        stroke-width="3"
        fill={getFillColor(l3.noiseLevel)}
      />
    </Svg>
  );
};

export default Level3Map;
