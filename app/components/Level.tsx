import { Text } from "~/components/ui/text";
import {
  AccordionItem,
  AccordionTrigger,
  AccordionContent,
} from "./ui/accordion";
import { View } from "react-native";
import LevelMap from "~/lib/levelmaps/Level1";
import { DEMO_LOUGNE_STATUSE } from "~/DummyData";
import OverlayL1 from "~/lib/levelmaps/OverlayL1";
import LEVELS from "~/lib/levelmaps/index";

interface LevelProps {
  level: number;
  isOpen: boolean;
}

const Level: React.FC<LevelProps> = ({ level, isOpen }) => {
  return (
    <AccordionItem value={`${level}`} className="border-none">
      <AccordionTrigger className="border-none">
        <View className="w-full p-2">
          <Text
            className={`${
              isOpen ? "text-red-500" : "text-black"
            } text-center font-semibold`}
          >
            LEVEL {level}
          </Text>
        </View>
      </AccordionTrigger>
      <AccordionContent className="">
        <View className="items-center">
          <OverlayL1 levelStatus={DEMO_LOUGNE_STATUSE} />
          {LEVELS[level - 1](DEMO_LOUGNE_STATUSE)}
        </View>
      </AccordionContent>
    </AccordionItem>
  );
};

export default Level;
