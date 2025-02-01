import { Card } from "~/components/ui/card";
import { Text } from "~/components/ui/text";
import {
  AccordionItem,
  AccordionTrigger,
  AccordionContent,
} from "./ui/accordion";

interface LevelProps {
  level: number;
}

const Level: React.FC<LevelProps> = ({ level }) => {
  return (
    <AccordionItem value={`item-${level}`}>
      <AccordionTrigger>
        <Card>
          <Text>Level {level}</Text>
        </Card>
      </AccordionTrigger>
      <AccordionContent>
        <Card>
          <Text>Floor Map for level {level}</Text>
        </Card>
      </AccordionContent>
    </AccordionItem>
  );
};

export default Level;
