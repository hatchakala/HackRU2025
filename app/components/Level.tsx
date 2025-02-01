import { Text } from "~/components/ui/text";
import {
  AccordionItem,
  AccordionTrigger,
  AccordionContent,
} from "./ui/accordion";
import { View } from "react-native";

interface LevelProps {
  level: number;
  isOpen: boolean;
}

const Level: React.FC<LevelProps> = ({ level, isOpen }) => {
  return (
    <AccordionItem value={`${level}`} className="border-none">
      <AccordionTrigger className="bg-zinc-800 border-none">
        <View className="w-full p-2">
          <Text
            className={`${
              isOpen ? "text-red-500" : "text-white"
            } text-center font-semibold`}
          >
            LEVEL {level}
          </Text>
        </View>
      </AccordionTrigger>
      <AccordionContent className="bg-zinc-800">
        <View>
          <Text className="text-white">Floor Map for level {level}</Text>
        </View>
      </AccordionContent>
    </AccordionItem>
  );
};

export default Level;
