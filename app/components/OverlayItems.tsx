import { View } from "react-native";
import { Button } from "~/components/ui/button";
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "~/components/ui/hover-card";
import { Text } from "~/components/ui/text";
import { LoungeStatus } from "~/types";

interface OverlayItems {
  loungeStatus: LoungeStatus[];
}

const OverlayItems: React.FC<OverlayItems> = ({ levelStatus }) => {
  return (
    <HoverCard>
      <HoverCard>
        <HoverCardTrigger asChild>
          <Button variant="link" size="lg">
            <Text className="text-black">Hover trigger</Text>
          </Button>
        </HoverCardTrigger>
        <HoverCardContent className="">
          <View>
            <Text>Hello lounge</Text>
          </View>
        </HoverCardContent>
      </HoverCard>
    </HoverCard>
  );
};

export default OverlayItems;
