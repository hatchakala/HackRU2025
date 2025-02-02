import { View } from "react-native";
import { Button } from "~/components/ui/button";
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "~/components/ui/hover-card";
import { Text } from "~/components/ui/text";
import { LoungeStatus } from "~/types";
// import AnimatedCircles from "./AnimatedDots";

interface OverlayItems {
  loungeStatus: LoungeStatus;
  x: number;
  y: number;
}

const OverlayItem: React.FC<OverlayItems> = ({ loungeStatus, x, y }) => {
  return (
    <HoverCard className={`absolute z-10`} style={{ top: y, left: x }}>
      <HoverCard>
        <HoverCardTrigger asChild>
          <Button variant="link" size="lg">
            {/* {loungeStatus.loungeId === "51" && <AnimatedCircles />} */}
          </Button>
        </HoverCardTrigger>
        <HoverCardContent className="w-fit">
          <View>
            {/* <Text>Lounge: {loungeStatus.loungeId}</Text> */}
            <Text>Noise level: {loungeStatus.noiseLevel}</Text>
            <Text>People count: {loungeStatus.peopleCount}</Text>
          </View>
        </HoverCardContent>
      </HoverCard>
    </HoverCard>
  );
};

export default OverlayItem;
