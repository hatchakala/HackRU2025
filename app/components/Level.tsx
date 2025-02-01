import { Text } from "~/components/ui/text";
import {
  AccordionItem,
  AccordionTrigger,
  AccordionContent,
} from "./ui/accordion";
import { View } from "react-native";
import Level1Map from "~/lib/levelmaps/Level1";
import { LoungeStatus } from "~/types";

const DEMO_LOUGNE_STATUSE: LoungeStatus[] = [
  {
    loungeId: "11",
    noiseLevel: 1,
    peopleCount: 2,
  },
  {
    loungeId: "21",
    noiseLevel: 0,
    peopleCount: 2,
  },
  {
    loungeId: "31",
    noiseLevel: 2,
    peopleCount: 2,
  },
  {
    loungeId: "41",
    noiseLevel: 1,
    peopleCount: 2,
  },
  {
    loungeId: "51",
    noiseLevel: 0,
    peopleCount: 2,
  },
  {
    loungeId: "61",
    noiseLevel: 2,
    peopleCount: 2,
  },
  {
    loungeId: "71",
    noiseLevel: 0,
    peopleCount: 2,
  },
  {
    loungeId: "81",
    noiseLevel: 0,
    peopleCount: 2,
  },
  {
    loungeId: "91",
    noiseLevel: 1,
    peopleCount: 2,
  },
  {
    loungeId: "101",
    noiseLevel: 2,
    peopleCount: 2,
  },
  {
    loungeId: "111",
    noiseLevel: 1,
    peopleCount: 2,
  },
];

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
          <Level1Map lougneStatuses={DEMO_LOUGNE_STATUSE} />
        </View>
      </AccordionContent>
    </AccordionItem>
  );
};

export default Level;
